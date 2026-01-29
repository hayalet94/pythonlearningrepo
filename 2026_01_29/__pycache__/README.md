'''

Project: Learning HTTP-Methods and Input-Masks through Python FastAPI, Request, pydantic BaseModel
    using GET, POST, PUT Methods

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
    