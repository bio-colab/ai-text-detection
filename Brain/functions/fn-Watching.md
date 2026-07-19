---
tags: [brain, function, watching]
aliases: [Watching, fn-Watching, المراقبة]
type: cognitive-function
function_id: 15
---

# fn-Watching — Continuous monitoring

**Role:** Observe environment and system health so the brain does not go stale.

## Watch surfaces

| Surface | What to watch | Cadence |
|---------|---------------|---------|
| arXiv | Detection, watermark, survey papers | Weekly/Monthly |
| HF models | New detectors, RAID leaderboard | Monthly |
| Commercial claims | Accuracy marketing vs critiques | On procurement / quarterly |
| Signal fashion | Overused AI words shifting | Quarterly |
| Local FPR | Non-native / Arabic samples | Per semester |
| Package health | Broken JSON, outdated arXiv IDs | On edit |
| Case queue | Open flags without human close | Continuous |
| Doctrine compliance | Punish-on-score alone incidents | Continuous |

Dashboard: [[watch-Dashboard]]

## Alert conditions

- `ALERT-JUSTICE`: disciplinary action without human review
- `ALERT-AR`: EN detector applied as sole AR evidence
- `ALERT-CAL`: scores treated as probabilities without calibration
- `ALERT-STALE`: no taxonomy update > 6 months
- `ALERT-FP`: cluster of non-native false positives
- `ALERT-DRIFT`: major LLM release without re-eval

## Watch → act

Watching does not decide; it opens tasks:
→ [[queue-Priorities]] + [[fn-Planning]] + [[fn-Learning]]

## Minimal watchlist (papers / methods)

- Kirchenbauer watermark 2301.10226
- DetectGPT 2301.11305
- Fast-DetectGPT **2310.05130**
- Binoculars 2401.12070
- Sadasivan impossibility 2303.11156
- Wu survey 2310.14724 / 2025 CL
- SynthID line
- RAID / MAGE / HC3 benchmarks

## Links

- Dashboard: [[watch-Dashboard]]
- Related: [[fn-Predicting]], [[fn-Learning]], [[fn-Knowledge Administration]]
- Hub: [[00_FULL_BRAIN]]
