from fastapi import FastAPI # pyright: ignore[reportMissingImports]
#import requests

#url = "http://127.0.0.1:8000/"

#response = requests.get(url)

app = FastAPI()

warendb = {
    100.2:"Bananenbrot",
    285.52:"Melone"
}


@app.get("/")
def root():
    return {"message":"hello world"}

@app.get("/waren")
def waren():
    print("Warenlager - bitte so benutzen: .../waren/Nummer ")
    return warendb


@app.get("/waren/{waren_nr}")
def warennummer(waren_nr: float):
    if waren_nr not in warendb:
        return "Nummer nicht gefunden. Sicher, dass sie existiert?"
    else:
        print(f"\nWarennummer empfangen: {warendb.get(waren_nr)}")
        return warendb.get(waren_nr)
        

    

    