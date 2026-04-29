from funkce import seznam_ukolu, menu_content, validacia_vstupu
ukoly = []

# Zobrazeie hlavného menu
def hlavni_menu() -> None:
    print(menu_content())

# Zobrazenie zoznamu úloh
def zobrazit_ukoly(data: list[dict[str, str]]) -> None:
    print(seznam_ukolu(data))
    print()

# Pridanie novej úlohy do zoznamu
def pridat_ukol() -> None:
    while True:
        nazev = input("\nZadejte název úkolu: ")
        popis = input("Zadejte popis úkolu: ")

        validacia = validacia_vstupu(nazev, popis)

        if validacia:
            print(f"> {validacia}")
            continue

        ukoly.append({
            "nazev": nazev.strip(),
            "popis": popis.strip()
        })

        print(f"\nÚkol '{nazev.strip()}' byl přidán. \n")
        break


# Funkcia odstránenia úlohy zo zoznamu
def odstranit_ukol() -> None:
    zobrazit_ukoly(ukoly)
    if ukoly:
        try:
            index = int(input("Zadejte číslo úkolu, který chcete odstranit: ")) - 1
            if index < 0:
                raise IndexError

            nazev_ukolu = ukoly[index]["nazev"]
            ukoly.pop(index)
            print(f"Úkol '{nazev_ukolu}' byl odstraněn.\n")

        except ValueError:
            print("Zadejte platné číslo úkolu.\n")

        except IndexError:
            print("Takový úkol neexistuje.\n")

# Hlavný loop programu
while True:
    hlavni_menu()
    vstup = input("Vyberte možnost (1-4): ").strip()

    match vstup:
        case "1":
            pridat_ukol()
        case "2":
            zobrazit_ukoly(ukoly)
        case "3":
            odstranit_ukol()
        case "4":
            print("\nKonec programu.\n")
            break
        case _:
            print("\nZadejte platnou volbu z menu programu.\n")
