from fastapi import FastAPI, Request     # pyright: ignore[reportMissingImports]

from pydantic import BaseModel

klientenliste = []

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool

@app.get("/")
def root():
    return {"message":"helloworld"}

@app.post("/klient")
def klientanfrage(klient_objekt: Item, request:Request):
    print(request.method)
    print(request.url)
    print(klient_objekt)
    klientenliste.append(klient_objekt)
    return klient_objekt

@app.get("/klient")
def klientenübersicht():
    return klientenliste

