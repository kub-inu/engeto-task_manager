# Task Manager
---
Prvý projekt pre certifikáciu Testing Academy od Engeta.

Jednoduchá CLI aplikácia napísaná v Pythone pre správu úloh spolu s vytvorenými testovacími prípadmi pre manuálne testovanie.

## 📌 Popis projektu

Projekt pozostáva z dvoch častí:
1. Implementácia CLI aplikácie **Task Manager**
2. Návrh a exekúcia **testovacích prípadov (Test Cases)** + pripomienky k zadaniu

Aplikácia umožňuje:
- pridať úlohu
- zobraziť úlohy
- odstrániť úlohu

Testovanie pokrýva hlavné funkcionality vrátane validácie vstupov a hraničných prípadov.


### ⚙️ Funkcionalita aplikácie

- `hlavni_menu()` – navigácia v aplikácii
- `pridat_ukol()` – pridanie novej úlohy
- `zobrazit_ukoly()` – výpis uložených úloh v zozname
- `odstranit_ukol()` – odstránenie úlohy

---

## 🧪 Testovanie

Testovanie bolo vykonané manuálne pomocou definovaných testovacích prípadov.

### Pokrytie:
- Happy path scenáre
- Validácia vstupov
- Edge cases
- Chybové stavy

### Použité techniky:
- ekvivalenčné triedy (Equivalence Partitioning)
- hraničné hodnoty (Boundary Value Analysis)
- parametrizované testy

### Výsledok:
- Všetky testy **prešli**
- Neboli identifikované žiadne defekty v rámci scope zadania

📄 Dokumentácia s vytvorenými testovacími prípadmi:
- `\task_manager_tc.pdf` ([Google Drive](https://docs.google.com/document/d/1xRp1iqtB5Z8bxbM4HAYWtApahmfkme07WkqjXBaLXpY/edit?usp=sharing))


### Mimo rozsah (Out of scope)

- perzistencia dát (uloženie do súboru / DB)
- editácia úloh (CRUD nie je kompletný)
- výkon a bezpečnosť
- pokročilá validácia (napr. dĺžka vstupu)

---

## Spustenie aplikácie

### 1. Klonovanie repozitára
```bash
git clone https://github.com/kub-inu/engeto-task_manager.git
```

### 2. Prejdenie do priečinka
V IDE otvor terminál a pomocou príkazu prejdi do adresára `\task_manager`. (Alebo si súbor otvor priamo v IDE a tento krok preskoč.)
```bash
cd task_manager
```

### 3. Spustenie aplikácie
V konzole zadaj tieto príkazy pre spustenie programu.
#### Windows
```bash
py main.py
```
```bash
python main.py
```

#### Linus / macOS
```bash
python3 main.py
```