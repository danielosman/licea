# Level 1 — Structured Data Processing

Level 1 transforms the raw scraped files in `data/content/` into a single normalized school profile following `template.md`. All input must come exclusively from `data/content/` files — no internet access, no guessing.

**Language rule: all output must be in Polish.** Every field value, narrative, justification, and free-text entry written by any agent (reader agents and the synthesis agent) must be in Polish. Do not produce any English text in output files.

Processing is done in three phases. Intermediate agent outputs are written to disk so that synthesis can be re-run without re-launching reader agents, and so individual agent files can be inspected or corrected independently.

---

## Phase 0 — Build the agent mapping file

Before launching any reader agent, read the school's `data/content/` directory and produce a mapping file that assigns every content file to exactly one reader agent.

**Output:** `schools/{folder_name}/{folder_name}_agent_mapping.md`

**How to build the mapping:**

1. List all `.md` files by reading the `data/content/` directory directly. Do not derive the file list from `sitemap.md` — that index only covers HTML pages and does not include document extracts added in Level 0 Phase 4. Every file present in `data/content/` is a content file and must appear in the mapping.
2. Skim each file briefly to assess its thematic content and substantive value.
3. Mark files with zero substantive content (legal boilerplate, blank pages, single-line notices) as **Pominięte**.
4. Assign the remaining files to 5 agents, aiming for 12–16 files per agent, grouped thematically:
   - **Agent A** — school identity: overview, mission, history, patron, experimental model, rankings, contact
   - **Agent B** — teaching: recruitment/class profiles, extracurricular clubs, graduation exams, individual curriculum, educational programs, vocational guidance, timetables, teachers, awards
   - **Agent C** — achievements and exchanges: olympiad participation, competition results, international exchanges, creative projects, news items
   - **Agent D** — school life: student council, flagship events (e.g. SOFA/WicFest), gallery, school life pages, prevention programs, student handbook
   - **Agent E** — infrastructure and support: cafeteria, library, nurse's office, cloakroom, psychological support, tutors, parents' council, association, financial aid, insurance
5. If a file does not fit cleanly, assign it to the agent whose theme is closest.

**Mapping file format:**

```markdown
# {folder_name} — Agent mapping
# Generated: {ISO date}
# Total content files: {n}

## Agent A — Tożsamość ({n} files)
file1.md
file2.md
...

## Agent B — Nauczanie ({n} files)
file1.md
...

## Agent C — Osiągnięcia i wymiany ({n} files)
...

## Agent D — Życie szkolne ({n} files)
...

## Agent E — Infrastruktura i wsparcie ({n} files)
...

## Pominięte ({n} files — zero substantive content)
rodo.md
klauzula_informacyjna.md
...
```

**Stop after writing the mapping file.** Present it to the user for review. Only proceed to Phase 1 once the mapping is approved (explicitly or implicitly by the user asking to continue).

---

## Phase 1–5 — Reader agents

Launch one **sonnet 4.6 sub-agent per agent** (A through E), sequentially — wait for each to finish before launching the next. Pass each agent:
- The list of files from its row in the mapping file
- The output file path it must write to
- The section block output format (see below)

Each agent reads all its assigned files and **writes** a file `schools/{folder_name}/{folder_name}_Agent_{letter}.md` containing **all 12 section blocks**, regardless of thematic focus. Every field must be filled — either with extracted content or with `BRAK_DANYCH`.

The agent is responsible for writing this file itself. The main agent must not write it on the agent's behalf.

### Section block output format

```
## SEKCJA 1: Informacje podstawowe
- nazwa: {pełna nazwa szkoły}
- numer: {numer}
- adres: {ulica, dzielnica}
- url: {strona internetowa}
- Źródła: {lista plików}

## SEKCJA 2: Co szkoła mówi o sobie
- kluczowe_sformulowania: {cytaty lub parafrazy kluczowych zdań z materiałów własnych}
- podkreślane_atuty: {lista atutów}
- Źródła: {lista plików}

## SEKCJA 3: Otwartość
- Erasmus+_tak_nie: {tak|nie|BRAK_DANYCH}
- dowody_erasmus: {opis lub BRAK_DANYCH}
- wymiany_zagraniczne: {opis lub BRAK_DANYCH}
- wspolpraca_zewnetrzna: {opis partnerów — uczelnie, firmy, NGO, instytucje kultury — lub BRAK_DANYCH}
- goście_prelegenci: {czy szkoła zaprasza zewnętrznych ekspertów, naukowców, artystów — opis lub BRAK_DANYCH}
- dostepnosc_nauczycieli: {czy nauczyciele oferują konsultacje, dyżury, kontakt online — opis lub BRAK_DANYCH}
- podejmowanie_aktualnych_tematow: {czy szkoła porusza aktualne tematy globalne lub społeczne na zajęciach lub wydarzeniach — opis lub BRAK_DANYCH}
- adopcja_nowych_technologii: {czy szkoła stosuje nowoczesne technologie w dydaktyce (e-learning, AI, platformy cyfrowe itp.) — opis lub BRAK_DANYCH}
- inne_sygnaly: {opis lub BRAK_DANYCH}
- propozycja_oceny: {1-5}
- uzasadnienie: {krótki opis}
- Źródła: {lista plików}

## SEKCJA 4: Przyjazność
- psycholog_pedagog: {tak|nie|BRAK_DANYCH}
- programy_wsparcia: {opis reaktywnych programów wsparcia — lub BRAK_DANYCH}
- dobrostan_psychiczny: {proaktywne działania na rzecz dobrostanu — warsztaty, dni zdrowia psychicznego, mindfulness itp. — opis lub BRAK_DANYCH}
- pomoc_finansowa: {opis lub BRAK_DANYCH}
- akceptacja_innosci: {opis podejścia szkoły do różnorodności, integracji uczniów o różnych potrzebach lub tożsamościach — opis lub BRAK_DANYCH}
- przeciwdzialanie_przemocy: {polityka antybullyingowa, procedury reagowania na przemoc i agresję — opis lub BRAK_DANYCH}
- wyrazanie_opinii: {czy uczniowie mają przestrzeń do wyrażania własnych poglądów i krytyki — opis lub BRAK_DANYCH}
- propozycja_oceny: {1-5}
- uzasadnienie: {krótki opis}
- Źródła: {lista plików}

## SEKCJA 5: Zaangażowanie
- kola: {pełna lista kół zainteresowań lub BRAK_DANYCH}
- zajecia_nietypowe: {zajęcia i programy spoza typowego programu polskiego liceum — biznes, ekonomia, AI, psychologia, prawo, przedsiębiorczość itp. — opis lub BRAK_DANYCH}
- rozwoj_zainteresowan: {czy szkoła ma konkretne mechanizmy wspierania indywidualnych zainteresowań — mentoring, projekty własne, programy „pasji" itp. — opis lub BRAK_DANYCH}
- wolontariat: {opis działalności wolontariackiej i społecznej — lub BRAK_DANYCH}
- inicjatywy_uczniowskie: {projekty i inicjatywy zapoczątkowane przez samych uczniów (oddolne) — opis lub BRAK_DANYCH}
- samorzad: {opis lub BRAK_DANYCH}
- olimpiady_konkursy: {opis lub BRAK_DANYCH}
- projekty_events: {opis lub BRAK_DANYCH}
- propozycja_oceny: {1-5}
- uzasadnienie: {krótki opis}
- Źródła: {lista plików}

## SEKCJA 6: Języki
- angielski: {tak|nie|BRAK_DANYCH}
- niemiecki: {tak|nie|BRAK_DANYCH}
- francuski: {tak|nie|BRAK_DANYCH}
- hiszpanski: {tak|nie|BRAK_DANYCH}
- inne: {lista lub BRAK_DANYCH}
- klasy_dwujezyczne: {tak|nie|BRAK_DANYCH}
- certyfikaty: {lista lub BRAK_DANYCH}
- wybor_jezykow: {czy języki są z góry przypisane do klasy, wybierane przez ucznia, czy model mieszany — opisz dokładnie jak to działa lub BRAK_DANYCH}
- grupy_poziomowe: {czy uczniowie są dzieleni na grupy według poziomu zaawansowania językowego — opis lub BRAK_DANYCH}
- native_speakers: {czy szkoła zatrudnia native speakerów lub oferuje zajęcia konwersacyjne z nimi — opis lub BRAK_DANYCH}
- uwagi: {dodatkowe informacje lub BRAK_DANYCH}
- Źródła: {lista plików}

## SEKCJA 7: Klasy
- lista_profili: {lista profili z rozszerzonymi przedmiotami lub BRAK_DANYCH}
- liczba_klas: {liczba lub BRAK_DANYCH}
- uwagi_specjalne: {opis lub BRAK_DANYCH}
- Źródła: {lista plików}

## SEKCJA 8: Infrastruktura
- stolowka_sklepik: {stołówka|sklepik|brak|BRAK_DANYCH}
- biblioteka: {tak|nie|BRAK_DANYCH}
- aula: {tak|nie|BRAK_DANYCH}
- gabinet_pielegniarki: {tak|nie|BRAK_DANYCH}
- szatnia: {tak|nie|BRAK_DANYCH}
- pracownie: {lista lub BRAK_DANYCH}
- stan_budynku: {bardzo dobry|dobry|przeciętny|wymaga remontu|BRAK_DANYCH}
- inne: {opis lub BRAK_DANYCH}
- Źródła: {lista plików}

## SEKCJA 9: Sport
- boiska: {opis boisk — liczba, rodzaje (piłka nożna, koszykówka, tenis itp.), nawierzchnia — lub BRAK_DANYCH}
- sale_gimnastyczne: {opis sal — liczba, rodzaje, wyposażenie — lub BRAK_DANYCH}
- silownia: {tak|nie|BRAK_DANYCH}
- basen: {tak|nie|BRAK_DANYCH}
- dostep_poza_lekcjami: {czy uczniowie mogą korzystać z obiektów sportowych poza zajęciami WF — opis lub BRAK_DANYCH}
- sekcje_sportowe: {lista lub BRAK_DANYCH}
- osiagniecia: {opis lub BRAK_DANYCH}
- uwagi: {opis lub BRAK_DANYCH}
- Źródła: {lista plików}

## SEKCJA 10: Profil intelektualny
- profile_scisle: {n klas + przedmioty lub BRAK_DANYCH}
- profile_humanistyczne: {n klas + przedmioty lub BRAK_DANYCH}
- kola_scisle: {lista lub BRAK_DANYCH}
- kola_humanistyczne: {lista lub BRAK_DANYCH}
- olimpiady_scisle: {lista lub BRAK_DANYCH}
- olimpiady_humanistyczne: {lista lub BRAK_DANYCH}
- jezyk_materialow: {opis tonu/języka materiałów}
- propozycja_oceny humanistyczny: {1|2|3|4|5}  ← 1 = słabe sygnały humanistyczne, 5 = silne
- propozycja_oceny ścisły: {1|2|3|4|5}  ← 1 = słabe sygnały ścisłe, 5 = silne
- uzasadnienie: {krótki opis}
- Źródła: {lista plików}

## SEKCJA 11: Światopogląd
- roznorodnosc_inkluzywnosc: {n}
- mniejszosci_rownosc_prawa: {n}
- tolerancja_akceptacja: {n}
- srodowisko_ekologia: {n}
- patriotyzm_ojczyzna_narod: {n}
- obowiazek_dyscyplina_honor: {n}
- tradycja_wartosci_wiara: {n}
- historia_bohaterowie_pamiec: {n}
- propozycja_oceny lewicowy: {1|2|3|4|5}  ← 1 = słabe sygnały lewicowe, 5 = silne
- propozycja_oceny prawicowy: {1|2|3|4|5}  ← 1 = słabe sygnały prawicowe, 5 = silne
- uzasadnienie: {krótki opis}
- Źródła: {lista plików}

## SEKCJA 12: Równowaga szkolna
- sygnaly_akademickie: {wzmianki o wynikach, rankingach, egzaminach, osiągnięciach akademickich lub BRAK_DANYCH}
- sygnaly_pasji: {różnorodność kół, projekty uczniowskie, inicjatywy własne, język zachęcający do rozwoju pasji lub BRAK_DANYCH}
- propozycja_oceny nauka: {1|2|3|4|5}  ← 1 = słabe sygnały akademickie, 5 = silne
- propozycja_oceny pasje: {1|2|3|4|5}  ← 1 = słabe sygnały pasji, 5 = silne
- uzasadnienie: {krótki opis}
- Źródła: {lista plików}

## SEKCJA 13: Innowacyjność
- nowe_inicjatywy: {opis nowych programów, zmian, inicjatyw z ostatnich lat lub BRAK_DANYCH}
- zajecia_aktualne: {czy zajęcia pozalekcyjne odpowiadają współczesnym trendom — opis lub BRAK_DANYCH}
- tematy_globalne: {czy szkoła podejmuje aktualne tematy globalne (AI, ekologia, zdrowie psychiczne itp.) — opis lub BRAK_DANYCH}
- roznice_od_tradycji: {co odróżnia szkołę od tradycyjnego polskiego liceum lub BRAK_DANYCH}
- propozycja_oceny: {1|2|3|4|5}  ← 1 = tradycyjna/zachowawcza, 5 = wysoce innowacyjna
- uzasadnienie: {krótki opis}
- Źródła: {lista plików}

## SEKCJA 14: Spójność przekazu
- sprzecznosci: {wykryte sprzeczności między materiałami — np. szkoła chwali się otwartością, ale nie ma żadnych wymian; lub BRAK_DANYCH}
- puste_hasla: {slogany i deklaracje bez pokrycia w konkretnych przykładach lub BRAK_DANYCH}
- propozycja_oceny: {1|2|3|4|5}  ← 1 = przekaz bardzo niespójny, 5 = przekaz w pełni spójny i wiarygodny
- uzasadnienie: {krótki opis}
- Źródła: {lista plików}
```

### Reader agent rules

- Read ALL assigned files before producing output.
- Write output to `schools/{folder_name}/{folder_name}_Agent_{letter}.md` — this is the agent's primary responsibility.
- Base ALL content strictly on the files provided — no internet access, no guessing.
- Keep all text in Polish.
- Count Światopogląd signal words literally (approximate counts are fine).
- For Erasmus+: only mark `tak` if Erasmus+ is explicitly mentioned.

### Światopogląd — znane sygnały nieoczywiste

Niektóre aktywności mogą być mylnie klasyfikowane. Poniższe przypadki mają ustaloną kategorię:

| Aktywność / sygnał | Kategoria | Uzasadnienie |
|---|---|---|
| Akcja Żonkil (Muzeum Historii Żydów Polskich POLIN) | `mniejszosci_rownosc_prawa` (lewicowy) | Upamiętnienie ofiar Zagłady — wyraz troski o mniejszości i historyczną empatię; nie należy klasyfikować jako `patriotyzm_ojczyzna_narod` ani `historia_bohaterowie_pamiec` |

---

## Phase 6 — Synthesis

The main agent reads all 5 agent output files (`{folder_name}_Agent_A.md` through `{folder_name}_Agent_E.md`) from the school folder and writes the final `{folder_name}.md` following `template.md`, section by section.

### Conflict resolution

- Any non-`BRAK_DANYCH` value beats `BRAK_DANYCH`.
- When two agents give conflicting non-null values, prefer the **ground-truth agent** for that field:

| Field | Ground-truth agent |
|---|---|
| Adres, URL, kontakt | A (overview.md, kontakt.md) |
| Klasy, Języki | B (rekrutacja.md) |
| Erasmus+, wymiany, olimpiady | C (wymiany_miedzynarodowe.md, udzial_olimpiadach.md) |
| Samorząd, flagowe eventy | D |
| Infrastruktura checkboxes | E (dedicated infrastructure pages) |

### Scoring and narrative fields

- For Światopogląd signal counts: **sum** across all 5 agents (each agent read different files, so counts are additive, not duplicated).

For all `propozycja_oceny` fields, compute a **weighted average** of the five agent proposals, rounded to one decimal place. Skip any agent that returned `BRAK_DANYCH` for that field (exclude both its score and its weight from the computation). After computing the weighted average, read all five justifications and write the final `uzasadnienie` in your own words.

Formula: `score = round( Σ(wᵢ × scoreᵢ) / Σ(wᵢ), 1 )` over agents with non-null proposals.

**Metryki bipolarne (SEKCJA 10, 11, 12):** każdy agent podaje dwa sub-wyniki zamiast jednego. Oblicz ważoną średnią **osobno dla każdego pola**: `avg_A = round( Σ(wᵢ × pole_A_i) / Σ(wᵢ), 1 )` i analogicznie `avg_B`. Oba wyniki są w skali 1–5. Agent syntezy podaje niezależny synthesis_score (1–5) **dla każdego pola z osobna**.

| Metryka | pole_A | pole_B |
|---|---|---|
| SEKCJA 10 Profil intelektualny | `humanistyczny` | `ścisły` |
| SEKCJA 11 Światopogląd | `lewicowy` | `prawicowy` |
| SEKCJA 12 Równowaga szkolna | `nauka` | `pasje` |

**Weights per section per agent:**

| Sekcja | A — Tożsamość | B — Nauczanie | C — Osiągnięcia | D — Życie szkolne | E — Infrastruktura |
|---|:---:|:---:|:---:|:---:|:---:|
| 3 Otwartość | 2 | 1 | 5 | 2 | 1 |
| 4 Przyjazność | 2 | 2 | 1 | 3 | 5 |
| 5 Zaangażowanie | 1 | 3 | 4 | 5 | 1 |
| 10 Profil intelektualny | 3 | 5 | 4 | 2 | 1 |
| 11 Światopogląd | 3 | 2 | 3 | 4 | 2 |
| 12 Równowaga szkolna | 2 | 4 | 4 | 3 | 1 |
| 13 Innowacyjność | 2 | 4 | 3 | 4 | 1 |
| 14 Spójność przekazu | 2 | 2 | 2 | 2 | 2 |

Rationale for the weights:
- **A** (identity pages, mission, history): reveals intellectual and ideological tone, little evidence for operational dimensions.
- **B** (recruitment, class profiles, curriculum, exam results): primary source for intellectual profile and school-balance academic signals; covers extracurricular clubs for engagement.
- **C** (olympiads, competitions, international exchanges): primary source for openness; strong signal for intellectual profile depth and engagement breadth.
- **D** (student council, flagship events, handbook, prevention programs): primary source for engagement and school life worldview signals; contributes to friendliness via prevention.
- **E** (psychological support, financial aid, health services, infrastructure): primary source for friendliness; marginal evidence for other dimensions.

### Spójność przekazu — special synthesis rule

For **SEKCJA 14**, the weighted average of reader-agent proposals is computed normally (equal weights), but the synthesis agent must also apply the following adjustment:

- Compute the **range** of non-null `propozycja_oceny` values across the five agents (max − min).
- A range ≥ 2 is itself evidence of incoherence — different agents read different parts of the site and formed meaningfully different impressions. Each full point of range above 1 should lower the synthesis score by 1 (e.g. range = 3 → subtract 2 from the synthesis score, floored at 1).
- The `synthesis_score` reflects this adjustment and the agent's holistic judgment after reading all five files. It is the primary score for this metric.

### Dual score

**Unipolar metrics (SEKCJA 3, 4, 5, 13, 14)** carry two scores on a single `Ocena` line:

```
- **Ocena:** {weighted_avg} ({synthesis_score})
```

**Bipolar metrics (SEKCJA 10, 11, 12)** have no single `Ocena` line. Instead each pole has its own score line:

```
- **Humanistyczny:** {weighted_avg} ({synthesis_score})
- **Ścisły:** {weighted_avg} ({synthesis_score})
```

(replace `Humanistyczny`/`Ścisły` with the pole names for SEKCJA 11 `Lewicowy`/`Prawicowy` and SEKCJA 12 `Nauka`/`Pasje`)

- **weighted_avg** — the weighted average of the five reader-agent sub-scores for that pole (one decimal place), computed using the formula and weights defined above.
- **synthesis_score** — an integer (1–5) formed independently by the synthesis agent after reading all five agent files in full. It reflects the agent's holistic judgment for that pole. This score may differ from the weighted average when the agent's global read reveals a clearer picture.

The synthesis score must be written in brackets immediately after the weighted average, with no label. Example: `3.2 (3)`.

### Output rules

- Every template field must have a value — no `{...}` placeholders may remain.
- All content in Polish.
- No external URLs fetched — all content derived from `data/content/` only.

---

## Verification checklist

After writing the output file, confirm:
- [ ] No `{...}` placeholders remain
- [ ] All metric sections present with correct headers
- [ ] Erasmus+ field explicitly set to `tak` or `nie`
- [ ] Klasy section describes the actual profile structure (or notes if experimental/no fixed profiles)
- [ ] Światopogląd signal counts are present and summed across all agents
- [ ] Metryki bipolarne (SEKCJA 10, 11, 12): each pole has its own weighted_avg and synthesis_score, both in range 1–5
- [ ] Innowacyjność section present with ocena in range 1–5
- [ ] Spójność przekazu section present with ocena in range 1–5 and inter-agent range noted
- [ ] No external URLs were fetched during processing
