# Webapp — Spec

## Overview

A single-page app for comparing Warsaw high schools. Not all Warsaw schools have been processed yet. Only schools that have a `.json` file in their `schools/{folder}/` directory are included in the app.

**Stack:** Astro (static, no framework islands needed)

**Data flow:** JSON files are the structured data layer — they are read by Astro at build time and compiled into static HTML. There is no server or runtime data fetching. To update the site after changing school data: edit or regenerate the relevant `.json` file, then run `astro build`.

---

## School picker

- Displayed at the top of the page, full width
- Schools listed inline (horizontal flow, wrapping), each as a button
- Button label format: `{school_id} — {short name}` — e.g. `64 — Witkiewicz`
  - Short name = folder name after the underscore, e.g. `64_Witkiewicz` → `Witkiewicz`
- Clicking a button toggles that school into/out of the comparison
- A single school can be selected (minimum 1, no maximum enforced)
- Selected buttons are visually highlighted

---

## Comparison area

- Full viewport width — no sidebar or navigation panel on either side
- Selected schools appear as columns, side by side
- Max column width: **640 px**
- Field labels and values are aligned across columns (same row = same field)

---

## Column layout

Each column contains the following sections, in order:

1. **Header** — full school name, district, website link
2. **Co szkoła mówi o sobie** — `self_description`
3. **Wyróżniki** — `distinguishing_features` (omit section if `null`)
4. **Podsumowanie** — `summary`
5. **Metryki** — one sub-section per metric (see below)
6. **Dane z ankiet** — `survey` fields (see below)

---

## Metric display

Each metric is a sub-section. Metrics fall into two groups:

### Scored metrics

Metrics that carry `avg_score` / `synthetic_score` (or equivalent paired scores):

| JSON key | Polish label |
|---|---|
| `openness` | Otwartość |
| `friendliness` | Przyjazność |
| `engagement` | Zaangażowanie |
| `intellectual_profile` | Profil intelektualny |
| `worldview` | Światopogląd |
| `school_balance` | Równowaga szkolna |
| `innovation` | Innowacyjność |
| `message_coherence` | Spójność przekazu |

**Default view (collapsed):**
- Metric name (centered, bold)
- Score(s): synthetic score only — e.g. `4`. For metrics with two dimensions (intellectual_profile, worldview, school_balance), show both scores on separate lines with their sub-labels (Humanistyczny / Ścisły, Lewicowy / Prawicowy, Nauka / Pasje)
- `Uzasadnienie` value

**Expanded view:**
- Avg score(s) shown alongside the synthetic score — e.g. `3.9`
- All remaining fields of that metric revealed

A single **"Rozwiń szczegóły"** toggle at the bottom of each scored metric expands/collapses all detail fields at once (not field by field).

### Unscored metrics

Metrics with no score — displayed fully expanded at all times:

| JSON key | Polish label |
|---|---|
| `languages` | Języki |
| `classes` | Klasy |
| `infrastructure` | Infrastruktura |
| `sports` | Sport |

---

## Field rendering

- Each field: label centered in italics above value
- Label = Polish translation of JSON key (see table below)
- `null` / empty values: display `—`
- Arrays: comma-separated or bulleted list depending on length
- Boolean: `tak` / `nie`

### Polish field labels (shared across metrics)

| JSON key | Polish label |
|---|---|
| `avg_score` | Ocena średnia |
| `synthetic_score` | Ocena syntetyczna |
| `erasmus` | Erasmus+ |
| `external_collaboration` | Współpraca zewnętrzna |
| `guests` | Goście i prelegenci |
| `teacher_availability` | Dostępność nauczycieli |
| `current_topics` | Aktualne tematy |
| `new_technologies` | Nowe technologie |
| `justification` | Uzasadnienie |
| `psychologist` | Psycholog / pedagog |
| `support_programs` | Programy wsparcia |
| `mental_wellbeing` | Dobrostan psychiczny |
| `diversity_acceptance` | Akceptacja inności |
| `anti_bullying` | Przeciwdziałanie przemocy |
| `opinion_expression` | Wyrażanie opinii |
| `clubs` | Koła zainteresowań |
| `unusual_activities` | Zajęcia nietypowe |
| `interest_development` | Rozwój zainteresowań |
| `volunteering` | Wolontariat |
| `student_initiatives` | Inicjatywy uczniowskie |
| `student_council` | Samorząd |
| `english` | Angielski |
| `german` | Niemiecki |
| `spanish` | Hiszpański |
| `other` | Inne języki |
| `bilingual_classes` | Klasy dwujęzyczne |
| `bilingual_language` | Język dwujęzyczny |
| `certificates` | Certyfikaty |
| `language_choice` | Wybór języków |
| `language_choice_details` | Szczegóły wyboru |
| `level_groups` | Grupy poziomowe |
| `native_speakers` | Native speakerzy |
| `notes` | Uwagi |
| `classes_notes` | Uwagi do klas |
| `cafeteria` | Stołówka / sklepik |
| `library` | Biblioteka |
| `auditorium` | Aula |
| `nurse_office` | Gabinet pielęgniarki |
| `specialized_labs` | Pracownie specjalistyczne |
| `building_condition` | Stan techniczny |
| `courts` | Boiska |
| `gyms` | Sale gimnastyczne |
| `fitness_room` | Siłownia / fitness |
| `pool` | Basen |
| `access_outside_lessons` | Dostęp poza lekcjami |
| `sports_clubs` | Sekcje sportowe |
| `sports_achievements` | Osiągnięcia sportowe |
| `humanities` | Humanistyczny |
| `stem` | Ścisły |
| `class_profiles_stem` | Profile klas — ścisłe |
| `class_profiles_humanities` | Profile klas — humanistyczne |
| `clubs_stem` | Koła ścisłe |
| `clubs_humanities` | Koła humanistyczne |
| `olympiads_stem` | Olimpiady ścisłe |
| `olympiads_humanities` | Olimpiady humanistyczne |
| `left_avg_score` | Lewicowy (średnia) |
| `left_synthetic_score` | Lewicowy (syntetyczna) |
| `right_avg_score` | Prawicowy (średnia) |
| `right_synthetic_score` | Prawicowy (syntetyczna) |
| `academics_avg_score` | Nauka (średnia) |
| `academics_synthetic_score` | Nauka (syntetyczna) |
| `hobbies_avg_score` | Pasje (średnia) |
| `hobbies_synthetic_score` | Pasje (syntetyczna) |
| `initiatives` | Inicjatywy i zmiany |
| `extracurricular_topics` | Aktualność zajęć |
| `contradictions` | Sprzeczności / puste hasła |

---

## Survey section (Dane z ankiet)

Displayed after metrics. Source: `survey` object in JSON.

Show the following fields (skip nulls):

| JSON key | Polish label |
|---|---|
| `survey_count` | Liczba ankiet |
| `matura_score_pct` | Wyniki matur (%) |
| `matura_pass_rate_pct` | Zdawalność matur (%) |
| `atmosphere_pct` | Atmosfera (%) |
| `learning_enjoyment_pct` | Przyjemność z nauki (%) |
| `student_relations_pct` | Relacje między uczniami (%) |
| `student_teacher_relations_pct` | Relacje uczeń–nauczyciel (%) |
| `teaching_modernity_pct` | Nowoczesność nauczania (%) |
| `recommendation_rate_pct` | Polecałbym/łabym (%) |
| `break_quality_pct` | Jakość przerw (%) |
| `avg_study_time_after_school` | Czas nauki po szkole |
| `student_count_2022` | Liczba uczniów (2022) |
| `year_founded` | Rok założenia |
| `amenities` | Udogodnienia |

---

## Visual design

- Clean, minimal aesthetic
- Metric section headers: centered, bold
- Field labels: centered, italic, muted color
- Field values: centered, full width of column
- Alternating light background between metrics for readability
- Collapsed/expanded state managed client-side (vanilla JS or Astro island)
- Responsive: on narrow viewports columns stack vertically
