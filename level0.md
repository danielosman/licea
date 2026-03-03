# Level 0 — Raw Data Scraping

Level 0 is a faithful dump of content from the school's website — no classification, normalization, or interpretation. The goal is to preserve the source material as-is.

**Language rule: all output must be in Polish.** This includes page titles written in the file header, all extracted text, and all sitemap metadata fields (title, link_name). Do not translate anything into English.

Scraping is done in three phases.

---

## Phase 1 — Build `sitemap.md` and `documents.md`

Navigate to the school's root URL (from `init/schools_urls.md`) and discover all internal pages. For each page found (including the root), record an entry in `data/sitemap.md` using the following format:

```
## <md_filename>

- url: <full URL>
- title: <page title>
- link_name: <anchor text that led to this page>
- from_page: <md_filename of the referring page>
- content_selector: <CSS selector for main content area, e.g. `main`, `#content`, `.entry-content` — used to skip navigation>
- status: <ok | error (...) | skipped>
- scraped: <ISO date>
```

In addition to pages, record all downloadable documents found on any visited page in a separate `data/documents.md` file, using the same section-based format as `sitemap.md`:

```
## <anchor text>

- url: <full download URL>
- from_page: <md_filename of the page where the link was found>
```

Include any link pointing to a downloadable file (PDF, DOCX, XLSX, ZIP, etc.). Do not include these in `sitemap.md`.

### Rules for Phase 1

- If the site appears to be a single-page application (SPA) — i.e. navigation does not load distinct URLs or all content lives on one page — stop immediately and inform the user. Do not proceed with Phase 2 or 3 until a plan is agreed upon.
- The root page must be included as the first entry.
- `md_filename` is a short snake_case filename (without `.md` extension) derived from the URL path, page title, or link name — whichever is most descriptive. Use `overview` for the root page.
- Discover pages by following navigation links (top nav, sidebar, footer). Also expand any dropdown/sub-menus.
- Scroll to the bottom of every page — some sites lazy-load navigation or content based on scroll position.
- Use best judgment about whether a page is worth including. Skip individual news/blog/event posts older than 8 years. Skip pagination, tag/category archive pages, and other low-value listing pages. Prefer pages with substantive school information.
- Ignore pages in a language other than Polish (e.g. English or Ukrainian versions).
- Do not follow external links (different domain).

---

## Phase 2 — Clean up `sitemap.md` and `documents.md`

Review the sitemap and remove duplicate entries:
- If two entries point to the same URL (after normalizing trailing slashes, query strings, and anchors), keep only one.
- If two entries would produce the same `md_filename`, disambiguate by appending a short suffix.

Also deduplicate `documents.md`: if the same download URL appears more than once (found from multiple pages), keep only one entry.

---

## Phase 3 — Scrape pages

Run the batch scraper script:

```
python3 scrapers/scrape_pages.py <folder_szkoły>
```

The script reads `data/sitemap.md`, fetches each pending page (skipping entries already marked `ok` or `skipped`), applies the `content_selector` CSS selector via BeautifulSoup to extract the main content area, writes `data/content/<md_filename>.md` with the standard header, and updates `status` and `scraped` in `data/sitemap.md` after each page.

**Dependencies:** `pip install requests beautifulsoup4 html2text`

---

## Phase 4 — Read selected documents

Review `data/documents.md` and identify which documents are likely to contain information that contributes to the school template. Read and extract content from those documents.

### Selection criteria

Read a document if it is likely to contain:
- Class profiles and extended subjects (e.g. *Oferta edukacyjna*, *Rekrutacja*)
- School programs with substantive detail (e.g. *Program wychowawczo-profilaktyczny*, *Program doradztwa zawodowego*, *Wewnątrzszkolny system doradztwa zawodowego*)

Skip documents that are primarily administrative or legal:
- RODO clauses, privacy notices, monitoring notices
- Student ID (*mLegitymacja*) forms
- Textbook lists (*Wykaz podręczników*)
- External exam communications from CKE (harmonogram, komunikat, przybory)
- Old yearbooks (*Roczniki szkolne*)
- Event-specific regulations (e.g. studniówka, wycieczki)
- Appendices and amendments to school bylaws

### For each selected document

1. Fetch the document URL and extract its textual content.
2. Choose a short snake_case filename (without `.md`) that describes the document, e.g. `oferta_edukacyjna_2024_2025`.
3. Write the extracted content to `data/content/<md_filename>.md` using the following header:

```
# <document title>

- url: <full document URL>
- document: <anchor text from documents.md>
- scraped: <ISO date>

---

<extracted content in Polish>
```

4. Add a `- content_file: <md_filename>` field to the corresponding entry in `data/documents.md`.

### Extracting PDFs with Node.js + pdfjs-dist

`pdfjs-dist` is available in the global npm installation (`/home/daniel/.nvm/versions/node/v24.14.0`). Use the **legacy** build for Node.js (the standard build requires DOM APIs):

```js
import * as pdfjsLib from '/tmp/node_modules/pdfjs-dist/legacy/build/pdf.mjs';
import { readFileSync } from 'fs';

async function extractPdf(pdfPath) {
  const data = new Uint8Array(readFileSync(pdfPath));
  const pdf = await pdfjsLib.getDocument({ data }).promise;
  let fullText = '';
  for (let i = 1; i <= pdf.numPages; i++) {
    const page = await pdf.getPage(i);
    const textContent = await page.getTextContent();
    let pageText = '';
    let lastY = null;
    for (const item of textContent.items) {
      if (lastY !== null && Math.abs(item.transform[5] - lastY) > 5) pageText += '\n';
      pageText += item.str;
      lastY = item.transform[5];
    }
    fullText += pageText.trim() + '\n\n';
  }
  return fullText.trim();
}
```

Install into `/tmp` with `cd /tmp && npm install pdfjs-dist` if not present. Download PDFs with `curl -s -o <dest> <url>`. Warnings about `standardFontDataUrl` are harmless — text is still extracted correctly.

### Rules for Phase 4

- Extract content faithfully — no summarization, no interpretation.
- All content must remain in Polish.
- If a document cannot be fetched or parsed (e.g. scanned PDF with no text layer), record `- content_file: błąd_odczytu` in `documents.md` and skip.

---

## Rules (all phases)

- All content must remain in Polish.
- No translation, summarization, or restructuring of the source content.
- No reasoning or classification — just the raw text.
