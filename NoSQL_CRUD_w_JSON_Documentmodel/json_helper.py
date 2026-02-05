import json

DATEI = "bibliothek.json"

def lade_buecher():
    """
    Lädt Bücher aus bibliothek.json

    Heute: Ohne Fehlerbehandlung (try/except morgen)
    Vorraussetzung: bibliothek.json existiert und enthält gültiges JSON

    Returns: 
        list: Liste von Buch-Dictionaries
    """

    with open(DATEI, "r", encoding="utf-8") as f:
        buecher = json.load(f)

        #Mini-Check: JSON-Entry muss Liste sein

        if not isinstance(buecher, list):
            raise TypeError("bibliothek.json muss ein JSON-Array (Liste) enhalten.")
        return buecher

def speichere_buecher(buecher):
    """
    Speichert Bücher in bibliothek.json

    Args:
        buecher (list): Liste von Buch-Dictionaries
    """
    with open(DATEI, "w", encoding="utf-8") as f:
        json.dump(buecher, f, ensure_ascii=False, indent=2)

def naechste_id(buecher):
    """
    Ermittelt die nächste freie ID

    Args:
        buecher(list): Liste von Buch-Dictionaries
    
    Returns:
        int: Nächste freie ID
    """
    if not buecher:
        return 1
    return max(buch["id"] for buch in buecher) + 1