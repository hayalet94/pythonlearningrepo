from fastapi import FastAPI, Request # pyright: ignore[reportMissingImports]

from pydantic import BaseModel

from typing import Optional


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
    return rezepte

@app.post("/rezepte")
def rezept_add(rezept:Rezeptmaske, request:Request):
    print(type(request.method))
    print(request.url)
    print(rezept)
    rezepte[rezept.rezept_id] = rezept
    return rezepte

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