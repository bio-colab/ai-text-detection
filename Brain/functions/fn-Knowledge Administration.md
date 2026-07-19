---
tags: [brain, function, knowledge]
aliases: [Knowledge Administration, fn-Knowledge Administration, إدارة المعرفة]
type: cognitive-function
function_id: 12
---

# fn-Knowledge Administration — Curate the taxonomy

**Role:** Own create/read/update/retire for the knowledge base so the brain stays true.

## Knowledge inventory

| Layer | Location | Status |
|-------|----------|--------|
| Unified README | [[README]] | Source of truth for package intent |
| Core JSONs 01–10 | `core/` | 174 patterns + taxonomy |
| Gaps 01–08 | `gaps/` | Critical limitations |
| Reference | `reference/` | Agent B deep materials + comparison |
| Brain | `Brain/` | Cognitive OS (this system) |

## CRUD rules

### Create
- New pattern must include: `id`, `name`, `detection`, `confidence`, `sources`, failure links to gaps.
- Source checklist ≥3 of: arxiv, github, huggingface, wikipedia, commercial (from ORIGINAL_README_A anti-stop rules).

### Read
- Always prefer unified core over raw reference when conflict; note Agent A (engineering) vs Agent B (analytical) merge in README.

### Update
- Fast-DetectGPT arXiv id must stay **2310.05130** (corrected in v1.1).
- Refresh half-life estimates every 3–6 months.
- When commercial claims change, update gap 06 + core 06 with “claimed vs independent”.

### Retire / demote
- Style markers after evasion becomes free → lower confidence, tag `#deprecated-signal`.
- Do not delete history; move narrative to [[memory-Long Term]].

## Quality gates (self-review mechanism)

```
Search → Classify → Count → Review
coverage target ≥ 95%
patterns per specialty file ≥ 15 (historical rule for core packs)
```

## MOC maintenance

- [[moc-Core Signals]]
- [[moc-Gaps]]
- [[moc-Reference]]
- [[moc-Taxonomy]]

Every MOC must list all children with one-line purpose.

## Links

- Related: [[fn-Learning]], [[fn-Watching]], [[fn-Linking]]
- Hub: [[00_FULL_BRAIN]]
