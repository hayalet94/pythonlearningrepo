from json_helper import lade_buecher

buecher = lade_buecher()

buecher_nach_jahr = []

def sort_nach_jahr(buecher, aufsteigend=True):

    return sorted(
        buecher,
        key=lambda buch: buch["erscheinungsjahr"],
        reverse=not aufsteigend
    )

sortierte_buecher = sort_nach_jahr(buecher, False)
for buch in sortierte_buecher:
    print("ID: ", buch["id"], "Jahr: ", buch["erscheinungsjahr"], "Titel: ", buch["buch"], "Autor: ", buch["author"])

