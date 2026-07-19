---
tags: [brain, function, memory]
aliases: [Memory Administration, fn-Memory Administration, إدارة الذاكرة]
type: cognitive-function
function_id: 05
---

# fn-Memory Administration — Store, retrieve, forget

**Role:** Manage three memory stores so the brain does not rely on a single pass.

## Memory hierarchy

| Store | File | Contents | Retention |
|-------|------|----------|-----------|
| Working | [[memory-Working Memory]] | Active case: text meta, scores, open questions | Session / until case close |
| Episodic | [[memory-Episodic Log]] | Closed cases, outcomes, errors | Permanent (append-only) |
| Long-term | [[memory-Long Term]] | Lessons, baselines, half-life notes, ensemble weights | Permanent + revision |

## Operations

### Encode
1. After [[fn-Perception]]: dump raw sensor bundle → Working.
2. After [[fn-Making Decision]]: summarize episode → Episodic.
3. After [[fn-Learning]]: promote stable rules → Long-term.

### Retrieve
- Before inference: load relevant Long-term (local FPR, language rules).
- On similar case: search Episodic by genre/language/signal pattern.

### Forget / decay
- Style markers past half-life → demote confidence ([[08_signal_obsolescence]]).
- Working cleared on case close (keep only pointer to episode).

### Student writing profiles (external memory)
Per [[05_external_evidence]]: store baseline samples, stylometric fingerprint, prior flags — never only raw detector scores.

## Integrity rules

- Never store uncalibrated commercial “99%” as ground truth ([[06_commercial_claims_critique]]).
- Tag memories with `language`, `date`, `model_generation` for obsolescence.

## Links

- Stores: [[memory-Working Memory]], [[memory-Episodic Log]], [[memory-Long Term]]
- Related: [[fn-Learning]], [[fn-Knowledge Administration]], [[fn-Watching]]
- Hub: [[00_FULL_BRAIN]]
