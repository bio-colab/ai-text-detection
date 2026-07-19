---
tags: [brain, function, perception]
aliases: [Perception, fn-Perception, الإدراك]
type: cognitive-function
function_id: 01
---

# fn-Perception — Accept data from all components

**Role:** Sensor layer. Ingest raw inputs and component outputs without interpreting yet.

## Inputs accepted

| Channel | Source in vault | What is sensed |
|---------|-----------------|----------------|
| Text payload | User / case file | Raw string, length, language guess |
| Linguistic layer | `core/01_linguistic_markers.json` | Lexical hits (delve, em-dash, transitions…) |
| Statistical layer | `core/02_statistical_signals.json` | PPL, burstiness, curvature, Binoculars… |
| Green-box / watermark | `core/03_green_box_watermark.json` | z-score, SynthID g-values |
| Black-box methods | `core/04_black_box_detection.json` | Proxy scores, lexicon, TTR |
| White-box methods | `core/05_white_box_detection.json` | Logprobs, ranks, entropy |
| Commercial tools | `core/06_commercial_detectors.json` | GPTZero, Turnitin, Originality… |
| Open-source tools | `core/07_open_source_detectors.json` | RoBERTa, Binoculars, MAGE, RAID… |
| Structural | `core/08_structural_formatting_signals.json` | Emoji bullets, markdown, symmetry |
| Semantic | `core/09_semantic_coherence_signals.json` | Hallucination, citations, voice |
| External evidence | [[05_external_evidence]] | Version history, metadata, oral |
| Gap constraints | [[moc-Gaps]] | Limits that must bound perception |

## Perception checklist (run every case)

```yaml
perception:
  text_length_words: null
  language: [en | ar | mixed | other]
  segments: []          # for mixed-text sentence-level
  signals_received:
    linguistic: []
    statistical: []
    structural: []
    semantic: []
    watermark: []
    commercial: []
    open_source: []
    external: []
  missing_sensors: []   # e.g. no logits → no white-box
  integrity_flags:
    non_native_risk: null
    short_text: null    # <250–300 words
    mixed_suspected: null
```

## Rules

1. **Accept all** — do not drop weak signals early; [[fn-Priority Administration]] weights later.
2. **Mark missing** — white-box needs logits; watermark needs key/schema.
3. **Language gate** — if Arabic, route warning from [[03_arabic_detection]] before any EN model score is trusted.
4. **Length gate** — if short, flag statistical unreliability ([[07_calibration_fusion_length]]).
5. Handoff → [[fn-Understanding]] + [[fn-Pattern Recognition]].

## Links

- Upstream: world / case intake
- Downstream: [[fn-Understanding]], [[fn-Pattern Recognition]], [[fn-Context Building]]
- Orchestrator: [[fn-Orchestration]]
- Hub: [[00_FULL_BRAIN]]
