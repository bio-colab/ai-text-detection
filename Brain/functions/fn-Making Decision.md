---
tags: [brain, function, decision]
aliases: [Making Decision, fn-Making Decision, اتخاذ القرار]
type: cognitive-function
function_id: 10
---

# fn-Making Decision — Verdict policy

**Role:** Convert beliefs into actions under ethical and institutional constraints.

## Decision space (academic integrity default)

| Decision | Meaning | When allowed |
|----------|---------|--------------|
| `clear` | No material AI concern | Low p_ai + coherent human signals + no external red flags |
| `flag_for_review` | Human review required | Medium score / mixed / high uncertainty |
| `request_evidence` | Ask version history / rewrite / oral | Any non-trivial flag |
| `support_concern` | Evidence supports AI assistance claim | High fused belief **and** external/oral corroboration |
| `insufficient` | Cannot decide fairly | AR without local tools / tiny text / missing sensors |

## Hard policy (non-negotiable)

1. **Never** `punish` or grade penalty on detector score alone.
2. **Always** Human-in-the-Loop for disciplinary action ([[protocol-Human Review]]).
3. Prefer **intent & mastery** (can student discuss?) over tool-use witch hunt ([[04_mixed_texts]]).
4. Apply **conservative thresholds** for non-native writers ([[01_false_positives_non_native]]).
5. Treat commercial 99% claims as untrusted until local validation ([[06_commercial_claims_critique]]).
6. Document uncertainty band in every decision record.

## Decision procedure

```
IF language == AR AND no_local_model:
    → insufficient | request_human_semantic_review
ELIF stakes == low AND p_ai < threshold_low:
    → clear
ELIF uncertainty == high OR non_native OR length_short:
    → flag_for_review + request_evidence
ELIF external_evidence_strong AND inference_high:
    → support_concern (still with oral option)
ELSE:
    → flag_for_review
```

## Decision record schema

```yaml
decision:
  case_id: ""
  outcome: flag_for_review
  rationale: []
  signals_used: []
  signals_discounted: []
  human_reviewer: null
  appeal_path: true
  timestamp: ""
```

Log to [[memory-Episodic Log]]. Feed outcome labels to [[fn-Learning]].

## Links

- Upstream: [[fn-Inference]], [[fn-Context Building]]
- Protocol: [[protocol-Human Review]]
- Hub: [[00_FULL_BRAIN]]
