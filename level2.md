# Poziom 2 — Weryfikacja krzyżowa i porównanie szkół

Poziom 2 uzupełnia gotowe profile z poziomu 1 o perspektywę porównawczą. Agent czyta syntezy **wszystkich** szkół, które mają ukończony plik `{folder}.md`, a następnie dla każdej z nich:

1. Wypełnia sekcję **Wyróżniki na tle innych szkół**.
2. Dodaje do każdej metryki z oceną numeryczną pola **Ocena po porównaniu** i **Uzasadnienie po porównaniu**.
3. Dodaje do każdej metryki bez oceny numerycznej pole **W porównaniu z innymi**.

**Reguła językowa:** cały nowy tekst musi być w języku polskim. Nazwy technicznych pól (np. `cross_score`) są wyjątkiem.

---

## Dane wejściowe

Pliki `schools/{folder}/{folder}.md` dla każdej szkoły z ukończonym profilem poziomu 1. Aby je odnaleźć, użyj wzorca `schools/*/*.md`, gdzie nazwa pliku jest identyczna z nazwą folderu nadrzędnego (np. `schools/15_Zmichowska/15_Zmichowska.md`). Szkoły bez takiego pliku są pomijane.

---

## Faza 0 — Przegląd wszystkich syntez

Przed jakimikolwiek modyfikacjami agent musi przeczytać **wszystkie** pliki `{folder}.md` w katalogu `schools/`. Celem jest zbudowanie obrazu rozkładu wyników i wyróżników w całej grupie.

Podczas lektury agent sporządza w pamięci roboczą tabelę ocen dla każdej metryki i każdej szkoły, a także notuje cechy wyróżniające poszczególne szkoły.

**Metryki podlegające porównaniu** — pełna lista w kolejności z `template.md`:

Metryki z oceną numeryczną (mają `synthesis_score` — agent odczytuje tę wartość i buduje ranking szkół):

- Otwartość — pole `Ocena` (unipolar)
- Przyjazność — pole `Ocena` (unipolar)
- Zaangażowanie — pole `Ocena` (unipolar)
- Profil intelektualny — pola `Humanistyczny`, `Ścisły` (bipolar)
- Światopogląd — pola `Lewicowy`, `Prawicowy` (bipolar)
- Równowaga szkolna — pola `Nauka`, `Pasje` (bipolar)
- Innowacyjność — pole `Ocena` (unipolar)
- Spójność przekazu — pole `Ocena` (unipolar)

Metryki bez oceny numerycznej (agent nie buduje rankingu, lecz porównuje opisowo):

- Języki
- Klasy (profile)
- Infrastruktura
- Sport

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

### Zmiana B — Pola porównawcze dla każdej metryki

Nowe pola wstawiamy **na końcu każdej sekcji metryki, bezpośrednio przed `---`** (po istniejącym polu `Uzasadnienie` lub innym ostatnim polu sekcji).

**Format dla metryk unipolarnych** (Otwartość, Przyjazność, Zaangażowanie, Innowacyjność, Spójność przekazu):

```markdown
- **Uzasadnienie:** `{istniejący tekst — bez zmian}`
- **Ocena po porównaniu:** `{cross_score}`
- **Uzasadnienie po porównaniu:** `{krótki opis — dlaczego ocena wzrosła/spadła/pozostała bez zmian na tle innych szkół}`
```

**Format dla metryk bipolarnych** (Profil intelektualny, Światopogląd, Równowaga szkolna):

Każdy biegun otrzymuje własną ocenę i własne uzasadnienie po porównaniu:

```markdown
- **Uzasadnienie:** `{istniejący tekst — bez zmian}`
- **Humanistyczny po porównaniu:** `{cross_score}`
- **Humanistyczny — uzasadnienie po porównaniu:** `{opis}`
- **Ścisły po porównaniu:** `{cross_score}`
- **Ścisły — uzasadnienie po porównaniu:** `{opis}`
```

(Analogicznie dla Lewicowy/Prawicowy i Nauka/Pasje.)

**Format dla metryk bez oceny numerycznej** (Języki, Klasy, Infrastruktura, Sport):

```markdown
- **Uwagi:** `{istniejący tekst — bez zmian}`
- **W porównaniu z innymi:** `{krótka notatka — co wyróżnia szkołę na tle grupy w tej metryce}`
```

Jeśli nic szczególnego się nie wyróżnia, wpisz: `Na tle grupy bez wyraźnych wyróżników.`

Przykłady:
- `Brak gabinetu pielęgniarki wyróżnia się negatywnie — wszystkie pozostałe szkoły w grupie go posiadają.`
- `Jako jedyna szkoła w grupie oferuje język japoński — wyraźny wyróżnik oferty językowej.`
- `Na tle grupy bez wyraźnych wyróżników.`

---

## Zasady oceniania i uzasadnienia po porównaniu

1. **`cross_score` to niezależna liczba całkowita (1–5), nie średnia.** Jest wynikiem holistycznego sądu agenta po lekturze wszystkich profili, z intencją lepszego rozróżnienia szkół niż w izolowanej ocenie z poziomu 1. Skala powinna być faktycznie używana w pełnym zakresie: jeśli jest wyraźny lider, powinien dostać 5; jeśli wyraźny słabeusz — 1.

2. **Rozkład ocen:** dąż do faktycznego zróżnicowania. Jeśli wszystkie szkoły dostały `synthesis_score = 3` w izolacji, po porównaniu część powinna dostać 2 lub 4, jeśli dane to uzasadniają.

3. **Uzasadnienie jest obowiązkowe.** Każde pole uzasadnienia musi zawierać przynajmniej jedno konkretne odniesienie do innej szkoły lub do rozkładu grupy — np. „Na tle grupy Śniadek wyróżnia się jako jedyna szkoła z explicite deklaracją LGBTQ+, co uzasadnia podniesienie oceny Przyjazności do 5." lub „Ocena pozostaje bez zmian — szkoła plasuje się w środku stawki bez wyraźnych cech odróżniających."

4. **Forma uzasadnienia:** zwięzłe 1–3 zdania zawierające pozycję szkoły w rankingu grupy (np. „najlepsza w grupie", „poniżej średniej grupy", „w środku stawki") oraz konkretny argument za zmianą lub utrzymaniem oceny. Opcjonalnie: nazwa innej szkoły jako punkt odniesienia.

5. **Nie zmieniaj `synthesis_score` ani `weighted_avg`.** Linia `Ocena: {weighted_avg} ({synthesis_score})` jest nienaruszalna — pochodzi z poziomu 1 i nie jest modyfikowana na poziomie 2.

6. **Neutralność metryki Światopogląd:** `cross_score` dla Lewicowy/Prawicowy nie jest oceną wartościującą — wyższy wynik oznacza silniejszy sygnał w danym kierunku, nie lepszą lub gorszą szkołę.

7. **Liczba szkół w grupie:** im mniejsza grupa, tym większa ostrożność przy radykalnych korektach — przy 2–3 szkołach porównanie ma mniejszą wartość statystyczną.

---

## Weryfikacja po zakończeniu

Po zaktualizowaniu wszystkich plików agent sprawdza:

- [ ] Sekcja `Wyróżniki na tle innych szkół` nie zawiera placeholdera w żadnym zaktualizowanym pliku.
- [ ] Każda metryka numeryczna ma pola `Ocena po porównaniu` i `Uzasadnienie po porównaniu` (dla bipolarnych — oddzielnie dla każdego bieguna).
- [ ] Każda metryka bez oceny numerycznej (Języki, Klasy, Infrastruktura, Sport) ma pole `W porównaniu z innymi`.
- [ ] Oryginalne linie `Ocena`, `weighted_avg` i `synthesis_score` pozostają niezmienione.
- [ ] Rozkład `cross_score` dla każdej metryki nie jest jednostajny (chyba że szkoły są rzeczywiście nieodróżnialne — wtedy należy to odnotować w uzasadnieniu).
