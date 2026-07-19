---
tags: [brain, function, priority]
aliases: [Priority Administration, fn-Priority Administration, إدارة الأولويات]
type: cognitive-function
function_id: 11
---

# fn-Priority Administration — What matters first

**Role:** Order work, signals, and gaps by impact under resource limits.

## Static priority: gaps (from README)

| Rank | Gap | Priority | Note |
|-----:|-----|----------|------|
| 1 | [[03_arabic_detection]] | ★★★★★★★★★★ | Highest for Arabic context |
| 2 | [[05_external_evidence]] | ★★★★★★ | Strongest practical evidence |
| 3 | [[01_false_positives_non_native]] | ★★★★★ | Justice / FP paradox |
| 4 | [[04_mixed_texts]] | ★★★★★ | Most common real case |
| 5 | [[02_impossibility_theorem]] | ★★★★ | Sets expectations |
| 6 | [[07_calibration_fusion_length]] | ★★★★ | Engineering maturity |
| 7 | [[06_commercial_claims_critique]] | ★★★★ | Procurement honesty |
| 8 | [[08_signal_obsolescence]] | ★★★★ | Maintenance |

## Runtime priority: signals in a case

| Priority | Prefer when… |
|----------|----------------|
| External evidence | Always high if available |
| Watermark z / SynthID | Scheme known |
| Semantic (citations, hallucination) | Non-native or AR |
| Binoculars + Fast-DetectGPT | EN, length OK, models available |
| Structural / linguistic | Short text |
| Commercial scores | Lowest trust until audited; use as weak prior only |
| Em-dash / delve alone | Lowest — easy evade, short half-life |

## Queue management

Live queue: [[queue-Priorities]]

Operations:
- `P0` — safety/justice (FP, AR misuse)
- `P1` — capability building (corpus, calibration)
- `P2` — ensemble engineering
- `P3` — cosmetic taxonomy polish

Recompute priorities after every [[fn-Watching]] cycle or major model release.

## Links

- Queue: [[queue-Priorities]]
- Related: [[fn-Planning]], [[fn-Orchestration]]
- Hub: [[00_FULL_BRAIN]]
