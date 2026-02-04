import sqlite3 

conn = sqlite3.connect("kontakte.db")
cursor = conn.cursor()

email_loeschen = "david@example.com"

cursor.execute(                                         #immer pre-checken um nicht ganze DB zu löschen
            """
            SELECT name FROM kontakte WHERE email = :email
            """,
            {"email":email_loeschen}
            )

row = cursor.fetchone()                                 #definition um nur eine row anzuzeigen

if row:
    print(f"Kontakt '{row[0]}' wird gelöscht...")
                                                        #gleiche dict syntax für cohesiveness
    cursor.execute("""                                  
                   DELETE FROM kontakte
                   WHERE email = :email
                   """,
                   {"email":email_loeschen}
                   )
    
    conn.commit()                                       #committen wenn done

    print(f"Gelöscht: {cursor.rowcount} Zeile(n)")
else:
    print(f"Kein Kontakt mit Email: '{email_loeschen}' gefunden.")


conn.close()