from fastapi import FastAPI, Request # pyright: ignore[reportMissingImports]
from pydantic import BaseModel

app = FastAPI()

profilliste = []
buchung_ph = []

testkunde = {
        "k_id": 1,
        "name": "Hansmüller",
        "ist_premium": True
        }



class Kunde(BaseModel):
    k_id: int
    name: str
    ist_premium: bool

class Product(BaseModel):
    titel: str
    lagerbestand: int

@app.get("/")
def root():
    return {"message":"helloworld"}

@app.post("/profil")
def profil(kunde_data:Kunde,request:Request):
    print(request.method)
    print(request.url)
    print(kunde_data)
    profilliste.append(testkunde)
    return profilliste

@app.get("/profil")
def profil_abrufen():
    return profilliste

@app.post("/lager/verbuchen")
def inventar_verbuchen(buchung:Product, request:Request):
    print(request.method)
    print(request.url)
    buchung_ph.append(buchung)
    return buchung
    

@app.get("/lager/verbuchen")
def inventar_verbuchen_display():
    return buchung_ph

