---
tags: [brain, function, understanding]
aliases: [Understanding, fn-Understanding, الفهم]
type: cognitive-function
function_id: 02
---

# fn-Understanding — Make sense of perceived data

**Role:** Turn raw sensor hits into meaningful claims with known failure modes.

## Understanding layers

### 1. What the signal *means*
| Signal family | Meaning | Primary source |
|---------------|---------|----------------|
| Low PPL / low burstiness | High predictability / uniformity | [[moc-Core Signals]] STAT |
| Curvature (DetectGPT / Fast) | Local valley in log-prob landscape | BB/WB + STAT |
| Binoculars ratio | Cross-model PPL discrepancy | STAT-010, BB-006 |
| Green-list z-score | Active watermark presence | KGW, WB-013 |
| Lexical / structural | Style fingerprint of LLM defaults | LM, STRUCT |
| Semantic | Content-level AI tells | SEM |
| Commercial score | Opaque ensemble output | CD + [[06_commercial_claims_critique]] |

### 2. What it *does not* mean
- Score ≠ calibrated P(AI) → [[07_calibration_fusion_length]]
- High score on non-native EN ≠ guilt → [[01_false_positives_non_native]]
- EN detector on AR text ≠ valid → [[03_arabic_detection]]
- Document-level AI on mixed text ≠ whole document AI → [[04_mixed_texts]]
- Any pure-text detector alone ≠ proof → [[02_impossibility_theorem]], [[05_external_evidence]]

### 3. Conceptual distinctions (from Agent B analytical brief)
- **Green Observed** (GLTR top-rank tokens) ≠ **Green Planted** (KGW watermark lists)
- **Black-box** (no source model) ≠ **White-box** (logits) ≠ **Green-box** (watermark key)
- **Claimed commercial accuracy** ≠ **independent / local evaluation**

## Understanding protocol

1. For each hit from [[fn-Perception]], attach:
   - `interpretation`
   - `confidence` (from JSON pattern)
   - `failure_modes` (gap links)
   - `evasion_ease` (from taxonomy: easiest_to_evade)
2. Resolve contradictions (e.g. high linguistic AI + high personal voice → mixed).
3. Output a **case narrative** for [[fn-Context Building]] and [[fn-Inference]].

## Output schema

```yaml
understanding:
  narrative: "..."
  signal_meanings: []
  contradictions: []
  doctrine_applied: [gap-ids]
  readiness_for_inference: true|false
```

## Links

- Upstream: [[fn-Perception]]
- Downstream: [[fn-Context Building]], [[fn-Inference]], [[fn-Linking]]
- Hub: [[00_FULL_BRAIN]]
