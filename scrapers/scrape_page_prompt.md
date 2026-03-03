# Faza 3 — Szablon promptu dla sub-agenta

Użyj tego szablonu dla każdego sub-agenta haiku uruchamianego w fazie 3. Uzupełnij
symbole zastępcze (w `<nawiasach ostrych>`) z wpisu w sitemapie przed wysłaniem.

---

Scrapujesz jedną stronę z witryny polskiego liceum. Twoim jedynym zadaniem jest
pobranie strony i zapisanie jej treści do pliku. Nie czytaj ani nie modyfikuj
`sitemap.md`.

**Szczegóły strony:**
- URL: `<url>`
- Plik wyjściowy: `<raw_data_path>/<md_filename>.md`
- Selektor treści: `<content_selector>`
- Dzisiejsza data: `<data ISO>`

**Kroki:**
1. Użyj narzędzia **WebFetch**, aby pobrać URL. Użyj dokładnie tego promptu dla WebFetch:
   > „Wyodrębnij całą zawartość tekstową z obszaru `<content_selector>` dosłownie. Nie streszczaj, nie tłumacz ani nie restrukturyzuj niczego. Zachowaj wszystkie polskie teksty dokładnie tak, jak są napisane. Jeśli selektor nic nie dopasowuje lub zwraca wyraźnie niepełną treść, wyodrębnij zamiast tego pełną zawartość strony — preferuj więcej treści niż mniej."
2. Zapisz plik wyjściowy z nagłówkiem, a następnie wyodrębnioną treścią:

```
---
url: <url>
scraped: <data ISO>
title: <tytuł strony tak jak pojawia się na stronie>
---
```

   Następnie dołącz wyodrębniony tekst dosłownie poniżej nagłówka.

3. Po zakończeniu odpowiedz pojedynczym obiektem JSON (bez żadnego innego tekstu):
   - W przypadku sukcesu: `{"status": "ok", "title": "<tytuł strony>"}`
   - W przypadku błędu (404, timeout, ściana logowania itp.): `{"status": "error", "reason": "<krótki opis>"}`

**Zasady:**
- **Cały wynik musi być po polsku** — nie tłumacz niczego, włącznie z polem `title` w nagłówku pliku i w odpowiedzi JSON.
- Bez streszczania, normalizacji ani restrukturyzacji — zachowaj tekst źródłowy dokładnie tak, jak jest.
- Nie podążaj za żadnymi linkami ani nie odwiedzaj innych stron.
- Nie czytaj ani nie modyfikuj `sitemap.md`.
