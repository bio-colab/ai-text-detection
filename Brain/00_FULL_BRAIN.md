---
tags: [brain, hub, orchestration, system]
aliases: [Full Brain, Cognitive Brain, العقل الكامل]
type: brain-hub
version: 1.0
date: 2026-07-18
domain: AI Text Detection Unified v1.1
---

# 🧠 FULL BRAIN — Cognitive Operating System

> **Domain brain** for [[README|AI Text Detection Unified v1.1]].  
> Connects every signal, gap, detector, and paper into a living cognitive loop: **sense → understand → link → decide → learn → watch**.

```
                    ┌─────────────────────┐
                    │   [[fn-Orchestration]]  │
                    │   (conductor)           │
                    └──────────┬──────────────┘
         ┌─────────────────────┼─────────────────────┐
         ▼                     ▼                     ▼
  [[fn-Perception]]    [[fn-Understanding]]    [[fn-Watching]]
         │                     │                     │
         ▼                     ▼                     ▼
  [[fn-Pattern Recognition]] [[fn-Linking]]   [[fn-Predicting]]
         │                     │                     │
         ▼                     ▼                     ▼
  [[fn-Relation Recognition]] [[fn-Context Building]] [[fn-Learning]]
         │                     │                     │
         └──────────┬──────────┴──────────┬──────────┘
                    ▼                     ▼
           [[fn-Inference]]      [[fn-Memory Administration]]
                    │                     │
                    ▼                     ▼
         [[fn-Making Decision]]  [[fn-Knowledge Administration]]
                    │                     │
                    ▼                     ▼
           [[fn-Planning]]       [[fn-Priority Administration]]
                    └──────────┬──────────┘
                               ▼
                    [[pipeline-Detect Text Cycle]]
```

---

## How to use this brain

1. **Open graph view** (Ctrl/Cmd+G) — filter tag `#brain` or path `Brain/`.
2. Start a case from [[pipeline-Detect Text Cycle]].
3. Let [[fn-Orchestration]] call functions in order (see protocol).
4. Write outcomes into [[memory-Working Memory]] then promote to [[memory-Long Term]].
5. Update priorities via [[fn-Priority Administration]] and knowledge via [[fn-Knowledge Administration]].

---

## Cognitive functions (16)

| # | Function | Role in this vault | Entry |
|---|----------|--------------------|-------|
| 1 | Perception | Ingest text + all component outputs | [[fn-Perception]] |
| 2 | Understanding | Interpret signals, claims, limits | [[fn-Understanding]] |
| 3 | Linking | Wikilinks, cross-refs, graph edges | [[fn-Linking]] |
| 4 | Context building | Case context, domain, language, length | [[fn-Context Building]] |
| 5 | Memory administration | Working / episodic / long-term stores | [[fn-Memory Administration]] |
| 6 | Inference | Bayesian fusion, score → belief | [[fn-Inference]] |
| 7 | Pattern recognition | Match 153 unique patterns (164 aggregated) from core | [[fn-Pattern Recognition]] |
| 8 | Relation recognition | Robust ↔ fragile, EN ↔ AR, internal ↔ external | [[fn-Relation Recognition]] |
| 9 | Planning | Investigation & research plans | [[fn-Planning]] |
| 10 | Making decision | Human-in-loop verdict policy | [[fn-Making Decision]] |
| 11 | Priority administration | Gap & signal priority queues | [[fn-Priority Administration]] |
| 12 | Knowledge administration | Taxonomy, CRUD, half-life | [[fn-Knowledge Administration]] |
| 13 | Learning | Feedback loops, corpus updates | [[fn-Learning]] |
| 14 | Predicting | Obsolescence, FP risk, model drift | [[fn-Predicting]] |
| 15 | Watching | Monitors, arXiv, signal half-life | [[fn-Watching]] |
| 16 | Orchestration | Routes all of the above | [[fn-Orchestration]] |

---

## Knowledge cortex (vault map)

### Core signals (153 unique patterns, 164 aggregated)
- [[moc-Core Signals]]
- Source files: `core/01` … `core/10` + [[ORIGINAL_README_A]]

### Critical gaps (8)
- [[moc-Gaps]]
- Highest priority: [[03_arabic_detection]] → [[01_false_positives_non_native]] → [[05_external_evidence]]

### Reference cortex
- [[moc-Reference]]
- Patterns, papers, tools, watermarks, comparison report

### Master taxonomy
- [[moc-Taxonomy]] ← `core/10_master_taxonomy.json`

---

## Decision doctrine (always on)

From gaps + README critical warnings:

1. **No 100% detector** — arms race ([[02_impossibility_theorem]]).
2. **Never punish on detector alone** — [[01_false_positives_non_native]] + Human-in-the-Loop.
3. **Arabic ≠ English pipeline** — [[03_arabic_detection]].
4. **Mixed text is the default case** — [[04_mixed_texts]].
5. **External evidence > pure text signals** — [[05_external_evidence]].
6. **Commercial claims need local audit** — [[06_commercial_claims_critique]].
7. **Calibrate + fuse + respect length** — [[07_calibration_fusion_length]].
8. **Signals expire** — [[08_signal_obsolescence]].

---

## Best ensemble (from master taxonomy)

Most robust stack:

1. Low Perplexity (with caution on non-native)
2. Binoculars Ratio
3. Fast-DetectGPT Curvature
4. Lexical Richness TTR
5. **Plus** external evidence + oral defense

Recommended open ensemble: **Binoculars + Fast-DetectGPT + TTR + z-score (if watermark) + human review**.

---

## Active system files

| Path | Purpose |
|------|---------|
| [[pipeline-Detect Text Cycle]] | End-to-end detection workflow |
| [[protocol-Signal Fusion]] | How to merge multi-layer scores |
| [[protocol-Human Review]] | Academic integrity decision rules |
| [[memory-Working Memory]] | Current case scratchpad |
| [[memory-Episodic Log]] | Case history |
| [[memory-Long Term]] | Stable lessons & baselines |
| [[queue-Priorities]] | What to do next |
| [[watch-Dashboard]] | What the brain monitors |
| [[HOME]] | Vault home / dashboard |

---

## Graph tips

- Tags: `#brain` `#signal` `#gap` `#detector` `#protocol` `#memory` `#priority-critical`
- Use **Local Graph** on this note to see the full cognitive mesh.
- Canvas: open [[Brain Canvas]] for the visual system map.

---

## Self-review loop (brain metabolism)

From `10_master_taxonomy` self_review_mechanism:

```
Search → Classify → Count → Review
  (هل غطيت كل الجوانب؟ هل أتممت كل المهام؟ هل صنفتها بشكل صحيح؟)
  → If coverage < 95% → refine → loop
```

Mapped functions: [[fn-Watching]] + [[fn-Learning]] + [[fn-Knowledge Administration]] + [[fn-Orchestration]].

---

*Brain version 1.0 — built over every file in core/, gaps/, reference/, README. Living system: re-read sources every 6 months.*
