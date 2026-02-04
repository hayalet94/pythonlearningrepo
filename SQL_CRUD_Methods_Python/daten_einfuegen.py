import sqlite3

conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()


                                                        #declaration with dictionaries
kontakte = [
    {"name":"Ben Mueller", "email":"ben@example.com", "telefon":"030-234567"},
    {"name":"Clara Wagner", "email":"clara@example.com", "telefon":"0421-345678"},
    {"name":"David Klein", "email":"david@example.com", "telefon":None}
]

kontakte_2 = [
    {"name":"Emma Fischer", "email":"emma@example.com", "telefon":"040-456789"},
    {"name":"Felix Bauer", "email":"felix@example.com", "telefon":"030-567890"}
]

cursor.execute("""
            CREATE TABLE IF NOT EXISTS kontakte (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL,
               telefon TEXT
               )
               """)

# cursor.execute(                                   #better readability in my opinion
#     """
#     INSERT INTO kontakte (name, email, telefon) 
#     VALUES (:name,:email,:telefon)
#     """,
#     {
#         "name": "Anna Schmidt",
#         "email": "anna@example.com",
#         "telefon": "040-123456"
#     }
# )

# for kontakt in kontakte:                          #add multiple contacts with for loop
#     cursor.execute(
#         "INSERT INTO kontakte (name, email, telefon) VALUES (:name,:email,:telefon)",
#         kontakt
#     )

cursor.executemany(                                 
    "INSERT OR IGNORE INTO kontakte (name, email, telefon) VALUES (:name, :email, :telefon)",
    kontakte_2
)                                                   #easier implementation through executemany function
                                                    #added INSERT OR IGNORE if data already exists

conn.commit()

print(f"{len(kontakte)} Kontakte eingefügt!")
# print("Kontakt erfolgreich eingefügt!")           #single contact add debug print

conn.close()
