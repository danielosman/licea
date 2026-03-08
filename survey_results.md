# Survey Results — Dane ze swiadomiewybieram.pl

Ten dokument opisuje, jak agent powinien odczytać i zapisać dane z portalu swiadomiewybieram.pl dla danej szkoły.

---

## Cel

Dla każdej szkoły z listy `init/schools_swiadomiewybieram.md` odczytaj stronę szkoły na portalu i zapisz wynikowe dane do pliku `schools/{folder}/{folder}_survey.md`.

---

## Dane wejściowe

- URL szkoły: odczytaj z `init/schools_swiadomiewybieram.md` na podstawie nazwy folderu szkoły.
- Strona **wymaga zalogowania** — zakładamy, że przeglądarka jest już zalogowana (używaj playwriter z aktywną sesją Chrome).

---

## Kroki

### 1. Nawigacja

Przejdź na URL szkoły z `init/schools_swiadomiewybieram.md`. Poczekaj na załadowanie strony.

### 2. Odczytanie zawartości

Odczytaj tekst z elementu `div.pxp-content` (lub całej strony, jeśli ten selektor nie zadziała). Wszystkie metryki znajdują się w tej sekcji.

### 3. Ekstrakcja metryk

Odczytaj następujące wartości (jeśli dana wartość to „zbieramy dane", „brak danych" lub „nie dotyczy" — zapisz ją dosłownie):

**Nagłówek:**
- Pełna nazwa szkoły
- Adres (ulica, dzielnica)
- ANKIETY — liczba zebranych ankiet uczniowskich (np. `ANKIETY: 24`)
- MATURA — wynik procentowy (np. `84.1%`)
- ATMOSFERA — wynik procentowy
- PRZYJEMNOŚĆ NAUKI — wynik procentowy

**Szkoła od wewnątrz:**
- DOBRE RELACJE MIĘDZY UCZNIAMI — wynik procentowy
- DOBRA RELACJA UCZEŃ/NAUCZYCIEL — wynik procentowy
- NOWOCZESNOŚĆ PROWADZENIA ZAJĘĆ — wynik procentowy
- NA ILE UCZNIOWIE POLECAJĄ SZKOŁĘ — wynik procentowy
- JAKOŚĆ ODPOCZYNKU NA PRZERWIE — wynik procentowy
- ŚREDNI CZAS NAUKI PO LEKCJACH — czas (np. `1 godz 40 min`)
- ILU UCZNIÓW KORZYSTA Z KOREPETYCJI — wynik procentowy lub status
- ŚREDNIE WYDATKI NA KOREPETYCJE — kwota lub status

**Zaangażowanie:**
- LICZBA PROJEKTÓW W ZWOLNIENI Z TEORII — liczba lub status
- RANKING SZKÓŁ PRZYJAZNYCH LGBTQ+ — wartość lub status

**Liceum w liczbach:**
- LICZBA UCZNIÓW (2022) — liczba
- ROK ZAŁOŻENIA SZKOŁY — rok
- ZDAWALNOŚĆ MATUR — wynik procentowy

**Udogodnienia:**
- Lista udogodnień dostępnych w szkole (każda pozycja to osobny punktor)

### 4. Zapis wyniku

Zapisz dane do pliku `schools/{folder}/{folder}_survey.md` w formacie opisanym poniżej. Nie używaj tabel — tylko sekcje i punktorы.

---

## Format pliku wynikowego

```
# Dane z ankiet uczniowskich — {Pełna nazwa szkoły}

- źródło: {URL ze swiadomiewybieram.pl}
- scraped: {data ISO, np. 2026-03-08}
- ankiety: {liczba zebranych ankiet, np. 24}

## Ogólne wyniki

- MATURA: {wartość}
- ATMOSFERA: {wartość}
- PRZYJEMNOŚĆ NAUKI: {wartość}

## Szkoła od wewnątrz

- DOBRE RELACJE MIĘDZY UCZNIAMI: {wartość}
- DOBRA RELACJA UCZEŃ/NAUCZYCIEL: {wartość}
- NOWOCZESNOŚĆ PROWADZENIA ZAJĘĆ: {wartość}
- NA ILE UCZNIOWIE POLECAJĄ SZKOŁĘ: {wartość}
- JAKOŚĆ ODPOCZYNKU NA PRZERWIE: {wartość}
- ŚREDNI CZAS NAUKI PO LEKCJACH: {wartość}
- ILU UCZNIÓW KORZYSTA Z KOREPETYCJI: {wartość}
- ŚREDNIE WYDATKI NA KOREPETYCJE: {wartość}

## Zaangażowanie

- LICZBA PROJEKTÓW W ZWOLNIENI Z TEORII: {wartość}
- RANKING SZKÓŁ PRZYJAZNYCH LGBTQ+: {wartość}

## Liceum w liczbach

- LICZBA UCZNIÓW (2022): {wartość}
- ROK ZAŁOŻENIA SZKOŁY: {wartość}
- ZDAWALNOŚĆ MATUR: {wartość}

## Udogodnienia

- {udogodnienie 1}
- {udogodnienie 2}
- ...
```

---

## Uwagi

- Jeśli jakaś metryka nie istnieje na stronie (brak sekcji), pomiń ją w pliku.
- Wartości „zbieramy dane", „brak danych", „nie dotyczy" zapisuj dosłownie — nie interpretuj ich jako braku danych.
- Plik wynikowy zapisuj w języku polskim (nazwy metryk tak jak na portalu).
