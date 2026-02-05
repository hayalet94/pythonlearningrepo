from json_helper import lade_buecher, speichere_buecher

def markiere_als_gelesen(buecher, buch_id):

    for buch in buecher:
        gefunden = False
        if buch_id == buch["id"]:
            gefunden = True
            if buch["gelesen"] is not True:
                buch["gelesen"] = True
                return print(f"ID: {buch["id"]} - {buch["buch"]} wurde als gelesen markiert.")
            else:
                return print(f"ID: {buch["id"]} - {buch["buch"]} schon gelesen.")
        
    if not gefunden:
        print("ID nicht gefunden.")

buecher = lade_buecher()

markiere_als_gelesen(buecher, 3)

speichere_buecher(buecher)