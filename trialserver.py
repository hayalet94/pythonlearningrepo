from fastapi import FastAPI # pyright: ignore[reportMissingImports]

app = FastAPI()

@app.get("/")
def root():
    return {"message":"hello world"}

@app.get("/status")
def dikshineri():
    return {"service":"aktiv"}

@app.get("/mitarbeiter")
def mitarbeitende():
    return [{
        "id":101,
        "abteilung":"Vertrieb"
        },
        {   
        "id":102,
        "abteilung":"IT"
        }] 