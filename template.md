# Szablon — Poziom 1: Charakterystyka szkoły

Poniższy szablon służy do ujednoliconego opisu każdego liceum. Każda metryka oceniana jest w skali 1–5 (gdzie 5 = najwyższy poziom) lub opisowo, jeśli zaznaczono inaczej. Dane uzupełniane są na podstawie materiałów poziomu 0.

> **Uwaga dla agenta syntezy:** Opisy metryk pisane *kursywą* pod nagłówkami sekcji to wskazówki interpretacyjne dla agenta — **nie pojawiają się w pliku wynikowym.** W pliku wynikowym każda sekcja zawiera wyłącznie nagłówek (`###`) i pola z wartościami (`- **Pole:** ...`).

---

## Informacje podstawowe

- **Nazwa:** `{pełna nazwa szkoły}`
- **Numer:** `{numer porządkowy}`
- **Adres:** `{dzielnica, ulica}`
- **Strona internetowa:** `{URL}`

---

## Co szkoła mówi o sobie

`{2–5 zdań na podstawie materiałów własnych szkoły — co sama podkreśla jako swoje atuty, tradycje, misję lub wyróżniki}`

---

## Wyróżniki na tle innych szkół

*Sekcja do uzupełnienia po zebraniu danych o wszystkich szkołach.*

---

## Podsumowanie

`{2–4 zdania ogólnej charakterystyki szkoły na podstawie poniższych metryk}`

---

## Metryki

### Otwartość
*Czy szkoła jest otwarta na nowe inicjatywy, projekty zewnętrzne i współpracę z innymi instytucjami? Jak aktywnie zaprasza i angażuje środowisko? Wskaźniki: programy wymiany, Erasmus+, współpraca z uczelniami i organizacjami, goście zewnętrzni, dostępność nauczycieli, podejmowanie aktualnych tematów, adopcja nowych technologii.*

- **Ocena:** `{weighted_avg} ({synthesis_score})`
- **Erasmus+:** `[ tak | nie ]`
- **Współpraca zewnętrzna:** `{partnerzy instytucjonalni — uczelnie, firmy, NGO — lub „brak danych"}`
- **Goście i prelegenci:** `{opis lub „brak danych"}`
- **Dostępność nauczycieli:** `{konsultacje, dyżury, kontakt online — opis lub „brak danych"}`
- **Aktualne tematy:** `{czy szkoła porusza aktualne tematy globalne/społeczne — opis lub „brak danych"}`
- **Nowe technologie:** `{stosowanie technologii w dydaktyce — opis lub „brak danych"}`
- **Uzasadnienie:** `{krótki opis}`

---

### Przyjazność
*Czy atmosfera w szkole sprzyja uczniom — czy szkoła dba o relacje, dobre samopoczucie i poczucie bezpieczeństwa? Wskaźniki: psycholog/pedagog, programy wsparcia, proaktywny dobrostan psychiczny, akceptacja inności, polityka antybullyingowa, przestrzeń na wyrażanie opinii.*

- **Ocena:** `{weighted_avg} ({synthesis_score})`
- **Psycholog / pedagog:** `[ tak | nie ]`
- **Programy wsparcia:** `{opis lub „brak danych"}`
- **Dobrostan psychiczny:** `{proaktywne działania — warsztaty, dni zdrowia psychicznego itp. — lub „brak danych"}`
- **Akceptacja inności:** `{opis podejścia do różnorodności i integracji — lub „brak danych"}`
- **Przeciwdziałanie przemocy:** `{polityka antybullyingowa, procedury reagowania — lub „brak danych"}`
- **Wyrażanie opinii:** `{czy uczniowie mają przestrzeń na własne poglądy i krytykę — opis lub „brak danych"}`
- **Uzasadnienie:** `{krótki opis}`

---

### Zaangażowanie
*Na ile uczniowie i nauczyciele aktywnie uczestniczą w życiu szkoły — koła zainteresowań, samorząd, projekty, olimpiady, wolontariat i inne formy aktywności pozalekcyjnej. Uwaga na jakość zaangażowania: czy inicjatywy są oddolne czy odgórne, czy szkoła wspiera indywidualny rozwój pasji.*

- **Ocena:** `{weighted_avg} ({synthesis_score})`
- **Koła zainteresowań:** `{lista}`
- **Zajęcia nietypowe:** `{spoza standardowego programu liceum — biznes, AI, psychologia, prawo itp. — lub „brak danych"}`
- **Rozwój zainteresowań:** `{mentoring, projekty własne, programy pasji — opis lub „brak danych"}`
- **Wolontariat:** `{opis lub „brak danych"}`
- **Inicjatywy uczniowskie:** `{oddolne projekty zapoczątkowane przez uczniów — opis lub „brak danych"}`
- **Samorząd:** `{opis lub „brak danych"}`
- **Uzasadnienie:** `{krótki opis}`

---

### Języki
*Jakie języki obce są nauczane w szkole? Czy oferuje klasy dwujęzyczne lub certyfikaty? Kluczowe: czy języki są przypisane do klasy z góry, czy uczeń może je wybrać samodzielnie podczas nauki.*

- **Angielski:** `[ tak | nie ]`
- **Niemiecki:** `[ tak | nie ]`
- **Hiszpański:** `[ tak | nie ]`
- **Inne:** `{np. francuski, włoski, rosyjski — lub „brak"}`
- **Klasy dwujęzyczne:** `[ tak | nie ]` — `{język}`
- **Certyfikaty:** `{np. Cambridge, DELF — lub „brak"}`
- **Wybór języków:** `[ przypisane do klasy | wybór ucznia | model mieszany | brak danych ]` — `{szczegółowy opis}`
- **Grupy poziomowe:** `{czy uczniowie dzieleni wg poziomu zaawansowania — opis lub „brak danych"}`
- **Native speakerzy:** `{opis lub „brak danych"}`
- **Uwagi:** `{dodatkowe informacje}`

---

### Klasy (profile)
*Jakie profile kształcenia oferuje szkoła? Profile określają główny kierunek nauki w danej klasie, np. mat-fiz, biol-chem, humanistyczny, społeczny.*

- **Profile w ofercie:**
  - `{profil 1}` — `{rozszerzone przedmioty}`
  - `{profil 2}` — `{rozszerzone przedmioty}`
  - `{...}`
- **Uwagi:** `{np. klasy sportowe, artystyczne, IB}`

---

### Infrastruktura
*Jak wygląda baza materialna szkoły — budynek, stan sal, dostępność pracowni, biblioteka, aula, stołówka, szatnie i inne udogodnienia dla uczniów.*

- **Stołówka / sklepik:** `[ stołówka | sklepik | brak ]`
- **Biblioteka:** `[ tak | nie ]`
- **Aula / sala widowiskowa:** `[ tak | nie ]`
- **Gabinet pielęgniarki:** `[ tak | nie ]`
- **Pracownie specjalistyczne:** `{np. chemiczna, fizyczna, komputerowa, plastyczna}`
- **Stan techniczny budynku:** `[ bardzo dobry | dobry | przeciętny | wymaga remontu ]`
- **Uwagi:** `{dodatkowe informacje}`

---

### Sport
*Jakie możliwości sportowe oferuje szkoła — boiska, sale gimnastyczne, basen, sekcje sportowe, udział w rozgrywkach miejskich i ogólnopolskich.*

- **Boiska:** `{liczba, rodzaje, nawierzchnia — lub „brak"}`
- **Sale gimnastyczne:** `{liczba, rodzaje — lub „brak"}`
- **Siłownia / fitness:** `[ tak | nie ]`
- **Basen:** `[ tak | nie ]`
- **Dostęp poza lekcjami:** `{czy uczniowie mogą korzystać z obiektów poza WF — opis lub „brak danych"}`
- **Sekcje i koła sportowe:** `{np. piłka nożna, koszykówka, lekkoatletyka}`
- **Osiągnięcia sportowe:** `{np. mistrzostwo Warszawy w piłce nożnej 2023}`
- **Uwagi:** `{dodatkowe informacje}`

---

### Profil intelektualny
*Czy szkoła kładzie większy nacisk na nauki ścisłe czy humanistyczne? Ocena na podstawie: struktury profili klas (rozszerzone przedmioty), kół zainteresowań, olimpiad, projektów i języka materiałów promocyjnych.*

- **Humanistyczny:** `{weighted_avg}` ({synthesis_score})
- **Ścisły:** `{weighted_avg}` ({synthesis_score})
- **Profile klas — rozszerzone przedmioty:**
  - Ścisłe (matematyka, fizyka, chemia, informatyka, biologia): `{n klas}`
  - Humanistyczne (polski, historia, WOS, geografia, języki obce): `{n klas}`
- **Koła i zajęcia pozalekcyjne:**
  - Ścisłe: `{np. robotyka, programowanie, koło chemiczne}`
  - Humanistyczne: `{np. teatr, dziennikarstwo, debaty, koło historyczne}`
- **Olimpiady i konkursy:**
  - Ścisłe: `{np. Olimpiada Matematyczna, Fizyczna}`
  - Humanistyczne: `{np. Olimpiada Historyczna, Filozoficzna}`
- **Uzasadnienie:** `{krótki opis}`

---

### Światopogląd
*Przybliżona orientacja światopoglądowa szkoły, oszacowana na podstawie języka używanego w materiałach własnych. Nie jest to ocena wartościująca — służy wyłącznie charakterystyce środowiska szkolnego.*

- **Lewicowy:** `{weighted_avg}` ({synthesis_score})
- **Prawicowy:** `{weighted_avg}` ({synthesis_score})
- **Sygnały lewicowe (liczba wystąpień):**
  - `różnorodność` / `inkluzywność`: `{n}`
  - `mniejszości` / `równość` / `prawa człowieka`: `{n}`
  - `tolerancja` / `akceptacja`: `{n}`
  - `środowisko` / `ekologia` / `klimat`: `{n}`
- **Sygnały prawicowe (liczba wystąpień):**
  - `patriotyzm` / `ojczyzna` / `naród`: `{n}`
  - `obowiązek` / `dyscyplina` / `honor`: `{n}`
  - `tradycja` / `wartości` / `wiara`: `{n}`
  - `historia` / `bohaterowie` / `pamięć`: `{n}`
- **Uzasadnienie:** `{krótki opis na podstawie tonu i treści materiałów}`

---

### Równowaga szkolna
*Na ile szkoła skupia się na nauce i wynikach formalnych (egzaminy, rankingi, olimpiady przedmiotowe), a na ile zachęca uczniów do rozwijania własnych pasji, zainteresowań i inicjatyw? Wskaźniki: oferta kół i projektów uczniowskich, sposób komunikowania sukcesów przez szkołę, elastyczność i przestrzeń na działania z własnego pomysłu.*

- **Nauka:** `{weighted_avg}` ({synthesis_score})
- **Pasje:** `{weighted_avg}` ({synthesis_score})
- **Uzasadnienie:** `{krótki opis}`

---

### Innowacyjność
*Na ile szkoła wychodzi poza model tradycyjnego polskiego liceum? Czy wprowadza nowe rozwiązania dydaktyczne, reaguje na aktualne wyzwania i zainteresowania uczniów, podejmuje tematy istotne globalnie? Wskaźniki: tematyka zajęć pozalekcyjnych (tradycyjna i zachowawcza czy odpowiadająca współczesnym trendom), programy eksperymentalne, nowe inicjatywy, zmiany wprowadzone w ostatnich latach.*

- **Ocena:** `{weighted_avg} ({synthesis_score})`
- **Inicjatywy i zmiany:** `{opis nowych programów, inicjatyw lub zmian wprowadzonych w ostatnich latach — lub „brak danych"}`
- **Zajęcia pozalekcyjne — aktualność tematyki:** `{czy koła i projekty odpowiadają współczesnym trendom — opis}`
- **Uzasadnienie:** `{krótki opis}`

---

### Spójność przekazu
*Na ile szkoła rzeczywiście wierzy w to, co pisze o sobie? Metryka ocenia wewnętrzną zgodność materiałów własnych szkoły: czy deklarowane wartości i priorytety mają pokrycie w konkretnych przykładach, czy różne części witryny mówią tym samym głosem, i czy treści z jednego miejsca nie przeczą treściom z innego. Wysoki wynik oznacza przekaz spójny i wiarygodny — niski sygnalizuje puste hasła, przesadzone twierdzenia lub wyraźne sprzeczności między materiałami.*

- **Ocena:** `{weighted_avg} ({synthesis_score})`
- **Sprzeczności / puste hasła:** `{opis wykrytych niespójności lub „brak"}`
- **Uzasadnienie:** `{krótki opis}`

