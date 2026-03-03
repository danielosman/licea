# Licea Warsaw — Project Overview

## Purpose

This project collects and structures information about Warsaw high schools (Polish: *licea*). It is organized in two processing levels: raw scraped data (Level 0) and normalized structured data (Level 1).

## Project Structure

```
licea/
├── CLAUDE.md
├── level0.md            # Level 0 scraping process (detailed)
├── level1.md            # Level 1 processing process (detailed)
├── template.md          # Level 1 output template
├── init/
│   ├── Licea_Warszawa_Final.xlsx   # Source spreadsheet with school data
│   └── schools_urls.md             # Authoritative mapping: school folder name → website URL
├── schools/
│   ├── 15_Zmichowska/
│   │   ├── data/
│   │   │   ├── sitemap.md              # Level 0: HTML page index
│   │   │   ├── documents.md            # Level 0: downloadable documents list
│   │   │   └── content/
│   │   │       ├── overview.md         # Level 0: root page
│   │   │       └── o_szkole.md         # Level 0: one file per scraped page
│   │   ├── 15_Zmichowska_agent_mapping.md  # Level 1 phase 0: agent file assignments
│   │   ├── 15_Zmichowska_Agent_A.md    # Level 1 phase 1: reader agent output
│   │   ├── 15_Zmichowska_Agent_B.md    # Level 1 phase 2: reader agent output
│   │   ├── 15_Zmichowska_Agent_C.md    # Level 1 phase 3: reader agent output
│   │   ├── 15_Zmichowska_Agent_D.md    # Level 1 phase 4: reader agent output
│   │   ├── 15_Zmichowska_Agent_E.md    # Level 1 phase 5: reader agent output
│   │   └── 15_Zmichowska.md            # Level 1 phase 6: final structured output
│   └── ...
├── scrapers/             # Scripts for collecting Level 0 data
└── processors/           # Scripts for transforming Level 0 → Level 1
```

## School URL lookup

`init/schools_urls.md` is the single source of truth for each school's website. Always read the school's URL from that file — never guess or construct URLs manually. Schools marked `brak` have no known website.

## Language

**All output files — scraped content, structured profiles, agent outputs, sitemap metadata — must be written in Polish.** This applies to both Level 0 and Level 1. Do not translate, summarize, or produce any content in English (or any other language). The only exceptions are technical field names defined in `template.md` (e.g. `status: ok`, `scraped:` dates).

## Conventions

- Each school has its own folder under `schools/`, named `{number}_{SchoolName}`, e.g. `15_Zmichowska`.
- The `data/` subfolder holds Level 0 content:
  - `data/sitemap.md` — index of all HTML pages; one `## slug` entry per page with metadata bullet points
  - `data/documents.md` — list of downloadable documents (PDF, DOCX, etc.); same section format as `sitemap.md` (`## link_name` + `- url:` + `- from_page:`); selected documents that were read also have a `- content_file:` field pointing to their extract in `data/content/`
  - `data/content/` — one `.md` file per scraped page or document extract (Phase 4)
- Level 1 produces two files in the school folder:
  - `{folder_name}_agent_mapping.md` — agent-to-file assignment created before any agent is launched
  - `{folder_name}.md` — final structured profile following `template.md`

## Level 0 — Raw Data Scraping

Faithful dump of the school's website. No interpretation. See **`level0.md`** for the full process.

## Level 1 — Structured Data

Normalized school profile following `template.md`. Input comes exclusively from `data/content/` files (and `data/sitemap.md` for page metadata). See **`level1.md`** for the full process (including the multi-agent approach and synthesis rules).
