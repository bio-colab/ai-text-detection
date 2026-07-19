---
tags: [brain, pipeline, protocol]
aliases: [Detect Text Cycle, pipeline-Detect Text Cycle]
type: pipeline
---

# Pipeline — Detect Text Cycle

Executable path for [[fn-Orchestration]]. Use with [[memory-Working Memory]].

## Phase 0 — Intake
1. Create case id: `CASE-YYYYMMDD-##`
2. Paste or link text; record word count, language hypothesis, genre, stakes.
3. Clear previous working memory.

## Phase 1 — Context gate
Run [[fn-Context Building]]:
- If **Arabic** → open [[03_arabic_detection]]; mark EN statistical sensors untrusted.
- If **short (<250–300w)** → mark stats unreliable ([[07_calibration_fusion_length]]).
- If **non-native possible** → raise FP prior ([[01_false_positives_non_native]]).
- If **high stakes** → human review mandatory.

## Phase 2 — Multi-sensor perception
[[fn-Perception]] collects:
- [ ] Linguistic (core/01)
- [ ] Statistical (core/02) if length & language OK
- [ ] Structural (core/08)
- [ ] Semantic (core/09) — always valuable
- [ ] Watermark (core/03) if scheme known
- [ ] Black/white box tools available (core/04–05, 07)
- [ ] Commercial (core/06) as weak signals only
- [ ] External: version history / metadata / baseline ([[05_external_evidence]])

## Phase 3 — Recognize
- [[fn-Pattern Recognition]] → list fired IDs
- [[fn-Relation Recognition]] → clusters, contradictions, segment shifts
- If mixed suspected → **segment-level** rescoring ([[04_mixed_texts]])

## Phase 4 — Understand & link
- [[fn-Understanding]] narrative + failure modes
- [[fn-Linking]] attach taxonomy + gap doctrine
- [[fn-Memory Administration]] retrieve long-term rules

## Phase 5 — Infer & predict
- [[protocol-Signal Fusion]]
- [[fn-Inference]] belief state + uncertainty
- [[fn-Predicting]] PPV / FP risk / obsolescence caveats

## Phase 6 — Decide
- [[fn-Making Decision]] + [[protocol-Human Review]]
- Outcomes: `clear` | `flag_for_review` | `request_evidence` | `support_concern` | `insufficient`
- **Forbidden:** punish on score alone

## Phase 7 — Encode & learn
- Write episode → [[memory-Episodic Log]]
- If ground truth later → [[fn-Learning]]
- Update [[queue-Priorities]] if systemic

## Phase 8 — Background
- [[fn-Watching]] continues on [[watch-Dashboard]]

---

## Quick path (low stakes, EN, long text)
Context → cheap linguistic/structural → Binoculars + Fast-DetectGPT + TTR → fuse → if medium+ flag human → log

## Arabic path
Context(AR) → semantic + optional local classifier → external/oral → **never** sole EN commercial verdict → log `insufficient` if only EN tools
