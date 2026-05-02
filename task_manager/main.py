from funkce import seznam_ukolu, obsah_menu, validacia_vstupu


def hlavni_menu() -> None:
    """Vypíše hlavní menu programu do konzole."""
    print(obsah_menu())


def zobrazit_ukoly(ukoly: list[dict[str, str]]) -> None:
    """
    Vypíše do konzole seznam všech uložených úkolů.

    Args:
        ukoly: seznam obsahujíci slovníky úkolů - {"název": str, "popis": str}
    """
    print(seznam_ukolu(ukoly))
    print() #Vytvorí nový riadok kvoli čiateľnosti v kóde


def pridat_ukol(seznam_ukolu: list[dict[str, str]]) -> None:
    """
    Vyzve uživatele k zadání názvu a popisu úkolu.
    Oba vstupy validuje a po zadání uloží nový úkol do seznamu.

    Args:
        seznam_ukolu: seznam úkolů ve formátu {"nazev": str, "popis": str}
    """
    while True:
        nazev = input("\nZadejte název úkolu: ")
        if validacia_vstupu(nazev, "název"):
            continue
        break

    while True:
        popis = input("\nZadejte popis úkolu: ")
        if validacia_vstupu(popis, "popis"):
            continue
        break

    seznam_ukolu.append({
        "nazev": nazev.strip(),
        "popis": popis.strip()
    })

    print(f"Úkol '{nazev.strip()}' byl přidán. \n")


def odstranit_ukol(seznam_ukolu: list[dict[str, str]]) -> None:
    """
    Odstraní úkol ze seznamu podle čísla zadaného uživatelem.
    Funkce se opakuje, dokud uživatel nezadá platné číslo úkolu.

    Args:
        seznam_ukolu: seznam úkolů {"nazev": str, "popis": str}
    """

    if not seznam_ukolu:
        zobrazit_ukoly(seznam_ukolu)
        return
    
    while True:
        try:
            index = int(input("Zadejte číslo úkolu, který chcete odstranit: ")) - 1
            if index < 0:
                raise IndexError

            nazev_ukolu = seznam_ukolu[index]["nazev"]
            seznam_ukolu.pop(index)
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