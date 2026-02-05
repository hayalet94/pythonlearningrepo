from json_helper import lade_buecher

buecher = lade_buecher()

def zaehle_ungelesen(buecher):
    ungelesene_buecher = 0
    for buch in buecher:
        if buch["gelesen"] is not True:
            print("Titel: ", buch["buch"], "Gelesen: ", buch["gelesen"])
            ungelesene_buecher += 1
    
    print(f"Anzahl ungelesener Bücher: {ungelesene_buecher}")

zaehle_ungelesen(buecher)
