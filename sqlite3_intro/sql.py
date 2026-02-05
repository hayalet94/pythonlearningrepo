import sqlite3

conn = sqlite3.connect("app.db")                                # alias schreiben -> app.db erstellen -> wird erstellt falls nicht existiert

cur = conn.cursor()                                             # Ausführhilfe für SQL-Befehle -> Alias

# cur.execute("""                                               # cur execute alias -> Tabelle erstellen in Python

#             CREATE TABLE IF NOT EXISTS users (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT NOT NULL,
#                 email TEXT UNIQUE NOT NULL,
#                 created_at TEXT DEFAULT (datetime('now'))
#             )
#             """)

# cur.execute(                                                  # cur execute ist alias -> Um Datensätze einzufügen
#     "INSERT INTO users (name, email) VALUES (?,?)",
#     ("Jacob", "jacob@example.com")
# )

# cur.execute("SELECT id, name, email, created_at FROM users")    # cur execute für SELECT

# rows = cur.fetchall()                                           # fetchall funktion um alle datensätze anzuzeigen

# for row in rows:                                                # loop durch datensätze
#     print(row)

# cur.execute(                                                    # UPDATE USERS mit name: Jacob bei der die Emailadresse jacob@example.com ist
#     "UPDATE users SET name = ? WHERE email = ?",
#     ("Jacob", "jacob@example.com")
# )

# cur.execute(                                                     # DELETE Datensatz von Tabelle users bei der die Emailadresse jacob@example.com ist
#     "DELETE FROM users WHERE email = ?",
#     ("jacob@example.com",)
# )


conn.commit()                                                  #änderungen speichern
conn.close()                                                    #verbindung schließen