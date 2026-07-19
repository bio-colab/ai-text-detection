# -*- coding: utf-8 -*-
"""
mijhar.signals — deterministic signal implementations.

Every signal is bound to a pattern ID in core/*.json (the knowledge base is
the source of truth; this module makes a machine-checkable subset of it
executable). Signals return *evidence*, never verdicts.

Design rules (non-negotiable, see doctrine in mijhar.report):
  * stdlib only — zero external dependencies, fully reproducible.
  * Every hit carries an excerpt so a human reviewer can verify it.
  * `weight` is an editorial prior copied from the corpus `confidence`
    field. It is NOT a calibrated probability and is never summed into
    a probability by this package.
  * Signals declare `languages`: "en", "ar", or "any" (language-agnostic).
"""

from __future__ import annotations

import math
import re
import statistics
import unicodedata
from dataclasses import dataclass, field, asdict

# --------------------------------------------------------------------------
# Lexicons (English) — sources: core/01_linguistic_markers.json examples,
# Juzek & Ward 2024 (arXiv:2412.11385) focal words, and widely replicated
# community lists. Editorial; expected to decay (see gaps/08).
# --------------------------------------------------------------------------

FOCAL_WORDS_EN = {
    # arXiv:2412.11385 focal-word style lexicon (subset) + core/01 LM-001/002/003/007
    "delve", "delves", "delved", "delving",
    "intricate", "intricacies", "intricately",
    "underscore", "underscores", "underscored", "underscoring",
    "tapestry", "realm", "realms", "landscape", "landscapes", "mosaic",
    "pivotal", "crucial", "groundbreaking", "multifaceted", "nuanced",
    "showcase", "showcases", "showcasing", "showcased",
    "meticulous", "meticulously", "seamless", "seamlessly",
    "leverage", "leverages", "leveraging", "leveraged",
    "foster", "fosters", "fostering", "garner", "garners",
    "boast", "boasts", "boasting", "commendable", "noteworthy",
    "vibrant", "bustling", "testament", "beacon", "paramount",
    "elevate", "elevates", "holistic", "robustness", "synergy",
}

META_FILLER_EN = [
    "it is important to note that", "it's important to note that",
    "it is worth noting that", "it's worth noting that",
    "it should be noted that", "needless to say",
    "at the end of the day", "when it comes to",
    "in the ever-evolving", "in the rapidly evolving",
]

CLICHE_OPENERS_EN = [
    "in today's fast-paced world", "in today's digital age",
    "in the modern era", "in an era of", "in recent years,",
    "since the dawn of", "throughout history,",
    "in the ever-changing landscape",
]

CLICHE_CLOSERS_EN = [
    "in conclusion,", "in summary,", "to sum up,", "ultimately,",
    "overall,", "the possibilities are endless",
    "as we move forward", "the future looks bright",
]

AI_SELF_DISCLOSURE_EN = [
    "as an ai language model", "as a large language model",
    "as an ai assistant", "i don't have personal opinions",
    "i cannot browse the internet", "my training data",
    "i'm just an ai", "as of my last knowledge update",
    "knowledge cutoff",
]

HEDGES_EN = [
    "potentially", "arguably", "generally speaking", "in many cases",
    "it could be argued", "to some extent", "more often than not",
    "may well", "might well",
]

TRANSITIONS_EN = [
    "moreover", "furthermore", "additionally", "consequently",
    "nevertheless", "nonetheless", "in addition", "on the other hand",
    "as a result", "in essence", "notably", "importantly",
]

SYCOPHANCY_OPENERS_EN = [
    "great question", "certainly!", "absolutely!", "of course!",
    "i'd be happy to", "what a fascinating",
]

# --------------------------------------------------------------------------
# Arabic lexicons — EXPERIMENTAL (gaps/03 applies in full). These are
# editorial observations of common LLM Arabic register, not validated
# against a labeled Arabic corpus. High decay expected.
# --------------------------------------------------------------------------

AI_SELF_DISCLOSURE_AR = [
    "بصفتي نموذج ذكاء اصطناعي", "بصفتي نموذج لغة",
    "كنموذج ذكاء اصطناعي", "لا أستطيع تصفح الإنترنت",
    "بيانات تدريبي", "حتى تاريخ معرفتي",
]

META_FILLER_AR = [
    "من الجدير بالذكر", "تجدر الإشارة إلى", "لا يخفى على أحد",
    "مما لا شك فيه", "وفي هذا الصدد", "علاوة على ذلك",
    "بالإضافة إلى ذلك", "ومن ناحية أخرى",
]

CLICHE_CLOSERS_AR = [
    "في الختام", "خلاصة القول", "وختاماً", "ومجمل القول",
    "وفي نهاية المطاف",
]

# --------------------------------------------------------------------------
# Data model
# --------------------------------------------------------------------------

@dataclass
class Evidence:
    excerpt: str
    position: int = -1
    detail: str = ""


@dataclass
class SignalResult:
    signal_id: str          # mijhar signal id
    corpus_ref: str         # pattern id(s) in core/*.json
    name: str
    languages: str          # "en" | "ar" | "any"
    fired: bool
    value: float            # measured quantity (rate, ratio, count…)
    threshold_note: str     # human-readable threshold description
    weight: float           # editorial prior from corpus confidence — NOT P(AI)
    evidence: list = field(default_factory=list)
    caveat: str = ""

    def to_dict(self):
        d = asdict(self)
        d["evidence"] = [asdict(e) if isinstance(e, Evidence) else e
                         for e in self.evidence]
        return d


# --------------------------------------------------------------------------
# Text utilities (language-aware, stdlib only)
# --------------------------------------------------------------------------

_AR_RE = re.compile(r"[\u0600-\u06FF]")
_WORD_RE = re.compile(r"[\w\u0600-\u06FF']+", re.UNICODE)
_SENT_SPLIT_RE = re.compile(r"(?<=[.!?؟…])\s+|\n{2,}")


def detect_language(text: str) -> str:
    """Crude but deterministic: ratio of Arabic-block letters."""
    letters = [c for c in text if c.isalpha()]
    if not letters:
        return "unknown"
    ar = sum(1 for c in letters if _AR_RE.match(c))
    ratio = ar / len(letters)
    if ratio > 0.5:
        return "ar"
    if ratio < 0.1:
        return "en"
    return "mixed"


def words(text: str):
    return _WORD_RE.findall(text.lower())


def sentences(text: str):
    parts = [s.strip() for s in _SENT_SPLIT_RE.split(text) if s.strip()]
    return [s for s in parts if len(_WORD_RE.findall(s)) >= 2]


def paragraphs(text: str):
    return [p.strip() for p in re.split(r"\n{2,}", text) if p.strip()]


def _excerpt(text: str, pos: int, width: int = 60) -> str:
    a = max(0, pos - width // 2)
    b = min(len(text), pos + width)
    return ("…" if a > 0 else "") + text[a:b].replace("\n", " ") + ("…" if b < len(text) else "")


def _phrase_hits(text_lower: str, text: str, phrases, limit=5):
    hits = []
    for ph in phrases:
        start = 0
        while True:
            i = text_lower.find(ph, start)
            if i < 0:
                break
            hits.append(Evidence(excerpt=_excerpt(text, i), position=i, detail=ph))
            start = i + len(ph)
            if len(hits) >= limit * 3:
                break
    return hits


# --------------------------------------------------------------------------
# Signals
# --------------------------------------------------------------------------

def sig_focal_words(text, ctx):
    ws = ctx["words"]
    n = max(1, len(ws))
    hits, seen = [], {}
    lower = ctx["lower"]
    for w in set(ws) & FOCAL_WORDS_EN:
        c = ws.count(w)
        seen[w] = c
        i = lower.find(w)
        if i >= 0:
            hits.append(Evidence(excerpt=_excerpt(text, i), position=i,
                                 detail=f"{w} ×{c}"))
    rate = sum(seen.values()) / n * 1000
    return SignalResult(
        "MJ-EN-01", "LM-001,LM-002,LM-003,LM-007", "Focal-word density",
        "en", fired=rate >= 8.0, value=round(rate, 2),
        threshold_note="≥8 focal words per 1000 words (editorial)",
        weight=0.9, evidence=hits[:8],
        caveat="Lexicon decays as models are re-tuned (gaps/08). Formal human "
               "academic prose also uses these words.")


def sig_ai_self_disclosure(text, ctx):
    phr = AI_SELF_DISCLOSURE_EN if ctx["lang"] != "ar" else AI_SELF_DISCLOSURE_AR
    if ctx["lang"] == "mixed":
        phr = AI_SELF_DISCLOSURE_EN + AI_SELF_DISCLOSURE_AR
    hits = _phrase_hits(ctx["lower"], text, phr)
    return SignalResult(
        "MJ-ANY-02", "SEM/meta (agent-B) + LM-005 family", "AI self-disclosure phrases",
        "any", fired=len(hits) > 0, value=float(len(hits)),
        threshold_note="any occurrence",
        weight=0.99, evidence=hits[:5],
        caveat="Near-conclusive when present, but trivially removed by editing; "
               "absence proves nothing.")


def sig_meta_filler(text, ctx):
    phr = META_FILLER_EN if ctx["lang"] == "en" else (
        META_FILLER_AR if ctx["lang"] == "ar" else META_FILLER_EN + META_FILLER_AR)
    hits = _phrase_hits(ctx["lower"], text, phr)
    n = max(1, len(ctx["words"]))
    rate = len(hits) / n * 1000
    return SignalResult(
        "MJ-ANY-03", "LM-005", "Meta-filler phrase density",
        "any", fired=rate >= 3.0, value=round(rate, 2),
        threshold_note="≥3 filler phrases per 1000 words",
        weight=0.8, evidence=hits[:6],
        caveat="Arabic list is EXPERIMENTAL (gaps/03): common in human Arabic "
               "academic register too — treat as weak evidence for Arabic.")


def sig_cliche_frame(text, ctx):
    lower = ctx["lower"]
    op = _phrase_hits(lower[:400], text[:400], CLICHE_OPENERS_EN, 3)
    cl = _phrase_hits(lower, text, CLICHE_CLOSERS_EN if ctx["lang"] != "ar"
                      else CLICHE_CLOSERS_AR, 3)
    fired = bool(op) and bool(cl)
    return SignalResult(
        "MJ-ANY-04", "LM-010,LM-011,STRUCT-005,STRUCT-006", "Cliché opener + closer frame",
        "any", fired=fired, value=float(len(op) + len(cl)),
        threshold_note="cliché opening AND cliché conclusion both present",
        weight=0.75, evidence=(op + cl)[:6],
        caveat="Taught in composition classes; humans use these frames. "
               "Only meaningful combined with other signals.")


def sig_em_dash(text, ctx):
    n = max(1, len(ctx["words"]))
    count = text.count("\u2014") + text.count("\u2013")
    rate = count / n * 1000
    hits = []
    i = text.find("\u2014")
    if i >= 0:
        hits.append(Evidence(excerpt=_excerpt(text, i), position=i))
    return SignalResult(
        "MJ-ANY-05", "LM-006,STRUCT-010", "Em/en-dash rate",
        "any", fired=rate > 4.0, value=round(rate, 2),
        threshold_note=">4 per 1000 words (corpus threshold)",
        weight=0.7, evidence=hits,
        caveat="Rapidly decaying signal (half-life est. in corpus); many human "
               "writers and most editors love the em dash.")


def sig_rule_of_three(text, ctx):
    pat = re.compile(r"\b[\w\u0600-\u06FF]+،?\s*,?\s*[\w\u0600-\u06FF]+،?\s*,?\s*"
                     r"(?:and|or|و)\s+[\w\u0600-\u06FF]+", re.IGNORECASE)
    # stricter: X, Y, and Z with commas
    strict = re.compile(r"[\w\u0600-\u06FF]+\s*[,،]\s*[\w\u0600-\u06FF]+\s*[,،]?\s*"
                        r"(?:and|و)\s+[\w\u0600-\u06FF]+", re.IGNORECASE)
    ms = list(strict.finditer(text))
    n_sent = max(1, len(ctx["sents"]))
    rate = len(ms) / n_sent
    ev = [Evidence(excerpt=_excerpt(text, m.start()), position=m.start())
          for m in ms[:4]]
    return SignalResult(
        "MJ-ANY-06", "LM-008,STRUCT-002", "Tricolon (rule-of-three) density",
        "any", fired=rate >= 0.35, value=round(rate, 3),
        threshold_note="≥0.35 triplets per sentence",
        weight=0.65, evidence=ev,
        caveat="A rhetorical device as old as Cicero; density, not presence, "
               "is what matters.")


def sig_not_x_but_y(text, ctx):
    pat = re.compile(r"\bnot (?:just|only|merely)\b[^.!?\n]{0,80}?\bbut\b",
                     re.IGNORECASE)
    ms = list(pat.finditer(text))
    n_sent = max(1, len(ctx["sents"]))
    ev = [Evidence(excerpt=_excerpt(text, m.start()), position=m.start())
          for m in ms[:4]]
    return SignalResult(
        "MJ-EN-07", "LM-009", "'Not just X, but Y' contrast template",
        "en", fired=len(ms) / n_sent >= 0.1, value=float(len(ms)),
        threshold_note="≥1 per 10 sentences",
        weight=0.7, evidence=ev)


def sig_hedging(text, ctx):
    hits = _phrase_hits(ctx["lower"], text, HEDGES_EN)
    n = max(1, len(ctx["words"]))
    rate = len(hits) / n * 1000
    return SignalResult(
        "MJ-EN-08", "LM-017", "Hedging-qualifier density",
        "en", fired=rate >= 4.0, value=round(rate, 2),
        threshold_note="≥4 hedges per 1000 words",
        weight=0.6, evidence=hits[:5],
        caveat="ELEVATED FALSE-POSITIVE RISK for non-native academic writers, "
               "who are trained to hedge (gaps/01).")


def sig_transition_chain(text, ctx):
    sents = ctx["sents"]
    starts = []
    for s in sents:
        first = s.split()[0].strip(",").lower() if s.split() else ""
        starts.append(first)
    chain = 0
    best = 0
    for f in starts:
        if f in TRANSITIONS_EN:
            chain += 1
            best = max(best, chain)
        else:
            chain = 0
    total = sum(1 for f in starts if f in TRANSITIONS_EN)
    rate = total / max(1, len(sents))
    ev = [Evidence(excerpt=s[:70], detail=s.split()[0]) for s in sents
          if s.split() and s.split()[0].strip(",").lower() in TRANSITIONS_EN][:5]
    return SignalResult(
        "MJ-EN-09", "LM-004,STRUCT-013", "Sentence-initial transition chain",
        "en", fired=(rate >= 0.25 or best >= 3), value=round(rate, 3),
        threshold_note="≥25% of sentences transition-initial, or ≥3 consecutive",
        weight=0.75, evidence=ev,
        caveat="Non-native writers are explicitly taught these connectors "
               "(gaps/01) — strong FP risk on Arab students' English.")


def sig_sycophancy(text, ctx):
    hits = _phrase_hits(ctx["lower"][:300], text[:300], SYCOPHANCY_OPENERS_EN, 3)
    return SignalResult(
        "MJ-EN-10", "LM-014", "Sycophancy opener",
        "en", fired=bool(hits), value=float(len(hits)),
        threshold_note="present in first 300 chars",
        weight=0.8, evidence=hits,
        caveat="Chat-transcript artifact; rarely survives into edited documents.")


def sig_burstiness(text, ctx):
    """Language-agnostic proxy: coefficient of variation of sentence lengths."""
    lens = [len(_WORD_RE.findall(s)) for s in ctx["sents"]]
    if len(lens) < 8:
        return SignalResult(
            "MJ-ANY-11", "STRUCT-012,STAT burstiness family", "Sentence-length burstiness (CV proxy)",
            "any", fired=False, value=-1.0,
            threshold_note="needs ≥8 sentences; NOT EVALUATED",
            weight=0.7, caveat="Text too short for a stable estimate "
                               "(text_length_sensitivity: low_on_short).")
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0.0
    return SignalResult(
        "MJ-ANY-11", "STRUCT-012,STAT burstiness family", "Sentence-length burstiness (CV proxy)",
        "any", fired=cv < 0.32, value=round(cv, 3),
        threshold_note="CV < 0.32 → suspiciously uniform (editorial proxy for "
                       "low burstiness; NOT token-level PPL burstiness)",
        weight=0.65,
        caveat="Weak surface proxy for the statistical signal. Non-native and "
               "bureaucratic prose is also uniform (Liang 2304.02819). "
               "Never use alone.")


def sig_paragraph_uniformity(text, ctx):
    lens = [len(_WORD_RE.findall(p)) for p in ctx["paras"]]
    lens = [l for l in lens if l >= 15]
    if len(lens) < 4:
        return SignalResult(
            "MJ-ANY-12", "STRUCT-003", "Paragraph-length uniformity",
            "any", fired=False, value=-1.0,
            threshold_note="needs ≥4 substantive paragraphs; NOT EVALUATED",
            weight=0.6)
    mean = statistics.mean(lens)
    cv = statistics.pstdev(lens) / mean if mean else 0.0
    return SignalResult(
        "MJ-ANY-12", "STRUCT-003", "Paragraph-length uniformity",
        "any", fired=cv < 0.25, value=round(cv, 3),
        threshold_note="CV < 0.25 across paragraphs (corpus threshold)",
        weight=0.6, evidence=[Evidence(excerpt=f"paragraph word counts: {lens}")])


def sig_markdown_overstructure(text, ctx):
    n_words = max(1, len(ctx["words"]))
    headers = len(re.findall(r"^#{1,4}\s", text, re.MULTILINE))
    bold_colon = len(re.findall(r"\*\*[^*\n]{1,40}\*\*\s*[::]", text))
    emoji_bullets = len(re.findall(
        r"^\s*[-*•]?\s*[\U0001F300-\U0001FAFF\u2705\u2728\u2b50\u26a1]",
        text, re.MULTILINE))
    score = (headers + bold_colon + emoji_bullets) / n_words * 1000
    ev = []
    m = re.search(r"\*\*[^*\n]{1,40}\*\*\s*[::]", text)
    if m:
        ev.append(Evidence(excerpt=_excerpt(text, m.start()), position=m.start()))
    return SignalResult(
        "MJ-ANY-13", "STRUCT-007,STRUCT-008,STRUCT-001,STRUCT-016",
        "Markdown over-structuring (headers + **Bold:** + emoji bullets)",
        "any", fired=score >= 6.0, value=round(score, 2),
        threshold_note="≥6 structuring tokens per 1000 words",
        weight=0.85, evidence=ev,
        caveat="Signals *tool-assisted formatting*, not authorship per se "
               "(non_native_fp_risk: medium, per core/08 _v2_meta).")


def sig_sentence_start_diversity(text, ctx):
    sents = ctx["sents"]
    if len(sents) < 8:
        return SignalResult(
            "MJ-ANY-14", "LM-019,STRUCT-004,STRUCT-019", "Sentence-opener diversity (entropy)",
            "any", fired=False, value=-1.0,
            threshold_note="needs ≥8 sentences; NOT EVALUATED", weight=0.7)
    bigrams = []
    for s in sents:
        ws = _WORD_RE.findall(s.lower())
        bigrams.append(" ".join(ws[:2]))
    freq = {}
    for b in bigrams:
        freq[b] = freq.get(b, 0) + 1
    n = len(bigrams)
    ent = -sum((c / n) * math.log2(c / n) for c in freq.values())
    top = max(freq.items(), key=lambda kv: kv[1])
    ev = [Evidence(excerpt=f"most repeated opener: '{top[0]}' ×{top[1]} "
                           f"of {n} sentences")]
    return SignalResult(
        "MJ-ANY-14", "LM-019,STRUCT-004,STRUCT-019", "Sentence-opener diversity (entropy)",
        "any", fired=ent < 2.0, value=round(ent, 2),
        threshold_note="first-two-word entropy < 2.0 bits (corpus threshold)",
        weight=0.7, evidence=ev)


def sig_multiple_conclusions(text, ctx):
    phr = (CLICHE_CLOSERS_EN if ctx["lang"] != "ar" else CLICHE_CLOSERS_AR)
    marks = []
    lower = ctx["lower"]
    for ph in phr:
        i = 0
        while True:
            i = lower.find(ph, i)
            if i < 0:
                break
            marks.append(i)
            i += len(ph)
    marks.sort()
    fired = len(marks) >= 2
    ev = [Evidence(excerpt=_excerpt(text, i), position=i) for i in marks[:3]]
    return SignalResult(
        "MJ-ANY-15", "STRUCT-014", "Multiple conclusion markers",
        "any", fired=fired, value=float(len(marks)),
        threshold_note="≥2 distinct conclusion markers",
        weight=0.7, evidence=ev)


def sig_personal_voice_absence(text, ctx):
    if ctx["lang"] == "ar":
        pronouns = len(re.findall(r"\b(?:أنا|رأيي|برأيي|أعتقد|لاحظت|جربت|واجهت)\b", text))
    else:
        pronouns = len(re.findall(r"\b(?:i|my|me|we|our)\b", ctx["lower"]))
    n = max(1, len(ctx["words"]))
    rate = pronouns / n * 1000
    return SignalResult(
        "MJ-ANY-16", "SEM personal-voice family (agent B)", "Personal-voice absence",
        "any", fired=(rate < 1.0 and n > 300), value=round(rate, 2),
        threshold_note="<1 first-person marker per 1000 words in 300+ word text",
        weight=0.5,
        caveat="Academic genres FORBID first person in many traditions "
               "(including much Arabic academic writing) — among the weakest "
               "signals here; ignore for formal papers.")


ALL_SIGNALS = [
    sig_focal_words, sig_ai_self_disclosure, sig_meta_filler, sig_cliche_frame,
    sig_em_dash, sig_rule_of_three, sig_not_x_but_y, sig_hedging,
    sig_transition_chain, sig_sycophancy, sig_burstiness,
    sig_paragraph_uniformity, sig_markdown_overstructure,
    sig_sentence_start_diversity, sig_multiple_conclusions,
    sig_personal_voice_absence,
]


def build_context(text: str) -> dict:
    return {
        "lang": detect_language(text),
        "lower": text.lower(),
        "words": words(text),
        "sents": sentences(text),
        "paras": paragraphs(text),
    }
