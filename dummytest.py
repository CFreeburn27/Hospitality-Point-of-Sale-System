import mysql.connector
from datetime import datetime



db = mysql.connector.connect(
host= "localhost",
user= "root",
passwd= "nikki",
database= "POSDatabase"
)
mycursor = db.cursor()



mycursor.execute("SELECT * FROM ProductItems")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)