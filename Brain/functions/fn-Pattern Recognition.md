---
tags: [brain, function, pattern-recognition]
aliases: [Pattern Recognition, fn-Pattern Recognition, التعرف على الأنماط]
type: cognitive-function
function_id: 07
---

# fn-Pattern Recognition — Match known AI-detection patterns

**Role:** Scan text (and metadata) against the catalogued pattern library (~174 patterns + reference patterns).

## Pattern libraries (perception targets)

| Library | Count | File / MOC |
|---------|------:|------------|
| Linguistic markers | 20 | `core/01` · LM-001…020 |
| Statistical signals | 14 | `core/02` · STAT-001…014 |
| Green-box watermark | 19 | `core/03` · KGW-001…019 |
| Black-box detection | 21 | `core/04` · BB-001…021 |
| White-box detection | 19 | `core/05` · WB-001…019 |
| Commercial patterns | 22 | `core/06` · CD-001…022 |
| Open-source patterns | 8 | `core/07` · OS-001…008 |
| Structural formatting | 20 | `core/08` · STRUCT-001…020 |
| Semantic coherence | 21 | `core/09` · SEM-001…021 |
| Reference deep patterns | 8+ | `reference/ai_detection_patterns.json` |

Full map: [[moc-Core Signals]]

## Recognition procedure

1. **Surface scan (cheap):** regex/lexicon — delve, em-dash, transitions, emoji bullets, formulaic openers.
2. **Structural scan:** paragraph CV, bullet counts, markdown overstructuring.
3. **Statistical scan (if model available):** PPL, burstiness, ranks, Binoculars, Fast-DetectGPT.
4. **Semantic scan:** citation check (Crossref), personal voice, hedging density, hallucination heuristics.
5. **Watermark scan (if applicable):** recompute green lists + z-score.
6. **Attack / evasion patterns:** paraphrase dilution, homoglyph, typos, copy-paste mix (KGW-014…016).

## High-value patterns (priority match)

From taxonomy `most_robust` + practical gaps:

| Priority | Pattern | Why |
|----------|---------|-----|
| P0 | Fabricated citations (SEM-002, CD-021) | Strong content signal |
| P0 | Watermark z>4 (if present) | Theoretical footing |
| P1 | Binoculars (STAT-010) | High reported robustness |
| P1 | Fast-DetectGPT (STAT-006) | Curvature, practical |
| P1 | Style shift (mixed) | Real-world mixed texts |
| P2 | TTR / lexical richness | Cheap ensemble member |
| P3 | Em dash / delve family | Easy evade; half-life short |

## Output

```yaml
patterns_fired:
  - id: LM-001
    strength: high|med|low
    evidence: "..."
    half_life_risk: high
negatives_checked:
  - personal_voice_present: true
  - natural_typos: false
```

Handoff → [[fn-Relation Recognition]], [[fn-Inference]].

## Links

- Catalog: [[moc-Core Signals]], [[moc-Taxonomy]]
- Related: [[fn-Perception]], [[fn-Relation Recognition]]
- Hub: [[00_FULL_BRAIN]]
