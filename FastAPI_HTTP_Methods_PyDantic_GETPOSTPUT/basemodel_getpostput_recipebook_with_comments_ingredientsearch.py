from fastapi import FastAPI, Request # pyright: ignore[reportMissingImports]

from pydantic import BaseModel

from typing import Optional, Union, List


'''
    FastAPI ist korrekt importiert und initialisiert
    Ein Pydantic-Modell mit BaseModel ist definiert
    Mindestens zwei GET-Endpunkte sind implementiert
    Mindestens ein POST-Endpunkt ist implementiert
    Alle Endpunkte verwenden korrekte Decorators (@app.get, @app.post)
    Die Endpunkte geben JSON-Daten zurück
    Korrekte HTTP-Statuscodes werden verwendet
    Die API startet mit fastapi dev dateiname.py
    Die Swagger UI ist unter http://127.0.0.1:8000/docs erreichbar
    Alle Endpunkte sind über Swagger UI testbar
    Die Einrückung ist korrekt und Kommentare sind vorhanden
    Eine README-Datei mit Kurzbeschreibung liegt bei
'''

app = FastAPI()

rezepte = {}

class Rezeptmaske(BaseModel):
    rezept_id: int
    name: str
    dauer: int
    zutaten: list
    schwierigkeit: str
    zubereitung: str
    bemerkungen: Optional[str] = None

class Rezept_Bemerkung(BaseModel):
    bemerkungen: str

class Zutat(BaseModel):
    zutaten: str

@app.get("/")
def root():
    return {"message":"Willkommen zum Rezeptbuch! Für die Rezeptliste bitte /rezepte öffnen"}

@app.get("/rezepte")
def rezeptbuch():
    return rezepte

@app.get("/rezepte/{rezept_id}")
def rezept_selection(rezept_id: int):
    if rezept_id not in rezepte:
        return "Rezept nicht gefunden, Eingabe überprüfen."
    print(rezepte[rezept_id])
    return rezepte[rezept_id]

@app.post("/rezepte")
def rezept_add(rezept:Union[Rezeptmaske, List[Rezeptmaske]],request:Request):
    print(type(request.method))     #terminaldebug
    print(request.url)              #terminaldebug
    print(rezept)                   #terminaldebug
    
    if isinstance(rezept, list):
        for r in rezept:
            rezepte[r.rezept_id] = r
        return {
            "message": f"{len(rezept)} Rezepte hinzugefügt",
            "Rezepte": [{"id":r.rezept_id, "Name":r.name} for r in rezept]
            }
    
    rezepte[rezept.rezept_id] = rezept
    return {"message": "Rezept hinzugefügt", "rezept_id": rezept.rezept_id, "Rezeptname": rezept.name}

@app.put("/rezepte/{rezept_id}")
def rezept_comment(rezept_id: int, update:Rezept_Bemerkung):

    if rezept_id not in rezepte:
        return {"error": "Rezept nicht gefunden."}

    rezept = rezepte[rezept_id]
    if rezept.bemerkungen == True:
        rezept.bemerkungen += " " + update.bemerkungen
    else:
        rezept.bemerkungen = update.bemerkungen
    
    return rezept

@app.post("/rezepte/zutaten")
def zutaten_search(zutat:Zutat):
    treffer = [r for r in rezepte.values() if zutat.zutaten in r.zutaten]
    if not treffer:
        return {"message": "Zutat in keinem Rezept gefunden."}
    return {f"Zutat":{zutat.zutaten}, "gefunden in Rezepten": len(treffer), "Rezepte": treffer}

