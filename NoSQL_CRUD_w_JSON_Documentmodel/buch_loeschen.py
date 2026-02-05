from json_helper import lade_buecher, speichere_buecher




def loesche_buch(buecher, buch_id):
    
    for buch in buecher:
        gefunden = False
        if buch_id == buch["id"]:
            gefunden = True
            buecher.remove(buch)
            return print(f"{buch["buch"]} mit der ID: {buch["id"]} wurde aus der Bibliothek entfernt.")
        
    if not gefunden:
        print("ID nicht gefunden.")


buecher = lade_buecher()

alte_anzahl_buecher = len(buecher)

loesche_buch(buecher, 6)

neue_anzahl_buecher = len(buecher)

print(f"{alte_anzahl_buecher-neue_anzahl_buecher} Bücher wurden entfernt.")
print(f"Neue Anzahl der Bücher: {neue_anzahl_buecher}")

speichere_buecher(buecher)