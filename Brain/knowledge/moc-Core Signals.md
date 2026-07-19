---
tags: [brain, moc, signal, knowledge]
aliases: [Core Signals MOC, moc-Core Signals]
type: moc
---

# MOC — Core Signals (164 patterns)

Maps the engineering catalog (Agent A) after unified merge. Parent: [[00_FULL_BRAIN]] · [[moc-Taxonomy]]

## Categories

### 01 Linguistic markers (20)
**File:** `core/01_linguistic_markers.json`  
**Function:** [[fn-Pattern Recognition]]  
Highlights: Delve family · tapestry/realm · formulaic transitions · em dash · meta fillers · low TTR · perfect grammar  
**Limits:** Easy paraphrase evade · non-native formality collision → [[01_false_positives_non_native]] · short half-life → [[08_signal_obsolescence]]

### 02 Statistical signals (14)
**File:** `core/02_statistical_signals.json`  
Highlights: Low PPL · burstiness · DetectGPT · **Fast-DetectGPT (2310.05130)** · Binoculars · Min-K% · DNA-GPT · PHD · TOCSIN  
**Most robust cluster:** PPL (careful) · Binoculars · Fast-DetectGPT · TTR

### 03 Green-box watermark (19)
**File:** `core/03_green_box_watermark.json`  
Highlights: KGW partition · gamma/delta · z-score · SynthID · Unigram · attacks (paraphrase, copy-paste, homoglyph)  
**Note:** Green *planted* ≠ GLTR green *observed*

### 04 Black-box detection (21)
**File:** `core/04_black_box_detection.json`  
No source-model logits: surrogate PPL, Fast-DetectGPT, DNA-GPT, Binoculars, Ghostbuster, RoBERTa, stylometry proxies

### 05 White-box detection (19)
**File:** `core/05_white_box_detection.json`  
Needs logits: logP, LogRank, LRR, NPR, GLTR buckets, Min-K%++, watermark with key, BiScope

### 06 Commercial detectors (22 + tools)
**File:** `core/06_commercial_detectors.json`  
GPTZero · Turnitin · Originality · Copyleaks · Winston · ZeroGPT  
**Critique:** [[06_commercial_claims_critique]]

### 07 Open-source detectors (8)
**File:** `core/07_open_source_detectors.json`  
RoBERTa OpenAI detector · MAGE · HC3 · GLTR · Binoculars · DetectGPT · lm-watermarking · RAID · RADAR · ModernBERT

### 08 Structural formatting (20)
**File:** `core/08_structural_formatting_signals.json`  
Emoji bullets · tricolon · uniform paragraphs · markdown overstructure · bold:colon · symmetry · rhetorical QA

### 09 Semantic coherence (21)
**File:** `core/09_semantic_coherence_signals.json`  
Hallucination · fabricated citations · no personal experience · hedging · safe alignment · semantic loops · meta AI self-ref  
**Preferred under non-native / Arabic stress**

### 10 Master taxonomy + gaps index
**File:** `core/10_master_taxonomy.json`  
See [[moc-Taxonomy]] · gaps layer [[moc-Gaps]]

## Original engineering README
[[ORIGINAL_README_A]] — 164 patterns, multi-agent collection rules, best ensemble note

## How brain uses this MOC
- [[fn-Perception]] registers component outputs by category
- [[fn-Pattern Recognition]] matches IDs
- [[fn-Inference]] weights by robustness matrix
- [[fn-Knowledge Administration]] updates counts and half-life
