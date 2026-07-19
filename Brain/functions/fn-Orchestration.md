---
tags: [brain, function, orchestration]
aliases: [Orchestration, fn-Orchestration, التنسيق]
type: cognitive-function
function_id: 16
---

# fn-Orchestration — Conduct the full brain

**Role:** Sequence, parallelize, and gate all cognitive functions. Single entry for operators.

## Master control loop

```
┌──────────────────────────────────────────────────────────┐
│ 0. WATCH (background) ──alerts──► PRIORITY + PLANNING     │
└──────────────────────────────────────────────────────────┘
CASE START
  1. PERCEPTION          ← accept all components
  2. CONTEXT BUILDING    ← language, length, stakes, sensors
  3. PATTERN RECOGNITION ← match libraries (parallel by family)
  4. RELATION RECOGNITION← clusters, shifts, contradictions
  5. UNDERSTANDING       ← meanings + failure modes
  6. LINKING             ← attach vault knowledge to case
  7. MEMORY retrieve     ← long-term rules + similar episodes
  8. INFERENCE           ← fuse + calibrate + uncertainty
  9. PREDICTING          ← PPV, FP risk, mixed likelihood
 10. MAKING DECISION     ← policy-constrained outcome
 11. MEMORY encode       ← working → episodic
 12. LEARNING            ← if label available
 13. KNOWLEDGE ADMIN     ← if taxonomy change needed
 14. PRIORITY ADMIN      ← refresh queue
CASE END
  background: WATCH continues
```

## Parallelization map

| Parallel group | Functions |
|----------------|-----------|
| G1 Sensors | Pattern families (ling/stat/struct/sem/wm) |
| G2 Structure | Linking + Relation + Understanding |
| G3 Judgment | Inference + Predicting |
| Serial gates | Context before Inference; Decision after Inference; Learning after Decision |

## Pipeline binding

Primary executable path: [[pipeline-Detect Text Cycle]]

Supporting protocols:
- [[protocol-Signal Fusion]]
- [[protocol-Human Review]]

## Orchestrator checklist (operator)

- [ ] Open [[memory-Working Memory]] and clear previous case
- [ ] Fill context card
- [ ] Run sensors / paste component outputs
- [ ] Fire patterns + note relations
- [ ] Fuse with doctrine discounts
- [ ] Decide under policy
- [ ] Log episode
- [ ] Update priorities if systemic issue
- [ ] Check [[watch-Dashboard]] weekly

## Failure modes of orchestration

| Failure | Symptom | Fix |
|---------|---------|-----|
| Skip context | EN scores on AR | Force language gate |
| Skip human | Auto-punish | Policy hard-stop |
| Skip external | Overtrust internal | Request evidence step |
| Skip learning | Repeat FP | Mandatory postmortem |
| Skip watching | Stale signals | 6-month refresh alarm |

## Links

- Hub: [[00_FULL_BRAIN]]
- All functions: [[fn-Perception]] … [[fn-Watching]]
- HOME: [[HOME]]
