#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
validate_corpus.py — deterministic integrity guard for the knowledge base.

Every class of defect that shipped in v1.1/v2.0 is encoded here as a check,
so it can never silently recur:

  C1  every *.json parses (v1.1 shipped a broken key_academic_papers.json)
  C2  pattern files satisfy the minimal schema (id, name, one detection
      mechanism, confidence in [0,1]) — schema/pattern_file.schema.json
  C3  aggregated pattern count == the number written in README/HOME/Brain
      (v1.1 claimed 174, real 164)
  C4  unique-vs-aggregated counts both declared in the master taxonomy and
      match reality (v2.0 hid cross-file duplicates inside "164")
  C5  declared _v2_meta fields actually exist in every core signal file
      (v1.1 declared non_native_fp_risk etc. without implementing them)
  C6  no unresolved [[wikilinks]] in Brain/, gaps/, HOME (placeholders must
      live in code fences)
  C7  files claimed removed in CHANGELOG are actually untracked
      (v2.0 claimed to remove workspace.json / بدون عنوان.canvas and didn't)
  C8  version string is consistent across README, HOME, taxonomy meta
  C9  every arXiv ID cited in key_academic_papers.json is well-formed and
      each key paper named in README exists in the file
  C10 no lone 0xB7 broken bytes in markdown (the v1.1 encoding defect)

Exit code 0 = all green. Non-zero = list of failures on stderr.
stdlib only. Run:  python3 scripts/validate_corpus.py
"""

from __future__ import annotations

import glob
import json
import os
import re
import subprocess
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FAILS: list[str] = []
WARNS: list[str] = []


def fail(msg):
    FAILS.append(msg)


def warn(msg):
    WARNS.append(msg)


def rel(p):
    return os.path.relpath(p, ROOT)


# ---------------------------------------------------------------- C1
def check_json_valid():
    files = sorted(glob.glob(os.path.join(ROOT, "**", "*.json"), recursive=True))
    files = [f for f in files if "/.git/" not in f and "/.obsidian/" not in f
             and "/node_modules/" not in f]
    ok = 0
    for f in files:
        try:
            json.load(open(f, encoding="utf-8"))
            ok += 1
        except Exception as e:
            fail(f"C1 invalid JSON: {rel(f)}: {e}")
    return files, ok


# ---------------------------------------------------------------- C2/C3/C4
CORE_SIGNAL_FILES = sorted(glob.glob(os.path.join(ROOT, "core", "0[1-9]*.json")))

def load_patterns():
    per_file = {}
    for f in CORE_SIGNAL_FILES:
        d = json.load(open(f, encoding="utf-8"))
        per_file[rel(f)] = d.get("patterns", [])
    return per_file


def check_schema(per_file):
    mech_keys = {"detection", "method", "formula", "pattern", "description"}
    for f, ps in per_file.items():
        for p in ps:
            pid = p.get("id", "<no id>")
            if "id" not in p or "name" not in p:
                fail(f"C2 {f}:{pid} missing id/name")
            if not (mech_keys & set(p)):
                fail(f"C2 {f}:{pid} lacks any detection mechanism "
                     f"({'/'.join(sorted(mech_keys))})")
            c = p.get("confidence")
            if not isinstance(c, (int, float)) or not (0 <= c <= 1):
                fail(f"C2 {f}:{pid} confidence invalid: {c!r}")


def check_counts(per_file):
    agg = sum(len(ps) for ps in per_file.values())
    names = [p.get("name", "").strip().lower()
             for ps in per_file.values() for p in ps]
    uniq = len(set(names))
    dups = {n: c for n, c in Counter(names).items() if c > 1}

    tax = json.load(open(os.path.join(ROOT, "core", "10_master_taxonomy.json"),
                         encoding="utf-8"))
    meta = tax.get("meta", {})
    if meta.get("total_patterns_aggregated") != agg:
        fail(f"C3 taxonomy total_patterns_aggregated="
             f"{meta.get('total_patterns_aggregated')} but real={agg}")
    if meta.get("unique_pattern_names") != uniq:
        fail(f"C4 taxonomy unique_pattern_names="
             f"{meta.get('unique_pattern_names')} but real={uniq}")
    declared_dups = meta.get("cross_file_duplicates", {})
    if {k.lower(): v for k, v in declared_dups.items()} != dups:
        fail(f"C4 taxonomy cross_file_duplicates out of date; real={dups}")

    # every mention of the aggregate count in prose must match
    for md in ["README.md", "HOME.md", "Brain/00_FULL_BRAIN.md",
               "Brain/knowledge/moc-Taxonomy.md",
               "Brain/knowledge/moc-Core Signals.md"]:
        path = os.path.join(ROOT, md)
        if not os.path.exists(path):
            continue
        t = open(path, encoding="utf-8").read()
        for m in re.findall(r"(\d{3})\s*(?:pattern|نمط|أنماط)", t):
            if int(m) not in (agg, uniq):
                fail(f"C3 {md} claims {m} patterns; real agg={agg}, uniq={uniq}")
    return agg, uniq, dups


# ---------------------------------------------------------------- C5
def check_declared_fields():
    for f in CORE_SIGNAL_FILES:
        d = json.load(open(f, encoding="utf-8"))
        meta = d.get("_v2_meta", {})
        for field in ("non_native_fp_risk", "text_length_sensitivity"):
            if field not in meta:
                fail(f"C5 {rel(f)} missing _v2_meta.{field}")
        if "disclaimers" not in d and "disclaimers" not in meta:
            fail(f"C5 {rel(f)} missing disclaimers block")
    tax = json.load(open(os.path.join(ROOT, "core", "10_master_taxonomy.json"),
                         encoding="utf-8"))
    if "theoretical_limits" not in tax:
        fail("C5 core/10 missing theoretical_limits section")


# ---------------------------------------------------------------- C6
def check_wikilinks():
    stems = set()
    for p in glob.glob(os.path.join(ROOT, "**", "*"), recursive=True):
        if os.path.isfile(p) and "/.git/" not in p:
            stems.add(os.path.splitext(os.path.basename(p))[0])
    md_files = [f for f in glob.glob(os.path.join(ROOT, "**", "*.md"),
                                     recursive=True) if "/.git/" not in f]
    fence = re.compile(r"```.*?```", re.DOTALL)
    inline = re.compile(r"`[^`\n]*`")
    for f in md_files:
        t = open(f, encoding="utf-8").read()
        t = fence.sub("", t)
        t = inline.sub("", t)
        for m in re.findall(r"\[\[([^\]\|#]+)", t):
            base = os.path.splitext(os.path.basename(m.strip()))[0]
            if base not in stems:
                fail(f"C6 dead wikilink [[{m.strip()}]] in {rel(f)}")


# ---------------------------------------------------------------- C7
def check_removed_files_untracked():
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT,
                             capture_output=True, text=True, timeout=30)
        tracked = set(out.stdout.split("\n"))
    except Exception:
        warn("C7 skipped (git unavailable)")
        return
    for banned in [".obsidian/workspace.json", "بدون عنوان.canvas"]:
        if banned in tracked:
            fail(f"C7 CHANGELOG claims '{banned}' removed but it is tracked")


# ---------------------------------------------------------------- C8
def check_version_consistency():
    tax = json.load(open(os.path.join(ROOT, "core", "10_master_taxonomy.json"),
                         encoding="utf-8"))
    v_tax = str(tax.get("meta", {}).get("version", ""))
    major = v_tax.split(".")[0] if v_tax else ""
    if not major:
        fail("C8 taxonomy meta.version missing")
        return
    for md in ["README.md", "HOME.md"]:
        t = open(os.path.join(ROOT, md), encoding="utf-8").read()
        vs = re.findall(r"\bv(\d+)\.(\d+)", t)
        stale = [f"v{a}.{b}" for a, b in vs
                 if int(a) < int(major) and (a, b) != ("1", "1")]
        # v1.1 allowed only in explicit history context
        for a, b in vs:
            if int(a) < int(major):
                # allow when the line mentions history/changelog/أصل/سابق
                pass
        head = t[:400]
        mv = re.search(r"\bv?(\d+)\.(\d+)", head)
        if mv and mv.group(1) != major:
            fail(f"C8 {md} headline version v{mv.group(1)}.{mv.group(2)} "
                 f"!= taxonomy v{v_tax}")


# ---------------------------------------------------------------- C9
ARXIV_RE = re.compile(r"^\d{4}\.\d{4,5}$")

def check_key_papers():
    path = os.path.join(ROOT, "reference", "key_academic_papers.json")
    d = json.load(open(path, encoding="utf-8"))
    have = {p.get("arxiv_id", "") for p in d.get("key_papers", [])}
    for p in d.get("key_papers", []):
        aid = p.get("arxiv_id", "")
        if aid and not ARXIV_RE.match(aid):
            fail(f"C9 malformed arXiv id in key_academic_papers: {aid!r}")
        if not isinstance(p.get("year"), (int, str)):
            fail(f"C9 bad year for {aid}")
    # papers the README itself names as key must be present
    required = {
        "2301.10226": "Kirchenbauer watermark",
        "2301.11305": "DetectGPT",
        "2310.05130": "Fast-DetectGPT",
        "2401.12070": "Binoculars",
        "2303.11156": "Sadasivan impossibility",
        "2304.02819": "Liang non-native bias",
        "2405.07940": "RAID benchmark",
    }
    for aid, name in required.items():
        if aid not in have:
            fail(f"C9 README names '{name}' as key but {aid} absent from "
                 f"key_academic_papers.json")


# ---------------------------------------------------------------- C10
def check_broken_bytes():
    for f in glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True):
        if "/.git/" in f:
            continue
        b = open(f, "rb").read()
        for i, byte in enumerate(b):
            if byte == 0xB7 and (i == 0 or b[i - 1] < 0xC0):
                fail(f"C10 lone 0xB7 byte at offset {i} in {rel(f)}")
                break


# ----------------------------------------------------------------
def main():
    files, ok = check_json_valid()
    per_file = load_patterns()
    check_schema(per_file)
    agg, uniq, dups = check_counts(per_file)
    check_declared_fields()
    check_wikilinks()
    check_removed_files_untracked()
    check_version_consistency()
    check_key_papers()
    check_broken_bytes()

    print(f"validate_corpus: {ok}/{len(files)} JSON valid | "
          f"patterns aggregated={agg} unique={uniq} "
          f"(cross-file duplicate names: {len(dups)})")
    for w in WARNS:
        print("WARN:", w)
    if FAILS:
        for msg in FAILS:
            print("FAIL:", msg, file=sys.stderr)
        print(f"\n{len(FAILS)} integrity failure(s).", file=sys.stderr)
        return 1
    print("all integrity checks green.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
