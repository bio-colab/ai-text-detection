---
tags: [brain, function, learning]
aliases: [Learning, fn-Learning, التعلم]
type: cognitive-function
function_id: 13
---

# fn-Learning — Improve from outcomes

**Role:** Close the loop from decisions and new research back into weights, rules, and corpus.

## Learning channels

| Channel | Input | Output |
|---------|-------|--------|
| Case feedback | True labels after oral/rewrite | Calibration points for fusion weights |
| Local audit | Iraqi/Arabic student sample tests | Local FPR/TPR tables |
| Literature | New arXiv / surveys | Pattern adds, demotions |
| Attack research | Humanizers, paraphrase rounds | Robustness notes |
| Commercial drift | Claim vs field performance | Trust scores |

## Learning procedures

### A. Online (per case)
1. After human final verdict, compare to fused score.
2. Record error type: FP non-native, FN paraphrased, mixed miss, short-text noise.
3. Append to [[memory-Episodic Log]].
4. If systematic, open task on [[queue-Priorities]].

### B. Offline (batch)
1. Re-estimate fusion weights (logistic on local features).
2. Recompute base rates for PPV.
3. Update Arabic corpus and retrain classifier ([[03_arabic_detection]] plan).
4. Demote obsolete markers ([[08_signal_obsolescence]]).

### C. Self-review loop (from taxonomy)
```
while coverage < 0.95:
  search(); classify(); review()
  if not covered: refine_query()
```

## What not to learn

- Do not “learn” that commercial 99.98% is truth.
- Do not fit detectors to punish non-native formality.
- Do not treat mixed-authorship mastery as pure AI guilt.

## Promotion path

Episodic insight → validated on ≥N cases → Long-term rule → Knowledge JSON/MOC update.

## Links

- Memory: [[fn-Memory Administration]], [[memory-Long Term]]
- Knowledge: [[fn-Knowledge Administration]]
- Watching: [[fn-Watching]]
- Hub: [[00_FULL_BRAIN]]
