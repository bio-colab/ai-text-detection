---
tags: [brain, function, predicting]
aliases: [Predicting, fn-Predicting, التنبؤ]
type: cognitive-function
function_id: 14
---

# fn-Predicting — Anticipate risks and futures

**Role:** Forecast failure modes before they become unjust decisions or dead signals.

## Prediction targets

### 1. Positive predictive value (PPV)
Given base rate + FPR/TPR, predict how many flags are false:
```
PPV = TPR·π / (TPR·π + FPR·(1-π))
```
Example from gap 01: class of 100, π=10%, FPR=3% → many false accusations risk.

### 2. Non-native FP inflation
Predict 2–4× FPR on L2 English academic writing → auto-raise review threshold.

### 3. Signal half-life
- Lexical fashion (delve, tapestry): **short** (6–18 months)
- Structural LLM defaults: **medium**
- Curvature / Binoculars-class: **longer but not immortal**
- Watermark (if mandated): **stable while scheme lives**
- External evidence: **most stable**

### 4. Model generation drift
New frontier models + humanizers → drop AUROC; predict need for re-benchmark after each major release.

### 5. Mixed-text prevalence
Predict most real cases are hybrid → plan segment-level detection default.

### 6. Arabic gap trajectory
Without local corpus, predict continued unreliability of EN tools on AR indefinitely.

## Prediction card

```yaml
predictions:
  p_false_accusation_if_auto_punish: high
  signal_obsolescence_12m: [LM-001, LM-002, em-dash]
  ensemble_degradation_risk: medium
  need_retrain_by: "2026-Q4"
  arabic_readiness: low
```

Feeds [[fn-Planning]] and [[fn-Priority Administration]].

## Links

- Gaps: [[01_false_positives_non_native]], [[08_signal_obsolescence]], [[02_impossibility_theorem]]
- Related: [[fn-Watching]], [[fn-Inference]]
- Hub: [[00_FULL_BRAIN]]
