---
tags: [brain, function, relations]
aliases: [Relation Recognition, fn-Relation Recognition, التعرف على العلاقات]
type: cognitive-function
function_id: 08
---

# fn-Relation Recognition — Map relations between entities

**Role:** Detect *relationships* (not only isolated patterns): between signals, between text segments, between actors and tools.

## Relation classes in this domain

### A. Signal–signal relations
- **Correlated** — Low PPL ↔ High green GLTR rank (same predictability root)
- **Complementary** — Statistical + Semantic (different failure modes)
- **Redundant** — STAT-001 Low PPL ≈ BB-001 Low PPL Proxy
- **Antagonistic** — High personal voice vs high formulaic structure → mixed-text hypothesis

### B. Method–access relations
| Access | Methods |
|--------|---------|
| Black-box | Surrogate PPL, Fast-DetectGPT proxy, RoBERTa, Ghostbuster |
| White-box | LogRank, LRR, Min-K%, true curvature |
| Green-box | KGW, Unigram, SynthID (key/scheme) |
| External | Version history, stylometric profile, oral |

### C. Segment–segment relations (mixed texts)
- Sudden style shift between paragraphs → human edit of AI draft ([[04_mixed_texts]])
- Semantic loops in middle + idiosyncratic intro → hybrid authorship

### D. Population relations
- Non-native formality ≈ AI formality → false alliance (spurious correlation) → [[01_false_positives_non_native]]
- Model distribution → human distribution convergence → detection collapse → [[02_impossibility_theorem]]

### E. Temporal relations
- Signal strength over time (half-life) → [[08_signal_obsolescence]]
- Detector trained on GPT-3.5 vs tested on 2026 models → domain shift

### F. Institutional relations
- Detector score ↛ academic verdict (must pass human protocol)
- Commercial marketing ↛ independent truth

## Relation recognition checklist

```yaml
relations:
  fired_clusters: []      # groups of redundant hits
  contradictions: []
  segment_shifts: []
  access_level: black|white|green|external_mix
  spurious_risks: [non_native_formality, short_text_noise]
  causal_vs_correlational: "document"
```

## Graph edges to maintain in Obsidian

Every relation note or case should create links of type:
`[[pattern A]] --supports--> [[hypothesis]]`  
`[[gap X]] --limits--> [[pattern A]]`

Use [[fn-Linking]] for persistent wiki structure.

## Links

- Upstream: [[fn-Pattern Recognition]], [[fn-Linking]]
- Downstream: [[fn-Inference]], [[fn-Context Building]]
- Hub: [[00_FULL_BRAIN]]
