# -*- coding: utf-8 -*-
"""Tests for the mijhar evidence scanner. Run: python3 -m pytest tests/ -q"""
import json
import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

from mijhar import scan_text, to_json, to_human  # noqa: E402
from mijhar.signals import detect_language        # noqa: E402


def read(name):
    with open(os.path.join(ROOT, "examples", name), encoding="utf-8") as f:
        return f.read()


# ---------------------------------------------------------------- language
def test_language_detection():
    assert detect_language("This is plain English text.") == "en"
    assert detect_language("هذا نص عربي بالكامل من دون كلمات أجنبية.") == "ar"
    assert detect_language("") == "unknown"


# ---------------------------------------------------------------- behavior
def test_ai_like_sample_fires_many_signals():
    r = scan_text(read("sample_ai_like.txt"))
    assert r["summary"]["signals_fired"] >= 5, \
        "the deliberately AI-styled sample must trip multiple signals"
    fired_ids = {s["signal_id"] for s in r["fired_signals"]}
    assert "MJ-EN-01" in fired_ids   # focal words: delve/tapestry/pivotal…
    assert "MJ-ANY-04" in fired_ids  # cliché opener+closer frame


def test_human_like_sample_stays_quiet():
    r = scan_text(read("sample_human_like.txt"))
    assert r["summary"]["signals_fired"] <= 1, \
        "personal, bursty human sample should fire at most a stray signal"


def test_arabic_sample_uses_experimental_path():
    r = scan_text(read("sample_arabic.txt"))
    assert r["input_stats"]["language"] == "ar"
    # English-only signals must be skipped, not silently misapplied
    skipped = {s["signal_id"] for s in r["skipped_signals"]}
    assert "MJ-EN-01" in skipped
    # the Arabic warning must be active
    assert any("EXPERIMENTAL" in w or "تجريب" in w
               for w in r["active_warnings"])


def test_evidence_always_has_excerpts():
    r = scan_text(read("sample_ai_like.txt"))
    for s in r["fired_signals"]:
        if s["signal_id"] in ("MJ-EN-01", "MJ-ANY-03", "MJ-ANY-04"):
            assert s["evidence"], f"{s['signal_id']} fired without evidence"


# ---------------------------------------------------------------- doctrine
def test_no_verdict_and_no_probability_anywhere():
    r = scan_text(read("sample_ai_like.txt"))
    dumped = json.dumps(r).lower()
    assert '"p_ai"' not in dumped and '"score"' not in dumped
    assert r["doctrine"]["verdict"].startswith("NONE")
    # weights must never be summed into a total score field
    assert "total_score" not in dumped
    assert "ai_probability" not in dumped


def test_short_text_refuses_conclusions():
    r = scan_text("Delve into the tapestry.")
    assert "too short" in r["summary"]["reading"].lower()
    assert any("150" in w for w in r["active_warnings"])


def test_quiet_result_is_not_claimed_as_human():
    r = scan_text("The dog sat by the door. " * 30)
    reading = r["summary"]["reading"]
    if r["summary"]["signals_fired"] == 0:
        assert "not" in reading.lower()  # "NOT evidence of human authorship"


def test_fp_warning_always_present():
    for sample in ("sample_ai_like.txt", "sample_human_like.txt"):
        r = scan_text(read(sample))
        assert any("61.22" in w for w in r["active_warnings"]), \
            "Liang FPR warning must appear on every report"


# ---------------------------------------------------------------- outputs
def test_json_roundtrip_and_human_render():
    r = scan_text(read("sample_ai_like.txt"))
    j = to_json(r)
    assert json.loads(j)["tool"] == "mijhar"
    h = to_human(r)
    assert "DOCTRINE" in h and "mijhar" in h


def test_chain_of_authenticity():
    sample = read("sample_ai_like.txt")
    r = scan_text(sample, filename="examples/sample_ai_like.txt")
    coa = r.get("chain_of_authenticity", {})
    assert "sha256" in coa
    import hashlib
    assert coa["sha256"] == hashlib.sha256(sample.encode("utf-8")).hexdigest()
    assert coa["deterministic"] is True
    assert coa["taxonomy_version"] == "v3.1-open"
    assert "git_commit" in coa
    assert "timestamp_utc" in coa
    assert "reproducible_cli" in coa
    assert "examples/sample_ai_like.txt" in coa["reproducible_cli"]
    human = to_human(r)
    assert "SHA-256" in human
    assert coa["sha256"] in human


def test_cli_smoke():
    env = dict(os.environ, PYTHONPATH=os.path.join(ROOT, "src"))
    p = subprocess.run(
        [sys.executable, "-m", "mijhar",
         os.path.join(ROOT, "examples", "sample_ai_like.txt"), "--json"],
        capture_output=True, text=True, env=env, timeout=60)
    assert p.returncode == 0, p.stderr
    out = json.loads(p.stdout)
    assert out["summary"]["signals_fired"] >= 5


def test_emoji_and_short_edge_cases_stay_quiet():
    r = scan_text("😊🚀🔥")
    assert r["summary"]["signals_fired"] == 0, "emoji-only text must not fire formatting signals"
    r_empty = scan_text("   ")
    assert r_empty["summary"]["signals_fired"] == 0


def test_all_signal_corpus_references_exist_in_core():
    from mijhar.signals import ALL_SIGNALS, build_context
    core_ids = set()
    for f in os.listdir(os.path.join(ROOT, "core")):
        if f.endswith(".json") and f.startswith("0"):
            d = json.load(open(os.path.join(ROOT, "core", f), encoding="utf-8"))
            for p in d.get("patterns", []):
                if "id" in p:
                    core_ids.add(p["id"])
    ctx = build_context("This is a sample test sentence.")
    for fn in ALL_SIGNALS:
        res = fn("sample", ctx)
        for pid in res.corpus_ref.split(","):
            pid = pid.strip()
            assert pid in core_ids, f"Signal {res.signal_id} references unknown pattern '{pid}'"


def test_docx_reading_support():
    p = os.path.join(ROOT, "examples", "الإشارة_المقنعة_نحل_وديمقراطية.docx")
    if os.path.exists(p):
        from mijhar.__main__ import _read_file
        t = _read_file(p)
        assert len(t) > 1000
        assert "نحل" in t


# ---------------------------------------------------------------- corpus
def test_validate_corpus_is_green():
    p = subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "validate_corpus.py")],
        capture_output=True, text=True, timeout=120)
    assert p.returncode == 0, "corpus integrity guard failed:\n" + p.stderr
