import sqlite3
conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

cursor.execute(                                 #update data entries
    """
    UPDATE kontakte SET telefon = :telefon
    WHERE email = :email
    """,
    {
        "telefon":"040-99999",
        "email":"anna@example.com"
    }
)

conn.commit()

print(f"Geänderte Zeilen: {cursor.rowcount}")

conn.close()
