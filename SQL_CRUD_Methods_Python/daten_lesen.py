import sqlite3 

conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

email_suche = "anna@example.com"

#print("db wurde gelesen.")
 
# cursor.execute("SELECT id, name, email, telefon FROM kontakte")

# rows = cursor.fetchall()                    #fetch all data from rows

# for row in rows:                            #positional row pull
#     print(f"ID: {row[0]}")
#     print(f"Name: {row[1]}")
#     print(f"Email: {row[2]}")
#     print(f"Telefon: {row[3]}")
#     print("-"*40)                                     #dashes for readability

cursor.execute(                                         #named placeholders method
    """
    SELECT id, name, email, telefon FROM kontakte
    WHERE email = :email
    """,
    {"email":email_suche}
)

row = cursor.fetchone()

if row:
    print(f"Kontakt gefunden:")
    print("-"*40)
    print(f"ID: {row[0]}")
    print(f"Name: {row[1]}")
    print(f"Email: {row[2]}")
    print(f"Telefon: {row[3]}")
    print("-"*40)
else:
    print(f"Kein Kontakt mit Email '{email_suche}' gefunden")

conn.close()                                #close connection
