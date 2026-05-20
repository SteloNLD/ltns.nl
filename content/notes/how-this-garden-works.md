---
title: How this garden works
date: 2026-05-19
lastmod: 2026-05-19
description: Structure, conventions, and workflow for this digital garden
tags: [meta]
stage: evergreen
---

This garden follows a zettelkasten-inspired structure. Notes are atomic, linked by idea rather than category, and grow over time.

## Structure

| Folder | What lives here | Public |
|---|---|---|
| `notes/` | Permanent evergreen notes — one idea per note | yes |
| `references/` | One note per source (book, article, talk, video) | yes |
| `inbox/` | Fleeting captures, unprocessed thoughts | no |
| `journal/` | Daily notes | no |
| `templates/` | Note templates | no |

`inbox/` and `journal/` are gitignored and never published.

## Workflow

1. Quick thought or link → `inbox/` (no template, just dump it)
2. Reading something → `references/` note while reading, clip with Obsidian Web Clipper
3. Process inbox → either discard, expand into a `notes/` note, or link to an existing one
4. Notes grow and link to each other over time
5. When a cluster of notes forms around a topic → create a MOC in `notes/`
6. Active MOCs and areas of focus → surfaced in [[now]]

## Note stages

Every note in `notes/` has a `stage` field:

- `seedling` — rough, just captured, may be incomplete
- `budding` — being developed, mostly coherent
- `evergreen` — stable, well-linked, stands on its own

References do not use stages.

## Naming conventions

| Type | Convention | Example |
|---|---|---|
| Note | kebab-case title | `compound-interest-of-knowledge.md` |
| Reference | `Author - Title` | `Ahrens - How to Take Smart Notes.md` |
| MOC | `MOC - Topic` | `MOC - Homelab.md` |
| Journal | `YYYY-MM-DD` | `2026-05-19.md` |
| Inbox | anything | `random thought.md` |

## Frontmatter

**Note**
```yaml
title:
date:
lastmod:
tags: []
stage: seedling
description:
```

**Reference**
```yaml
title:
date:
tags: []
type:        # book, article, talk, video, podcast
author:
url:
```

**MOC**
```yaml
title:
date:
lastmod:
tags: []
```

**Journal**
```yaml
title:       # the date
date:
tags: []
```

## Tags

Three kinds of tags, all in the `tags` field:

- **Domain** — your topic areas: `simracing`, `travel`, `homelab`, `it`
- **Concept** — granular ZK keywords: `mental-model`, `performance`, `networking`
- **Stage** — note maturity: `seedling`, `budding`, `evergreen` (mirrors the `stage` field, useful for filtering)

Nested tags for sub-topics: `#simracing/setups`, `#homelab/networking`
