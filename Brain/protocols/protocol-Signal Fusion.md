---
tags: [brain, protocol, inference]
aliases: [Signal Fusion, protocol-Signal Fusion]
type: protocol
---

# Protocol — Signal Fusion

Used by [[fn-Inference]] · Doctrine from [[07_calibration_fusion_length]]

## Principles
1. Raw scores are **not** probabilities until calibrated.
2. Fusion must be **context-weighted**, not equal average of everything.
3. Always emit **uncertainty** band.
4. Prefer **complementary** families (stat + semantic + external) over many redundant lexical hits.

## Suggested weight priors (EN, long text, native, black-box)

| Family | Prior weight | Notes |
|--------|-------------:|-------|
| External evidence | 0.30 | If present; else redistribute |
| Watermark z / SynthID | 0.25 | If applicable |
| Binoculars / Fast-DetectGPT | 0.20 | Robust cluster |
| Semantic (citations, voice) | 0.15 | |
| Structural + linguistic bag | 0.07 | Correlated; cap influence |
| Commercial single score | 0.03 | Until local audit |
| Perfect-grammar / em-dash alone | ~0 | Diagnostic only |

## Adjustments
- Non-native: ×0.5 on PPL/grammar/TTR-like; ×1.3 semantic+external
- Short text: ×0.3 statistical curvature/PPL; ×1.4 structural/linguistic
- Arabic: EN classifiers → weight 0; semantic+local+external only
- Mixed: fuse **per segment**, then distribution over segments (not one doc score)

## Calibration options
- Platt scaling / isotonic on local labeled set
- Logistic meta-model on feature vector
- Report score as `uncalibrated_score` vs `calibrated_p` explicitly

## Ensemble baseline (taxonomy)
**Binoculars + Fast-DetectGPT + TTR + z-score(if any) + human review**

## Output
```yaml
fusion:
  calibrated_p_ai: null
  uncalibrated_score: null
  uncertainty: high|med|low
  top_drivers: []
  discounts_applied: []
```

Continue to [[fn-Making Decision]].
