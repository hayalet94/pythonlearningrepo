from json_helper import lade_buecher

buecher = lade_buecher()

def suche_buch_nach_titel(buecher, suchbegriff):
    gefunden = False

    for buch in buecher:
        if suchbegriff.lower() in buch["buch"].lower():
            print("ID: ", buch["id"], "Titel: ", buch["buch"], "Autor: ", buch["author"], "Jahr: ", buch["erscheinungsjahr"])
            gefunden = True
    
    if not gefunden:
        print("Buch nicht gefunden.")

suche_buch_nach_titel(buecher,suchbegriff="Python")