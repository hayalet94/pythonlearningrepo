from json_helper import lade_buecher

print(f"Anzahl der Bücher: {len(lade_buecher())}")
print(f"Typ der Daten: {type(lade_buecher)}")

for buch in lade_buecher():

    if buch["gelesen"] == True:
        gelesen = "[X]"
    else:
        gelesen = "[]"

    print("Gelesen?: ", gelesen ,"\tTitel:", buch["buch"],"\tAuthor: ", buch["author"])
