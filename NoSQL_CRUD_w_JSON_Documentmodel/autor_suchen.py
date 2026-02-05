from json_helper import lade_buecher

buecher = lade_buecher()

def suche_buch_nach_titel(buecher, author):
    gefunden = False

    for buch in buecher:
        if author.lower() in buch["author"].lower():
            print("ID: ", buch["id"], "Titel: ", buch["buch"], "Autor: ", buch["author"], "Jahr: ", buch["erscheinungsjahr"])
            gefunden = True
    
    if not gefunden:
        print("Author nicht gefunden.")

suche_buch_nach_titel(buecher,author="george orwell")