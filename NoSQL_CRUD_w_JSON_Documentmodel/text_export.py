from json_helper import lade_buecher

def exportiere_als_text(buecher, dateiname):
    
    with open(dateiname, "w", encoding="utf-8") as f:
        f.write("="*40+"\n")
        f.write("\t\tBücherliste\n")
        f.write("="*40+"\n")

        for buch in buecher:
            status = "[X]" if buch["gelesen"] else "[ ]"
            f.write(f"{status} {buch["buch"]}\n")
            f.write(f"\tAuthor: {buch["author"]}\n")
            f.write(f"\tErscheinungsjahr: {buch["erscheinungsjahr"]}\n")
            f.write(f"\tID {buch["id"]}\n")
            f.write("-"*40+"\n")


buecher = lade_buecher()
exportiere_als_text(buecher, "buecherliste.txt")
print("[OK] Exportiert nach 'buecherliste.txt' im Projektordner.")