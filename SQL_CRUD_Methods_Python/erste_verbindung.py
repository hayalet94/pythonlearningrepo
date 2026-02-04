import sqlite3

conn = sqlite3.connect("meine_db.db")
print("Verbindung erfolgreich!")

# cursor = conn.cursor()
# print("Cursor erstellt!")
# print(f"Cursor-Objekt: {cursor}")

#cursor.execute("SELECT * FROM tabelle")



with sqlite3.connect("meine_db.db") as conn:
    cursor = conn.cursor()
    

#    cursor.execute("INSERT INTO kontakte (name, email) VALUES ('Testmann', 'testi123@testmail.com')")
name = input("Name: ")
email = input("email: ")

cursor.execute("INSERT INTO kontakte (name, email) VALUES (?,?)", (name, email,))  # ? Placeholders - irritating to figure, prone to positional errors


                                                    #named placeholders better to read, dicts instead tuples, still sql injection safe         
name2 = input("Name: ")
email2 = input("email: ")

cursor.execute("""                                  
               INSERT INTO kontakte (name, email)
               VALUES (:name, :email)
               """,
               {
                    "name":name2,
                    "email":email2
               }
               )

cursor.execute("""
            CREATE TABLE IF NOT EXISTS kontakte (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               email TEXT UNIQUE NOT NULL,
               telefon TEXT
               )
               """)

# conn.commit()             #obsolete because of line 12 context manager method automatic commit

conn.commit()

print("Tabelle erfolgreich erstellt!")

conn.close()
print("Verbindung geschlossen!")