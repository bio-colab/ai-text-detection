# -*- coding: utf-8 -*-
"""
mijhar.report — assembles the evidence report and enforces the doctrine.

The doctrine below is not a disclaimer bolted on at the end; it is the
product. mijhar is a microscope (مِجْهَر), not a judge: it collects
observable evidence and hands it to a human. It never outputs P(AI),
never outputs a verdict, and refuses to pretend otherwise.
"""

from __future__ import annotations

import json
from datetime import date

from .signals import ALL_SIGNALS, build_context

TOOL_NAME = "mijhar"
TOOL_VERSION = "3.1.0"

DOCTRINE = {
    "verdict": "NONE — this tool never decides authorship.",
    "what_this_is": (
        "A deterministic evidence collector. Each fired signal is a stylistic "
        "observation with an excerpt a human can verify, bound to a documented "
        "pattern in the corpus (core/*.json)."
    ),
    "what_this_is_not": (
        "Not a probability of AI authorship. Signal weights are editorial "
        "priors, not calibrated probabilities; do not sum, multiply, or "
        "threshold them (see gaps/07)."
    ),
    "false_positive_warning": (
        "Detectors of this family show severely elevated false-positive rates "
        "on non-native English writers: Liang et al. (arXiv:2304.02819, "
        "Patterns 2023) measured an average 61.22% FPR on human-written TOEFL "
        "essays. If the author may be a non-native writer, discount stylistic "
        "signals accordingly (gaps/01)."
    ),
    "arabic_warning": (
        "Arabic support is EXPERIMENTAL. Most English-calibrated signals do "
        "not transfer; only language-agnostic and Arabic-lexicon signals ran, "
        "and they are unvalidated against a labeled Arabic corpus (gaps/03)."
    ),
    "short_text_warning": (
        "Below ~150 words most signals are noise; below ~300 words statistical "
        "proxies are unreliable and were skipped (text_length_sensitivity)."
    ),
    "impossibility_note": (
        "Reliable detection may be theoretically bounded as models approach "
        "the human text distribution (Sadasivan et al., arXiv:2303.11156). "
        "Absence of signals proves nothing."
    ),
    "required_process": (
        "Human-in-the-loop review is mandatory before any consequence. "
        "Prefer out-of-text evidence: version history, drafts, an oral "
        "defense, a writing baseline (gaps/05). Never punish on a score."
    ),
    "decay_note": (
        "Stylistic lexicons decay as models are retrained; treat "
        "estimated_half_life_months in the corpus seriously (gaps/08)."
    ),
}


def scan_text(text: str) -> dict:
    ctx = build_context(text)
    lang = ctx["lang"]
    n_words = len(ctx["words"])

    results = []
    skipped = []
    for fn in ALL_SIGNALS:
        r = fn(text, ctx)
        applicable = (r.languages == "any" or r.languages == lang
                      or (lang == "mixed"))
        if not applicable:
            skipped.append({"signal_id": r.signal_id, "name": r.name,
                            "reason": f"language mismatch (text={lang}, "
                                      f"signal={r.languages})"})
            continue
        results.append(r)

    fired = [r for r in results if r.fired]
    not_evaluated = [r for r in results if r.value == -1.0]

    warnings = []
    if n_words < 150:
        warnings.append(DOCTRINE["short_text_warning"])
    if lang in ("ar", "mixed"):
        warnings.append(DOCTRINE["arabic_warning"])
    warnings.append(DOCTRINE["false_positive_warning"])

    report = {
        "tool": TOOL_NAME,
        "version": TOOL_VERSION,
        "date": str(date.today()),
        "doctrine": DOCTRINE,
        "input_stats": {
            "language": lang,
            "words": n_words,
            "sentences": len(ctx["sents"]),
            "paragraphs": len(ctx["paras"]),
        },
        "active_warnings": warnings,
        "summary": {
            "signals_evaluated": len(results),
            "signals_fired": len(fired),
            "signals_not_evaluated_short_text": len(not_evaluated),
            "signals_skipped_language": len(skipped),
            "reading": _reading(len(fired), len(results), n_words, lang),
        },
        "fired_signals": [r.to_dict() for r in
                          sorted(fired, key=lambda r: -r.weight)],
        "quiet_signals": [{"signal_id": r.signal_id, "name": r.name,
                           "value": r.value,
                           "threshold_note": r.threshold_note}
                          for r in results if not r.fired],
        "skipped_signals": skipped,
    }
    return report


def _reading(n_fired: int, n_eval: int, n_words: int, lang: str) -> str:
    """A qualitative sentence for humans. Deliberately NOT a score."""
    if n_words < 150:
        return ("Text too short for meaningful stylistic evidence. "
                "Do not draw conclusions.")
    if n_fired == 0:
        return ("No stylistic signals fired. This is NOT evidence of human "
                "authorship (evasion is easy; see impossibility_note).")
    if n_fired <= 2:
        return ("A few isolated signals fired. Individually these mean "
                "little; review the excerpts and seek out-of-text evidence.")
    return ("Multiple signals fired. Review each excerpt, then seek "
            "out-of-text evidence (drafts, version history, oral defense). "
            "Do not act on this report alone" +
            ("; Arabic results are experimental." if lang != "en" else "."))


def to_json(report: dict, indent: int = 2) -> str:
    return json.dumps(report, ensure_ascii=False, indent=indent)


def to_human(report: dict) -> str:
    lines = []
    s = report["summary"]
    st = report["input_stats"]
    lines.append(f"مِجْهَر mijhar v{report['version']} — evidence report "
                 f"({report['date']})")
    lines.append(f"language={st['language']}  words={st['words']}  "
                 f"sentences={st['sentences']}")
    lines.append("-" * 70)
    lines.append(f"evaluated {s['signals_evaluated']} signals | "
                 f"fired {s['signals_fired']} | "
                 f"short-text skips {s['signals_not_evaluated_short_text']} | "
                 f"language skips {s['signals_skipped_language']}")
    lines.append("")
    for r in report["fired_signals"]:
        lines.append(f"[{r['signal_id']}] {r['name']}  "
                     f"(value={r['value']}, {r['threshold_note']}; "
                     f"corpus: {r['corpus_ref']})")
        for e in r["evidence"][:3]:
            lines.append(f"    · {e['excerpt']}"
                         + (f"  [{e['detail']}]" if e.get("detail") else ""))
        if r.get("caveat"):
            lines.append(f"    ⚠ {r['caveat']}")
    lines.append("")
    lines.append("READING: " + s["reading"])
    lines.append("")
    for w in report["active_warnings"]:
        lines.append("⚠ " + w)
    lines.append("")
    lines.append("DOCTRINE: no verdict, no P(AI), human review mandatory, "
                 "never punish on a score.")
    return "\n".join(lines)
