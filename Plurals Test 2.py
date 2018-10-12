import sqlite3

name = input("Inserisci la parola di cui vuoi conosce il plurale:\n")



conn = sqlite3.connect("Gender.db")
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS Genere(Singolare TEXT, Genere TEXT, Plurale TEXT)")

def data_entry():
    global plurale
    global genere
    print("Non conosco la parola. Aiutami con la sua definizione.")

    regolare = input("E' un plurale regolare?\n")

    if regolare == "Si":
        plurale = plurale()
    if regolare == "No":
        genere = input("Inserisci il genere della parola:\n")
        plurale = input("Inserire il plurale:\n")

    c.execute("INSERT INTO Genere VALUES(?, ?, ?)",(name, genere, plurale)) #aggiungi parola e suo genere

    conn.commit()
    search_data()

def search_data():
    global row
    c.execute("SELECT * FROM Genere WHERE Singolare=(?)", [name])
    row = c.fetchall()
    if len(row) == 0:               #se la lista è vuota(nome non c'è nel database)
        data_entry()                #inserisci nuovi valori
    else:
        print(row[0][2])            #altrimenti stampa il genere

def plurale():
    global genere
    if name[len(name)-1] == "o":
        genere = "Maschile"
        plurale = name[0:(len(name) - 1)] + "i"
        return(plurale)
    if name[len(name)-1] == "a":
        genere = "Femminile"
        plurale = name[0:(len(name) - 1)] + "e"
        return(plurale)


create_table()
search_data()

