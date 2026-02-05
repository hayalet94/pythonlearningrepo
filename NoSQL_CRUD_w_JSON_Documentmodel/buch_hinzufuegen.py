from json_helper import lade_buecher, speichere_buecher, naechste_id


buecher=lade_buecher()

neues_buch = {
    "id":naechste_id(buecher),
    "buch":"Animal Farm",
    "author":"George Orwell",
    "erscheinungsjahr":1945,
    "gelesen":True,
    "tags": ["Roman", "Englisch", "Dystopie"]
    }

alte_anzahl_buecher = len(buecher)

buecher.append(neues_buch)
neue_anzahl_buecher = len(buecher)

speichere_buecher(buecher)

print(f"{neue_anzahl_buecher-alte_anzahl_buecher} Bücher wurden hinzugefügt!")
print(f"ID-Nr. des Buches: {neues_buch["id"]}")
print(f"Neue Anzahl der Bücher: {len(lade_buecher())}")
