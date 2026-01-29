
Project: Learning HTTP-Methods and Input-Masks through Python FastAPI, Request, pydantic BaseModel using GET, POST, PUT Methods, added library typing Optional for Optional inputs

Methods:

GET: root - Placeholder Welcomemessage 
GET: Rezeptbuch - return Recipebook Entries List
POST: Rezept Add - BaseModel Rezeptmaske -> Pydantic BaseModels
GET: Rezept Selection - access recipes by id + except
PUT: Rezept Comment - BaseModel Rezeptmaske -> Pydantic BaseModels, access reciped by id and update comment + except

Pydantic BaseModels:

    Mask Rezeptmaske
        mask: 
            rezept_id: int
            name: str
            dauer: int
            zutaten: list
            schwierigkeit: str
            zubereitung: str
            bemerkungen: Optional[str] = None #Optional addition, can be added later
    Mask Rezept_Bemerkung
        mask:
            bemerkungen: str

GET: "/" - message: "Willkommen zum Rezeptbuch! Für die Rezeptliste bitte /rezepte öffnen"

GET: "/rezepte" - Returns list of entries in recipebook

GET: "/rezepte/{rezept_id}" - Returns individual recipe based on recipe id
    +except - "Rezept nicht gefunden. Eingabe überprüfen."

POST: "/rezepte" - debug prints: type of request method, request url, added recipe
    +adds recipe entry validated by BaseModel Mask to recipelist
    +returns recipelist
    
PUT: "/rezepte/{rezept_id}" - appends comment("bemerkungen") to selected recipe by recipe id if recipe id exists within recipe list, if no comment yet, creates new one
    +returns updated recipe



    