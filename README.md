# Task Manager

Prvý projekt pre certifikáciu Testing Academy od Engeta.
Jednoduchá CLI aplikácia napísaná v Pythone pre správu úloh spolu s vytvorenými testovacími prípadmi pre manuálne testovanie.

## Popis projektu

Projekt pozostáva z dvoch častí:
1. Implementácia CLI aplikácie **Task Manager**
2. Návrh a exekúcia **testovacích prípadov (Test Cases)** + pripomienky k zadaniu

Aplikácia umožňuje:
- pridať úlohu
- zobraziť úlohy
- odstrániť úlohu

Testovanie pokrýva hlavné funkcionality vrátane validácie vstupov a hraničných prípadov.

### Funkcionalita aplikácie

- `hlavni_menu()` – navigácia v aplikácii
- `pridat_ukol()` – pridanie novej úlohy
- `zobrazit_ukoly()` – výpis uložených úloh v zozname
- `odstranit_ukol()` – odstránenie úlohy

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
#### Linux / macOS
```bash
python3 main.py
```
---

## Testovanie
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

### Mimo rozsah (Out of scope)
- perzistencia dát (uloženie do súboru / DB)
- editácia úloh (CRUD nie je kompletný)
- výkon a bezpečnosť
- pokročilá validácia (napr. dĺžka vstupu)

---

## Dokumentácia s vytvorenými testovacími prípadmi:
### v0.2
- [Task_Manager_TC_SK_v0.2](https://docs.google.com/document/d/1Pv5U1ykjbDslHGMPoWtJqtv8QFfUzoIZUpQS9F_NGPg/edit?usp=sharing) (Google Docs)
- [Task_Manager_TC_CZ_v0.2](https://docs.google.com/document/d/1vcdw8emFGb5UFqsxaK8ANfsZS-8qoDT_kvjrzrLqSFI/edit?usp=sharing) (Google Docs)

### v0.1:
- [Task_Manager_TC_SK_v0.1](https://docs.google.com/document/d/1xRp1iqtB5Z8bxbM4HAYWtApahmfkme07WkqjXBaLXpY/edit?usp=sharing) (Google Docs)

---

## Aktuálne zmeny po oprave

### Zmeny v kóde:
- Odstránenie globálnej premennej `ukoly`
- Pridanie funkcie `spustit_aplikaci()`, ktorá spravuje chod programu. Premenná `ukoly` bola presunutá do tejto funkcie a odtiaľ sa preposiela ako argument do: `zobrazit_ukoly(ukoly)`, `pridat_ukol(ukoly)` a `odstranit_ukol(ukoly)`
- Funkcie pracujú priamo s predaným zoznamom (mutácia namiesto vracania nového zoznamu), čo využíva vlastnosť listu ako mutovateľného dátového typu.
- Úprava validačnej logiky pri pridávaní novej úlohy: validácia prebieha pre každý vstup samostatne a opakuje sa, kým užívateľ nezadá platný vstup
    - Úprava pomocnej funkcie `validacia_vstupu(hodnota, pole)`: funkcia kontroluje, či je hodnota prázdna a podľa toho vracia True/False. Zároveň skladá validačnú hlášku podľa názvu poľa (hlášky nie sú natvrdo definované v kóde)
- Úprava validačnej logiky pri odstránení úlohy: po zadaní neplatného vstupu alebo neexistujúcej úlohy program opakuje zadanie (retry loop) a nevracia užívateľa do hlavného menu
- Pridanie docstringov k funkciám

### Zmeny v dokumentácii:
- Testovacie dokumenty boly presunuté do samostatného súboru v root adresári projektu
- Konkrétne zmeny sú uvedené na konci testovacieho dokumentu
- Na odporúčanie pridaná česká verzia testovacej dokumentácie
