---
tags: [brain, function, linking]
aliases: [Linking, fn-Linking, الربط]
type: cognitive-function
function_id: 03
---

# fn-Linking — Connect knowledge and cases

**Role:** Build the associative fabric of the vault (wikilinks, tags, matrices).

## Link types

| Relation | Example | How encoded |
|----------|---------|-------------|
| `implements` | Binoculars implements Cross-PPL | signal ↔ method |
| `uses_signal` | GPTZero uses PPL + burstiness | detector ↔ pattern |
| `limited_by` | PPL limited_by non-native FP | pattern ↔ gap |
| `stronger_than` | External evidence stronger_than internal | gap-05 doctrine |
| `attacks` | Paraphrase attacks KGW | attack ↔ watermark |
| `same_as` | STAT-006 ≈ BB-004 Fast-DetectGPT | cross-file IDs |
| `requires` | White-box requires logits | method ↔ precondition |
| `half_life` | delve marker → obsolescence | pattern ↔ gap-08 |

## Master cross-reference (from taxonomy)

**Most robust:** Low PPL · Binoculars · Fast-DetectGPT · TTR  
**Easiest to evade:** Em dash · Vocab blacklist · Flawless grammar  
**Strongest watermark:** KGW z>4 · SynthID Bayesian · Unigram fixed  
**Commercial stacks:** GPTZero=PPL+Burst+vocab · Turnitin=seg+RoBERTa · Originality=stylometric+transformer

## Linking protocol

1. When a new pattern is added → link to category MOC + related gaps.
2. When a case closes → link episode in [[memory-Episodic Log]] to patterns fired.
3. Maintain alias table for dual IDs (STAT-010 ↔ BB-006 ↔ OS-005 Binoculars).
4. Keep graph healthy: every Brain note must have ≥2 outgoing links.

## Alias map (critical duplicates)

| Concept | IDs / notes |
|---------|-------------|
| Fast-DetectGPT | STAT-006, BB-004, WB-009 · arXiv **2310.05130** |
| DetectGPT | STAT-005, BB-003, WB-008 · 2301.11305 |
| Binoculars | STAT-010, BB-006, WB-010, OS-005 |
| KGW z-score | KGW-004, WB-013, OS-006 |
| Em dash | LM-006, BB-021, STRUCT-010, CD-019 |
| Low TTR | LM-016, BB-013, CD-017 |
| Hallucinated citations | SEM-002, CD-021 |

## Links

- Knowledge: [[moc-Core Signals]], [[moc-Gaps]], [[moc-Reference]], [[moc-Taxonomy]]
- Downstream: [[fn-Relation Recognition]], [[fn-Context Building]]
- Hub: [[00_FULL_BRAIN]]
