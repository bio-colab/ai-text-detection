---
tags: [brain, function, inference]
aliases: [Inference, fn-Inference, الاستدلال]
type: cognitive-function
function_id: 06
---

# fn-Inference — From signals to beliefs

**Role:** Fuse evidence into calibrated posterior beliefs, not marketing scores.

## Inference model (practical Bayesian frame)

```
P(AI | evidence) ∝ P(evidence | AI) · P(AI)
```

- **Prior P(AI)** = context base rate (default 0.05–0.15 academic; never 0.5 blindly) → [[01_false_positives_non_native]]
- **Likelihoods** from pattern confidences in core JSON (treat as *relative* strengths, not true probs until calibrated)
- **Evidence classes:** internal statistical · linguistic · structural · semantic · watermark · external

## Fusion protocol → [[protocol-Signal Fusion]]

1. **Normalize** raw scores to comparable [0,1] bands per family.
2. **Weight by context:**
   - Short text → ↓ statistical, ↑ linguistic/structural
   - Non-native → ↓ PPL/grammar-perfect, ↑ semantic/external
   - Arabic → EN classifiers weight ≈ 0 until local model exists
   - Watermark z>4 → strong independent evidence (different mechanism)
3. **Meta-fusion options:**
   - Weighted average + uncertainty band
   - Logistic meta-classifier (local training preferred)
   - Platt / isotonic calibration when labels exist ([[07_calibration_fusion_length]])
4. **Contradiction handling:** mixed indicators → raise P(mixed) not force binary.

## Output belief state

```yaml
inference:
  p_ai_document: null      # calibrated if possible
  p_mixed: null
  p_human: null
  uncertainty: low|med|high
  drivers: []              # top contributing signals
  suppressors: []          # gaps that reduced confidence
  ensemble_used: "Binoculars+FastDetectGPT+TTR+external"
  ready_for_decision: true|false
```

## Hard constraints on inference

- Impossibility theorem: pure distributional detection fails as models approach human ([[02_impossibility_theorem]]).
- Uncalibrated score ≠ probability ([[07_calibration_fusion_length]]).
- Commercial claims discounted until local audit ([[06_commercial_claims_critique]]).

## Links

- Upstream: [[fn-Understanding]], [[fn-Pattern Recognition]], [[fn-Context Building]]
- Downstream: [[fn-Making Decision]], [[fn-Predicting]]
- Protocol: [[protocol-Signal Fusion]]
- Hub: [[00_FULL_BRAIN]]
