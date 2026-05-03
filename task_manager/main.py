from funkce import seznam_ukolu, obsah_menu, validacia_vstupu

def hlavni_menu() -> None:
    """Vypíše hlavní menu programu do konzole."""
    print(obsah_menu())

def zobrazit_ukoly(ukoly: list[dict[str, str]]) -> None:
    """
    Vypíše do konzole seznam všech uložených úkolů.

    Args:
        ukoly: seznam úkolů ve formátu {"nazev": str, "popis": str}
    """
    print(seznam_ukolu(ukoly))
    print() # Vytvoří prázdný řádek kvůli čitelnosti výstupu.

def pridat_ukol(ukoly: list[dict[str, str]]) -> None:
    """
    Vyzve uživatele k zadání názvu a popisu úkolu.
    Oba vstupy validuje a po zadání uloží nový úkol do seznamu.

    Args:
        ukoly: seznam úkolů ve formátu {"nazev": str, "popis": str}
    """
    print() # Vytvoří prázdný řádek kvůli čitelnosti výstupu.
    while True:
        nazev = input("Zadejte název úkolu: ")
        if not validacia_vstupu(nazev, "název"):
            continue
        break

    while True:
        popis = input("Zadejte popis úkolu: ")
        if not validacia_vstupu(popis, "popis"):
            continue
        break

    ukoly.append({
        "nazev": nazev.strip(),
        "popis": popis.strip()
    })

    print(f"Úkol '{nazev.strip()}' byl přidán.\n")

def odstranit_ukol(ukoly: list[dict[str, str]]) -> None:
    """
    Odstraní úkol ze seznamu podle čísla zadaného uživatelem.
    Funkce se opakuje, dokud uživatel nezadá platné číslo úkolu.

    Args:
        ukoly: seznam úkolů {"nazev": str, "popis": str}
    """
    if not ukoly:
        zobrazit_ukoly(ukoly)
        return
    
    while True:
        zobrazit_ukoly(ukoly)
        try:
            index = int(input("Zadejte číslo úkolu, který chcete odstranit: ")) - 1
            if index < 0:
                raise IndexError

            nazev_ukolu = ukoly[index]["nazev"]
            ukoly.pop(index)
            print(f"Úkol '{nazev_ukolu}' byl odstraněn.\n")
            break
        except ValueError:
            print("Zadejte platné číslo úkolu.\n")
        except IndexError:
            print("Takový úkol neexistuje.\n")

def spustit_aplikaci() -> None:
    """
    Spustí hlavní smyčku aplikace.
    Program se ukončí po zadání volby „4“ v hlavním menu.
    """
    ukoly = []
    while True:
        hlavni_menu()
        vstup = input("Vyberte možnost (1-4): ").strip()
        match vstup:
            case "1":
                pridat_ukol(ukoly)
            case "2":
                zobrazit_ukoly(ukoly)
            case "3":
                odstranit_ukol(ukoly)
            case "4":
                print("\nKonec programu.\n")
                break
            case _:
                print("\nZadejte platnou volbu z menu programu.\n")

if __name__ == "__main__":
    spustit_aplikaci()