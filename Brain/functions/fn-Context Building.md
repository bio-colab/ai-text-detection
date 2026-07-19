---
tags: [brain, function, context]
aliases: [Context Building, fn-Context Building, بناء السياق]
type: cognitive-function
function_id: 04
---

# fn-Context Building — Situate the case

**Role:** Build the situational frame that changes how all other functions behave.

## Context dimensions

| Dimension | Values | Impact |
|-----------|--------|--------|
| Language | EN / AR / mixed | AR → disable EN-only trust ([[03_arabic_detection]]) |
| Writer profile | native / non-native / unknown | Raise FP risk ([[01_false_positives_non_native]]) |
| Text length | <250 / 250–500 / >500 words | Short → deweight stats ([[07_calibration_fusion_length]]) |
| Genre | essay, abstract, blog, chat | Formulaic genres inflate structural AI scores |
| Purity | pure-AI / pure-human / mixed | Mixed → segment-level ([[04_mixed_texts]]) |
| Stakes | educational, legal, research | High stakes → mandatory human review |
| Available sensors | black / white / green / external | Missing sensors → higher uncertainty |
| Domain base rate | estimated AI prevalence | Drives positive predictive value ([[01_false_positives_non_native]]) |
| Student baseline | available / missing | Fingerprint compare ([[05_external_evidence]]) |

## Context card template

```yaml
context:
  case_id: ""
  language: en
  length_words: 0
  writer: non_native_possible
  genre: academic_essay
  purity_hypothesis: mixed
  stakes: academic_integrity
  base_rate_ai: 0.10
  sensors:
    white_box: false
    watermark_key: false
    version_history: false
    oral_defense: false
  policy:
    punish_on_score_alone: false   # ALWAYS false
    require_human_review: true
```

## Context → routing rules

- `language=ar` → [[fn-Planning]] Arabic path; semantic + local classifier focus.
- `length<250` → linguistic + structural + semantic only for primary weight.
- `purity=mixed` → sentence/paragraph segmentation pipeline.
- `stakes=high` → [[protocol-Human Review]] mandatory.
- `version_history=true` → elevate external evidence weight.

Handoff → [[fn-Inference]] with full context card.

## Links

- Upstream: [[fn-Perception]], [[fn-Understanding]]
- Downstream: [[fn-Inference]], [[fn-Planning]], [[fn-Making Decision]]
- Hub: [[00_FULL_BRAIN]]
