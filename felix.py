import mysql.connector
import json
import pandas


def maakverbinding():
    mydb = mysql.connector.connect(
        host="dbycolvrijdag1.mysql.database.azure.com",
        port=3306, 
        user="felixdeadmin",
        password="abcd1234ABCD!@#$",
        database="ycolfieldvrijdag"
        #ssl=True
    )
    return mydb


def felixstart(deparam):
    dedb = maakverbinding()
    gaan = deparam
    sql = "INSERT INTO fiets (brand, diameter) VALUES (%s, %s)"
    val = (gaan, 21)
    cursor = dedb.cursor()
    cursor.execute(sql, val)
    dedb.commit()
    print("in de methode van felix")
    return "hij doet het"+deparam

def toonAlleFietsen():
    dedb = maakverbinding()
    mycursor = dedb.cursor()
    mycursor.execute("SELECT * FROM fiets")
    myresult = mycursor.fetchall()
    return json.dumps(myresult)

def leesuitcsv():
    print("csv lezen in python")
    totalstring = ""
    hetdf = pandas.read_csv("Pokemon.csv")

    print(hetdf.columns)

    for pokemon in hetdf["Name"]:
        print(pokemon)

    for i, pokemon in hetdf.iterrows():
        print(pokemon["Name"]+"met de kracht", pokemon["Attack"])
        totalstring += "de "+pokemon["Name"]+" heeft als strength "+str(pokemon["Attack"])+"<br>"
    return totalstring