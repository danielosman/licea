# Poziom 2 — Weryfikacja krzyżowa i porównanie szkół

Poziom 2 uzupełnia gotowe profile z poziomu 1 o perspektywę porównawczą. Agent czyta syntezy **wszystkich** szkół, które mają ukończony plik `{folder}.md`, a następnie dla każdej z nich:

1. Wypełnia sekcję **Wyróżniki na tle innych szkół**.
2. Dodaje do każdej ocenianej metryki nowy wynik — **ocenę po porównaniu** — odzwierciedlający pozycję szkoły na tle całej grupy.
3. Dopisuje do każdej metryki pole **Uzasadnienie po porównaniu**, wyjaśniające argumenty za zmianą lub utrzymaniem oceny.

**Reguła językowa:** cały nowy tekst musi być w języku polskim. Nazwy technicznych pól (np. `cross_score`) są wyjątkiem.

---

## Dane wejściowe

- Pliki: `schools/{folder}/{folder}.md` dla każdej szkoły z ukończonym profilem poziomu 1.
- Tylko szkoły z wypełnionym plikiem syntezy są brane pod uwagę. Szkoły bez pliku `{folder}.md` są pomijane w tym kroku.

---

## Faza 0 — Przegląd wszystkich syntez

Przed jakimikolwiek modyfikacjami agent musi przeczytać **wszystkie** pliki `{folder}.md` w katalogu `schools/`. Celem jest zbudowanie obrazu rozkładu wyników i wyróżników w całej grupie.

Podczas lektury agent sporządza w pamięci roboczą tabelę ocen dla każdej metryki i każdej szkoły (patrz format poniżej), a także notuje cechy wyróżniające poszczególne szkoły.

**Metryki podlegające porównaniu** (te, które mają `synthesis_score` w pliku Level 1):

| Metryka | Pole w pliku |
|---|---|
| Otwartość | `Ocena` (unipolar) |
| Przyjazność | `Ocena` (unipolar) |
| Zaangażowanie | `Ocena` (unipolar) |
| Innowacyjność | `Ocena` (unipolar) |
| Spójność przekazu | `Ocena` (unipolar) |
| Profil intelektualny — humanistyczny | `Humanistyczny` (bipolar) |
| Profil intelektualny — ścisły | `Ścisły` (bipolar) |
| Światopogląd — lewicowy | `Lewicowy` (bipolar) |
| Światopogląd — prawicowy | `Prawicowy` (bipolar) |
| Równowaga — nauka | `Nauka` (bipolar) |
| Równowaga — pasje | `Pasje` (bipolar) |

Dla każdej metryki agent odczytuje `synthesis_score` (liczba w nawiasie okrągłym) z pliku Level 1 i buduje ranking szkół.

**Uwaga:** ocena po porównaniu to niezależna liczba całkowita (1–5). Nie jest średnią — jest wynikiem holostycznego sądu agenta po lekturze wszystkich profili, z intencją lepszego rozróżnienia szkół na skali niż w izolowanej ocenie z poziomu 1. Skala powinna być faktycznie używana w pełnym zakresie (1–5): jeśli jest wyraźny lider, powinien dostać 5; jeśli jest wyraźny słabeusz, powinien dostać 1.

---

## Faza 1 — Aktualizacja plików szkół

Po przeczytaniu wszystkich syntez agent przetwarza szkoły **jedna po drugiej** i aktualizuje każdy plik `{folder}.md`. Każda aktualizacja obejmuje dwa rodzaje zmian.

### Zmiana A — Sekcja „Wyróżniki na tle innych szkół"

Zastąp dotychczasowy placeholder:

```markdown
*Sekcja do uzupełnienia po zebraniu danych o wszystkich szkołach.*
```

treścią opisową w formie 3–6 punktorów. Każdy punktor wskazuje na jeden konkretny wyróżnik szkoły — cechę, która odróżnia ją od pozostałych liceów w zbiorze. Wyróżniki mogą być pozytywne, negatywne lub neutralne (fakty, a nie oceny). Przykłady kategorii wyróżników:

- unikalna oferta klas lub języków
- szczególnie wysoka lub niska ocena w konkretnej metryce na tle grupy
- unikalna inicjatywa, projekt lub partnerstwo
- wyraźny profil ideowy lub światopoglądowy nieobecny u innych
- szczególna infrastruktura lub brak, który wyróżnia szkołę in minus

Jeśli szkoła nie ma wyróżników godnych uwagi, wpisz: `*Brak wyraźnych wyróżników na tle zebranej grupy szkół.*`

**Format wyjściowy:**

```markdown
## Wyróżniki na tle innych szkół

- {wyróżnik 1}
- {wyróżnik 2}
- {wyróżnik 3}
- {opcjonalnie dalsze}
```

### Zmiana B — Ocena po porównaniu dla każdej metryki

Dla każdej metryki z listy w Fazie 0 agent dodaje pole `cross_score` i pole `Uzasadnienie po porównaniu` bezpośrednio pod istniejącą linią `Ocena` (lub `Humanistyczny`/`Ścisły`/`Lewicowy`/`Prawicowy`/`Nauka`/`Pasje`).

**Format dla metryk unipolarnych** (Otwartość, Przyjazność, Zaangażowanie, Innowacyjność, Spójność przekazu):

Linia `Ocena` pozostaje bez zmian. Nowe pola wstawiamy bezpośrednio pod nią:

```markdown
- **Ocena:** `{weighted_avg} ({synthesis_score})`
- **Ocena po porównaniu:** `{cross_score}`
- **Uzasadnienie po porównaniu:** `{krótki opis — dlaczego ocena wzrosła/spadła/pozostała bez zmian na tle innych szkół}`
```

**Format dla metryk bipolarnych** (Profil intelektualny, Światopogląd, Równowaga szkolna):

Każde pole biegunowe otrzymuje własną ocenę po porównaniu. Nowe pola wstawiamy za odpowiadającą im linią:

```markdown
- **Humanistyczny:** `{weighted_avg}` ({synthesis_score})
- **Humanistyczny po porównaniu:** `{cross_score}`
- **Ścisły:** `{weighted_avg}` ({synthesis_score})
- **Ścisły po porównaniu:** `{cross_score}`
- **Uzasadnienie po porównaniu:** `{krótki opis dla obu biegunów}`
```

(Analogicznie dla Lewicowy/Prawicowy i Nauka/Pasje.)

---

## Zasady oceniania po porównaniu

1. **Rozkład ocen:** dąż do faktycznego zróżnicowania. Jeśli wszystkie szkoły dostały `synthesis_score = 3` w izolacji, po porównaniu część powinna dostać 2 lub 4, jeśli dane to uzasadniają.

2. **Uzasadnienie jest obowiązkowe.** Każde pole `Uzasadnienie po porównaniu` musi zawierać przynajmniej jedno konkretne odniesienie do innej szkoły lub do rozkładu grupy — np. „Na tle grupy Śniadek wyróżnia się jako jedyna szkoła z explicite deklaracją LGBTQ+, co uzasadnia podniesienie oceny Przyjazności do 5." lub „Ocena pozostaje bez zmian — szkoła plasuje się w środku stawki bez wyraźnych cech odróżniających."

3. **Nie zmieniaj synthesis_score ani weighted_avg.** Linia `Ocena: {weighted_avg} ({synthesis_score})` jest nienaruszalna — pochodzi z poziomu 1 i nie jest modyfikowana na poziomie 2.

4. **Neutralność metryki Światopogląd:** ocena po porównaniu dla Lewicowy/Prawicowy nie jest oceną wartościującą — wyższy wynik oznacza silniejszy sygnał w danym kierunku, nie lepszą lub gorszą szkołę.

5. **Liczba szkół w grupie:** uzasadnienie może odnosić się do „n szkół w grupie" lub do konkretnych nazw szkół. Im mniejsza grupa, tym większa ostrożność przy radykalnych korektach — przy 2–3 szkołach porównanie ma mniejszą wartość statystyczną.

---

## Format uzasadnienia po porównaniu

Uzasadnienie powinno być zwięzłe (1–3 zdania) i zawierać:

- Pozycję szkoły w rankingu grupy dla tej metryki (np. „najlepsza w grupie", „poniżej średniej grupy", „w środku stawki").
- Konkretny argument za zmianą lub utrzymaniem oceny (co ta szkoła robi lepiej/gorzej niż inne).
- Opcjonalnie: nazwę innej szkoły jako punkt odniesienia, jeśli to klaruje argumentację.

---

## Weryfikacja po zakończeniu

Po zaktualizowaniu wszystkich plików agent sprawdza:

- [ ] Sekcja `Wyróżniki na tle innych szkół` jest wypełniona (nie zawiera placeholder) w każdym zaktualizowanym pliku.
- [ ] Każda metryka z listy w Fazie 0 ma pole `Ocena po porównaniu` (lub odpowiednik dla bipolarnych) i `Uzasadnienie po porównaniu`.
- [ ] Oryginalne linie `Ocena`, `weighted_avg` i `synthesis_score` pozostają niezmienione.
- [ ] Uzasadnienia są w języku polskim i zawierają odniesienie do grupy lub konkretnej szkoły.
- [ ] Oceny po porównaniu mieszczą się w skali 1–5.
- [ ] Rozkład `cross_score` dla każdej metryki nie jest jednostajny (chyba że szkoły są rzeczywiście nieodróżnialne w danym wymiarze — wtedy należy to odnotować).
