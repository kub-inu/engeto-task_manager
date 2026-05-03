def obsah_menu() -> str:
    """Vrátí text hlavního menu."""
    return (
        "Správce úkolů - Hlavní menu\n"
        "1. Přidat nový úkol\n"
        "2. Zobrazit všechny úkoly\n"
        "3. Odstranit úkol\n"
        "4. Konec programu"
    )

def ukol_format(index: int, data: dict[str, str]) -> str:
    """
    Naformátuje jednu položku seznamu úkolů pro výpis do konzole.

    Args:
        index: pořadové číslo úkolu
        data: slovník úkolu ve formátu {"nazev": str, "popis": str}

    Returns:
        str: Naformátovaná položka ve tvaru "<index>. <nazev> - <popis>".
    """
    return f"{index}. {data['nazev']} - {data['popis']}"

def seznam_ukolu(seznam: list[dict[str, str]]) -> str:
    """
    Vrátí naformátovaný seznam úkolů.

    Args:
        seznam: seznam úkolů ve formátu {"nazev": str, "popis": str}

    Returns:
        str: Naformátovaný seznam úkolů nebo hláška o prázdném seznamu.
    """
    if not seznam:
        return "\nNení nic k zobrazení."
    
    vystup = ["\nSeznam úkolů:"]
    
    for i, ukol in enumerate(seznam, start=1):
        vystup.append(ukol_format(i, ukol))
    
    return "\n".join(vystup)

def validacia_vstupu(hodnota: str, pole: str) -> bool:
    """
    Validuje zadanou hodnotu uživatele - ověří zda je prázdna.

    Args:
        hodnota: hodnota zadaná uživatelem
        pole: název kontrolovaného pole

    Returns:
        bool: False, pokud je hodnota prázdna, jinak True 
    """
    if not hodnota.strip():
        print(f'> Nezadal jste {pole} úkolu.\n')
        return False
    
    return True