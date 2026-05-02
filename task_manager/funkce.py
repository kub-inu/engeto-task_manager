def obsah_menu() -> str:
    return (
        "Správce úkolů - Hlavní menu\n"
        "1. Přidat nový úkol\n"
        "2. Zobrazit všechny úkoly\n"
        "3. Odstranit úkol\n"
        "4. Konec programu"
    )

def ukol_format(index: int, data: dict[str, str]) -> str:
    return f"{index}. {data['nazev']} - {data['popis']}"

def seznam_ukolu(data: list[dict[str, str]]) -> str:
    if not data:
        return "\nNení nic k zobrazení."
    
    seznam = ["\nSeznam úkolů:"]
    
    for i, ukol in enumerate(data, start=1):
        seznam.append(ukol_format(i, ukol))
    
    return "\n".join(seznam)


# def validacia_vstupu(nazev: str, popis: str) -> str | None:
#     nazev_ukolu, popis_ukolu = nazev.strip(), popis.strip()

#     if not nazev_ukolu and not popis_ukolu:
#         return 'Nezadal jste název ani popis úkolu.'
#     if not nazev_ukolu:
#         return 'Nezadal jste název úkolu.'
#     if not popis_ukolu:
#         return 'Nezadal jste popis úkolu.'
    
#     return None

def validacia_vstupu(hodnota: str, pole: str) -> bool:
    """
    Validuje zadanou hodnotu uživatele - ověří zda je prázdna.

    Args:
        hodnota: hodnota zadaná uživatelem
        pole: název kontrolovaného pole

    Returns:
        True, pokud je hodnota prázdna, jinak False 
    """

    if hodnota.strip():
        return False

    print(f'> Nezadal jste {pole} úkolu. ')
    return True