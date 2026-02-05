
Project: 

    Learning HTTP-Methods and Input-Masks through Python FastAPI, Request, pydantic BaseModel using GET, POST, PUT Methods, added library typing Optional for Optional inputs
_____________________________________________________________________

Methods:

    GET: root - Placeholder Welcomemessage 

    GET: Rezeptbuch - return Recipebook Entries List

    POST: Rezept Add - BaseModel Rezeptmaske -> Pydantic BaseModels

    GET: Rezept Selection - access recipes by id + except

    PUT: Rezept Comment - BaseModel Rezeptmaske -> Pydantic BaseModels, 
    access reciped by id and update comment + except

_____________________________________________________________________

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
_____________________________________________________________________

    GET: "/" - message: "Willkommen zum Rezeptbuch! Für die Rezeptliste bitte /rezepte öffnen"

    GET: "/rezepte" - Returns list of entries in recipebook

    GET: "/rezepte/{rezept_id}" - Returns individual recipe based on recipe id
        +except - "Rezept nicht gefunden. Eingabe überprüfen."

    POST: "/rezepte" - debug prints: type of request method, request url, added recipe
        +adds recipe entry validated by BaseModel Mask to recipelist
        +returns recipelist
        
    PUT: "/rezepte/{rezept_id}" - appends comment("bemerkungen") to selected recipe by recipe id if recipe id exists within recipe list, if no comment yet, creates new one
        +returns updated recipe

_____________________________________________________________________

ADDITIONAL (with LLM Help)
_____________________________________________________________________

>FILE: 
    basemodel_getpostput_recipebook_with_comments_ingredientseach.py

>COMMENT:
    +Added typing Union, List for merging multiple recipe entries via POST
    +Added implementing multiple recipes at once via post
    +Added ingredient search function - type in ingredient via post and find recipes which contain your ingredient

_____________________________________________________________________

CHANGES:
_____________________________________________________________________

    POST: "/rezepte" - 

        +checks if entry is instance, compares recipe within list

        +loops through entries and defines individual instances

        +returns how many recipes got added

        +returns IDs and Names of added recipes

        +appends recipes to recipelist

        +returns confirmation message that recipe got added

        +also works for single entries


_____________________________________________________________________

ADDED FUNCTIONS:
_____________________________________________________________________
    Pydantic BaseModel: 
    
    Mask Zutat
            mask:
                zutaten: str

    POST: "/rezepte/zutaten" - searches for typed ingredient within body of recipelist /rezepte
        +if ingredient within recipelist: return amount of hits of your ingredient within recipes, return recipes which contain your ingredient

