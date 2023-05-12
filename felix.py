import mysql.connector
import json

def maakverbinding():
    mydb = mysql.connector.connect(
        host="dbycolvrijdag1.mysql.database.azure.com",
        port=3306, 
        user="felixdeadmin",
        password="abcd1234ABCD!@#$",
        database="ycolfieldvrijdag",
        ssl=True
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