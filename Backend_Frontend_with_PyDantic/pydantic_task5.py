from fastapi import FastAPI # pyright: ignore[reportMissingImports]
from pydantic import BaseModel

app = FastAPI()

class Lieferung(BaseModel):
    gewicht_kg:float

class Rückmeldung(BaseModel):
    status:str
    detail:str

@app.post("/lieferung/anmelden")
def anmeldung(angemeldet:Lieferung,aktuell:Rückmeldung):
    if angemeldet.gewicht_kg > 500:
        return aktuell.status == "fehler"
    
