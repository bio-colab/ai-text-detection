---
tags: [brain, moc, taxonomy, knowledge]
aliases: [Taxonomy MOC, moc-Taxonomy]
type: moc
---

# MOC — Master Taxonomy

Source: `core/10_master_taxonomy.json` · Version **1.1-unified** · 2026-07-18

## Meta
- Language focus: English (with AR warnings)
- Patterns aggregated: **164** · unique names: **153** (9 patterns legitimately appear in more than one methodological layer — see `cross_file_duplicates` in core/10)
- Gaps filled: **8**
- Merge: Engineering catalog (A) + Analytical brief (B)
- Method: Multi-agent parallel research + self-review loop

## Taxonomy branches

| Key | File | Count | Type |
|-----|------|------:|------|
| 01_linguistic_markers | 01_…json | 20 | علامات |
| 02_statistical_signals | 02_…json | 14 | statistical |
| 03_green_box_watermark | 03_…json | 19 | green box |
| 04_black_box_detection | 04_…json | 21 | black box |
| 05_white_box_detection | 05_…json | 19 | white box |
| 06_commercial_detectors | 06_…json | 22 | commercial |
| 07_open_source_detectors | 07_…json | 8 | open source |
| 08_structural_formatting | 08_…json | 20 | formatting |
| 09_semantic_coherence | 09_…json | 21 | semantic |
| 10_gaps_and_limitations | gaps/*.md | 8 | conceptual_limitations |

Detail MOC: [[moc-Core Signals]] · [[moc-Gaps]]

## Cross-reference matrix

### Most robust
- Low Perplexity
- Binoculars Ratio
- Fast-DetectGPT Curvature
- Lexical Richness TTR

### Easiest to evade
- Em dash (remove)
- Vocab blacklist (paraphrase)
- Flawless grammar (add typos)

### Strongest watermark
- KGW z-score > 4
- SynthID Bayesian
- Unigram Fixed

### Commercial stack sketch
- GPTZero = PPL + Burstiness + vocab + 7-comp
- Turnitin = segmentation + RoBERTa + pronoun + fake citation
- Originality = stylometric + transformer

## Self-review mechanism
`Search → Classify → Count → Review → refine if coverage < 95%`  
Validation: id, name, detection, examples, sources, confidence  
Anti-stop: pattern counter & source-type checklist

Administered by [[fn-Knowledge Administration]] · [[fn-Learning]]
