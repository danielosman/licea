#!/usr/bin/env python3
"""
scrape_pages.py — Faza 3: masowe pobieranie stron z sitemap.md

Użycie:
    python scrapers/scrape_pages.py <folder_szkoły>

Przykład:
    python scrapers/scrape_pages.py 15_Zmichowska

Skrypt:
  - Parsuje schools/<folder>/data/sitemap.md
  - Pomija wpisy ze statusem 'ok' lub 'skipped'
  - Dla pozostałych: pobiera stronę, stosuje content_selector (CSS),
    zapisuje wynik do data/content/<md_filename>.md jako markdown
  - Aktualizuje pola 'status' i 'scraped' w sitemap.md po każdym pobraniu

Zależności: requests, beautifulsoup4, html2text
    pip install requests beautifulsoup4 html2text
"""

import re
import sys
import time
from datetime import date
from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup

# ---------------------------------------------------------------------------
# Konfiguracja
# ---------------------------------------------------------------------------
TIMEOUT = 15   # sekundy
DELAY   = 1.0  # przerwa między żądaniami (grzeczność wobec serwera)
HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; licea-scraper/1.0; +https://github.com/licea)"
}


# ---------------------------------------------------------------------------
# Parsowanie sitemap.md
# ---------------------------------------------------------------------------
def parse_sitemap(sitemap_path: Path) -> list[dict]:
    """
    Zwraca listę wpisów stron z sitemap.md.
    Sekcja '## Documents' i wszystko po niej jest ignorowane.
    """
    text = sitemap_path.read_text(encoding="utf-8")
    entries = []

    # Dziel na bloki zaczynające się od "## "
    blocks = re.split(r'\n(?=## )', "\n" + text)

    for block in blocks:
        lines = block.strip().splitlines()
        if not lines:
            continue
        header = lines[0]
        if not header.startswith("## "):
            continue
        section_name = header[3:].strip()
        if section_name.lower() == "documents":
            break  # reszta pliku to tabela dokumentów

        entry = {"md_filename": section_name}
        for line in lines[1:]:
            m = re.match(r"-\s+(\w+):\s+(.*)", line.strip())
            if m:
                entry[m.group(1)] = m.group(2).strip()
        entries.append(entry)

    return entries


# ---------------------------------------------------------------------------
# Ekstrakcja treści
# ---------------------------------------------------------------------------
def extract_content(html: str, selector: str) -> str:
    """
    Wyodrębnia treść z obszaru wskazanego selektorem CSS i konwertuje do markdown.
    Jeśli selektor nie pasuje lub jest pusty, wraca do pełnej treści strony.
    """
    soup = BeautifulSoup(html, "html.parser")
    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    if selector and selector not in ("-", ""):
        area = soup.select_one(selector)
        if not area:
            print(f"    uwaga: selektor '{selector}' nie pasuje, używam pełnej treści")
    else:
        area = None

    target_html = str(area) if area else str(soup)

    h = html2text.HTML2Text()
    h.body_width  = 0      # bez zawijania linii
    h.ignore_images = True
    h.unicode_snob  = True # poprawna obsługa polskich znaków
    return h.handle(target_html).strip()


def get_page_title(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    tag = soup.find("title")
    return tag.get_text(strip=True) if tag else ""


# ---------------------------------------------------------------------------
# Aktualizacja sitemap.md
# ---------------------------------------------------------------------------
def update_sitemap_entry(sitemap_path: Path, md_filename: str,
                         status: str, scraped: str) -> None:
    """Nadpisuje pola 'status' i 'scraped' dla danego wpisu w sitemap.md."""
    text = sitemap_path.read_text(encoding="utf-8")

    # Podziel na bloki po nagłówkach "## "
    blocks = re.split(r'\n(?=## )', "\n" + text)
    updated = []

    for block in blocks:
        lines = block.strip().splitlines()
        if lines and lines[0] == f"## {md_filename}":
            block = re.sub(r"(- status:\s*).*", rf"\g<1>{status}", block)
            block = re.sub(r"(- scraped:\s*).*", rf"\g<1>{scraped}", block)
        updated.append(block)

    sitemap_path.write_text("\n".join(updated).lstrip("\n"), encoding="utf-8")


# ---------------------------------------------------------------------------
# Pobieranie jednej strony
# ---------------------------------------------------------------------------
def scrape_entry(entry: dict, raw_data_dir: Path, sitemap_path: Path) -> None:
    md_filename  = entry.get("md_filename", "")
    url          = entry.get("url", "")
    selector     = entry.get("content_selector", "")
    status_now   = entry.get("status", "")
    title        = entry.get("title", "")

    if status_now in ("ok", "skipped"):
        print(f"  pominięto ({status_now}): {md_filename}")
        return

    output_path = raw_data_dir / f"{md_filename}.md"
    today = date.today().isoformat()

    print(f"  pobieranie: {md_filename}  [{url}]")
    try:
        resp = requests.get(url, headers=HEADERS, timeout=TIMEOUT)
        resp.raise_for_status()
        resp.encoding = resp.apparent_encoding  # poprawne dekodowanie polskich znaków

        content = extract_content(resp.text, selector)

        # Użyj tytułu ze strony jeśli sitemap go nie zawiera
        if not title or title == "BRAK_DANYCH":
            title = get_page_title(resp.text)

        file_content = (
            f"---\n"
            f"url: {url}\n"
            f"scraped: {today}\n"
            f"title: {title}\n"
            f"---\n\n"
            f"{content}\n"
        )
        output_path.write_text(file_content, encoding="utf-8")
        update_sitemap_entry(sitemap_path, md_filename, "ok", today)
        print(f"    ok — zapisano {output_path.name}")

    except requests.HTTPError as e:
        reason = f"HTTP {e.response.status_code}"
        update_sitemap_entry(sitemap_path, md_filename, f"error ({reason})", today)
        print(f"    błąd: {reason}")

    except requests.RequestException as e:
        reason = str(e)[:80]
        update_sitemap_entry(sitemap_path, md_filename, f"error ({reason})", today)
        print(f"    błąd: {reason}")

    time.sleep(DELAY)


# ---------------------------------------------------------------------------
# Punkt wejścia
# ---------------------------------------------------------------------------
def main():
    if len(sys.argv) != 2:
        print("Użycie: python scrapers/scrape_pages.py <folder_szkoły>")
        print("Przykład: python scrapers/scrape_pages.py 15_Zmichowska")
        sys.exit(1)

    folder_name  = sys.argv[1]
    base_dir     = Path(__file__).parent.parent
    data_dir     = base_dir / "schools" / folder_name / "data"
    content_dir  = data_dir / "content"
    sitemap_path = data_dir / "sitemap.md"

    if not sitemap_path.exists():
        print(f"Błąd: nie znaleziono {sitemap_path}")
        sys.exit(1)

    content_dir.mkdir(parents=True, exist_ok=True)

    entries = parse_sitemap(sitemap_path)
    pending = [e for e in entries if e.get("status") not in ("ok", "skipped")]
    print(f"Znaleziono {len(entries)} wpisów, do pobrania: {len(pending)}")

    for entry in entries:
        scrape_entry(entry, content_dir, sitemap_path)

    print("Gotowe.")


if __name__ == "__main__":
    main()
