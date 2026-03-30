#!/usr/bin/env python3
from __future__ import annotations
import argparse, importlib.util, sys, json, math
from pathlib import Path
from typing import Dict, List, Tuple, Any

ORIG_PATH = Path(__file__).with_name("HPF_QPRCA_MicroToy_v0_2_7_BridgedContinuationAmbiguity_2026-03-20.py")

def load_orig():
    spec = importlib.util.spec_from_file_location("hpfv27_wrapped", ORIG_PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod

def unpack_pair(mod, pair):
    l, r = pair
    return mod.unpack_site(l), mod.unpack_site(r)

def active_transport_totals(mod, pair):
    (nLl, nRl, _, _), (nLr, nRr, _, _) = unpack_pair(mod, pair)
    return {
        "left_dir_total": nLl + nLr,
        "right_dir_total": nRl + nRr,
        "site_totals": [nLl + nRl, nLr + nRr],
        "transport_total": nLl + nRl + nLr + nRr,
    }

def classify_transport_outcome(mod, in_pair, out_pair):
    it = active_transport_totals(mod, in_pair)
    ot = active_transport_totals(mod, out_pair)
    if it["transport_total"] > 0 and ot["transport_total"] == 0:
        return "quenched"
    if ot["left_dir_total"] > ot["right_dir_total"]:
        return "left_biased"
    if ot["right_dir_total"] > ot["left_dir_total"]:
        return "right_biased"
    if ot["transport_total"] > 0:
        return "balanced"
    return "inactive"

def classify_resource_engagement(mod, in_pair, out_pair):
    (inL, inR) = in_pair
    (outL, outR) = out_pair
    (_, _, bL0, qL0), (_, _, bR0, qR0) = mod.unpack_site(inL), mod.unpack_site(inR)
    (_, _, bL1, qL1), (_, _, bR1, qR1) = mod.unpack_site(outL), mod.unpack_site(outR)
    b_changed = (bL0 != bL1) or (bR0 != bR1)
    q_changed = (qL0 != qL1) or (qR0 != qR1)
    if b_changed and q_changed:
        return "both"
    if b_changed:
        return "storage"
    if q_changed:
        return "queue"
    return "none"

def classify_collision_mode(mod, in_pair, out_pair):
    it = active_transport_totals(mod, in_pair)
    ot = active_transport_totals(mod, out_pair)
    r_eng = classify_resource_engagement(mod, in_pair, out_pair)
    input_conflict = max(it["site_totals"]) >= 2
    rerouted = (it["site_totals"] != ot["site_totals"]) or (
        it["left_dir_total"] != ot["left_dir_total"] or it["right_dir_total"] != ot["right_dir_total"]
    )
    buffered = (r_eng != "none") and (ot["transport_total"] < it["transport_total"] or r_eng in {"storage", "both", "queue"})
    if rerouted and buffered and input_conflict:
        return "mixed"
    if buffered and input_conflict:
        return "buffer"
    if rerouted and input_conflict:
        return "reroute"
    return "pass"

def compute_sigma(mod, in_pair, out_pair):
    return (
        classify_transport_outcome(mod, in_pair, out_pair),
        classify_collision_mode(mod, in_pair, out_pair),
        classify_resource_engagement(mod, in_pair, out_pair),
    )

def get_sanitized_reversible_subregistry(mod):
    toy = mod.QPRCAMicroToyV020()
    return {name: mod.RULES[name] for name, ok in toy.bijection_check.items() if ok}

def evaluate_rule(mod, toy, in_pair, rule_name):
    fn = mod.RULES[rule_name]
    out_pair = fn(*in_pair)
    p_burden = continuation_burden(mod, in_pair)
    bL = toy.site_burdens(in_pair[0], out_pair[0], in_pair[0])
    bR = toy.site_burdens(in_pair[1], out_pair[1], in_pair[1])
    F_left, scores_left = toy._site_F(in_pair[0], bL, p_burden)
    F_right, scores_right = toy._site_F(in_pair[1], bR, p_burden)
    return {
        "out_pair": out_pair,
        "sigma": compute_sigma(mod, in_pair, out_pair),
        "F_left": F_left,
        "F_right": F_right,
        "F_block": max(F_left, F_right),
        "accepted": max(F_left, F_right) < 1.0,
        "scores_left": scores_left,
        "scores_right": scores_right,
    }

def continuation_classes(mod, in_pair):
    rules = get_sanitized_reversible_subregistry(mod)
    grouped: Dict[Tuple[str, str, str], List[str]] = {}
    for rule_name in rules:
        out_pair = mod.RULES[rule_name](*in_pair)
        sigma = compute_sigma(mod, in_pair, out_pair)
        grouped.setdefault(sigma, []).append(rule_name)
    return grouped

def continuation_neff(mod, in_pair):
    grouped = continuation_classes(mod, in_pair)
    total = sum(len(v) for v in grouped.values())
    probs = [len(v) / total for v in grouped.values()]
    denom = sum(p * p for p in probs)
    return 1.0 / max(1e-12, denom)

def continuation_burden(mod, in_pair):
    rules = get_sanitized_reversible_subregistry(mod)
    neff = continuation_neff(mod, in_pair)
    neff_max = float(max(1, len(rules)))
    if neff_max <= 1.0:
        return 0.0
    return max(0.0, min(1.0, math.log(neff) / math.log(neff_max)))

def evaluate_existence_sensor(mod, aggregate_mode="grouped_l2", model_mode="baseline"):
    toy = mod.QPRCAMicroToyV020(model_mode=model_mode, aggregate_mode=aggregate_mode)
    rules = list(get_sanitized_reversible_subregistry(mod).keys())
    results = []
    confusion = {"true_positive":0,"true_negative":0,"false_positive":0,"false_negative":0}
    for inL in range(16):
        for inR in range(16):
            in_pair = (inL, inR)
            evals = [evaluate_rule(mod, toy, in_pair, rn) for rn in rules]
            F_min = min(x["F_block"] for x in evals)
            exists = any(x["accepted"] for x in evals)
            if F_min < 1.0 and exists:
                label = "true_positive"; confusion[label]+=1
            elif F_min >= 1.0 and not exists:
                label = "true_negative"; confusion[label]+=1
            elif F_min < 1.0 and not exists:
                label = "false_positive"; confusion[label]+=1
            else:
                label = "false_negative"; confusion[label]+=1
            results.append({
                "input_pair":[inL,inR],
                "continuation_classes":{" | ".join(sig): members for sig,members in continuation_classes(mod, in_pair).items()},
                "continuation_class_count": len(continuation_classes(mod, in_pair)),
                "continuation_neff": continuation_neff(mod, in_pair),
                "P_cont": continuation_burden(mod, in_pair),
                "F_min": F_min,
                "exists_legal_continuation": exists,
                "confusion_label": label,
            })
    return {
        "aggregate_mode": aggregate_mode,
        "model_mode": model_mode,
        "sanitized_rule_names": rules,
        "sanitized_rule_count": len(rules),
        "confusion_matrix": confusion,
        "results": results,
    }

def sigma_pressure_test(mod):
    sample_inputs = [(0,0),(1,0),(3,0),(3,3),(7,3),(15,15),(6,9),(12,5)]
    cases=[]
    for in_pair in sample_inputs:
        group = continuation_classes(mod, in_pair)
        cases.append({
            "input_pair": list(in_pair),
            "class_count": len(group),
            "classes": {" | ".join(sig): members for sig,members in group.items()}
        })
    return {
        "purpose":"adversarial pre-lock spot check of candidate Sigma equivalence",
        "sample_cases": cases
    }

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--demo", choices=["sigma_pressure_test","existence_sensor"], required=True)
    p.add_argument("--aggregate-mode", choices=["additive","max","grouped_l2"], default="grouped_l2")
    p.add_argument("--model-mode", choices=["baseline","refined"], default="baseline")
    p.add_argument("--output", default="")
    args=p.parse_args()
    mod=load_orig()
    out = sigma_pressure_test(mod) if args.demo=="sigma_pressure_test" else evaluate_existence_sensor(mod, args.aggregate_mode, args.model_mode)
    text=json.dumps(out, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    else:
        print(text)

if __name__ == "__main__":
    main()
