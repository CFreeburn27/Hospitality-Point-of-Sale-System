import mysql.connector
from datetime import datetime

import mysql.connector
from datetime import datetime



db = mysql.connector.connect(
host= "localhost",
user= "root",
passwd= "nikki",
database= "posdatabase"
)
mycursor = db.cursor()



# mycursor.execute("SELECT Product_Per_Unit_Cost FROM ProductItems WHERE Product_ID = '1234567891'")
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)

# db = mysql.connector.connect(
# 	host= "localhost",
# 	user= "root",
# 	passwd= "nikki",
# 	database= "posdatabase"
# 	)
# mycursor = db.cursor()
#
# # #create database
# # mycursor.execute("CREATE DATABASE POSDataase")
# # db.commit()
# #
sql = "DROP TABLE IF EXISTS Customer, ProductItems"
mycursor.execute(sql)
#
mycursor.execute("CREATE TABLE ProductItems (Product_ID INTEGER(12) PRIMARY KEY, Product_Name VARCHAR(255), Product_Brand VARCHAR(255), Product_Type VARCHAR(255), Product_Description VARCHAR(255)\
, Product_Per_Unit_Cost float(53), Stock_Level INTEGER(12))")
#
#
# # mycursor.execute("SELECT Product_Per_Unit_Cost FROM ProductItems WHERE Product_ID = '1234567891'")
# # myresult = mycursor.fetchall()
# # for x in myresult:
# #	print(x)
#
# mycursor.execute("SELECT Product_Per_Unit_Cost FROM ProductItems WHERE Product_ID = '1234567891'")
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)


Product_info1 = "INSERT INTO ProductItems (Product_ID, Product_Name, Product_Brand, Product_Type, Product_Description, Product_Per_Unit_Cost, Stock_Level) VALUES (1234567891, 'VB Schooner', 'CUB', 'Beer', 'Local Australian Beer', 7.0, 300 \
), (1234567890, 'Carlton Schooner', 'CUB', 'Beer', 'Local Australian Beer', 7.0, 250), (1234567889, 'Tooheys New Schooner', 'Lion', 'Beer', 'Local Australian Beer', 7.0, 500) , (1234567888, \
'XXXX Schooner', 'Lion', 'Beer', 'Mid Strength Beer', 6.80, 500), (1234567887, 'Furphy Schooner', 'Lion', 'Beer', 'Australian Craft Beer', 8.80, 300 \
), (1234567886, 'Kosciuszko Schooner', 'Lion', 'Beer', 'Australian Craft Beer', 8.80, 300 \
) "

Product_info2 = "INSERT INTO ProductItems (Product_ID, Product_Name, Product_Brand, Product_Type, Product_Description, Product_Per_Unit_Cost, Stock_Level) VALUES (1234567885, 'Bottle of Rosé', 'Estate Wines', 'Rosé', 'French Rosé', 40.0, 300 \
), (1234567884, 'Bottle of Champagne', 'Estate Wines', 'Sparkling Wine', 'French Champagne', 62.0, 250), (1234567883, 'Glass of Shiraz', 'Estate Wines', 'Red Wine', 'Australian Shiraz', 8.80, 500) , (1234567882, \
'Bottle of Shiraz', 'Estate Wines', 'Red Wine', 'Australian Shiraz ', 48.0, 500), (1234567881, 'Glass of Chardonnay', 'Estate Wines', 'White Wine', 'Australian Chardonnay', 8.50, 300 \
), (1234567880, 'Bottle of Chardonnay', 'Estate Wines', 'White Wine', 'Australian Chardonnay', 45.0, 300 \
) "

Product_info3 = "INSERT INTO ProductItems (Product_ID, Product_Name, Product_Brand, Product_Type, Product_Description, Product_Per_Unit_Cost, Stock_Level) VALUES (1234567879, 'Bundaberg OP Nip', 'Paramount', 'Spirit', 'Rum', 8.0, 300 \
), (1234567878, 'George Dickel Nip', 'Diageo', 'Spirit', 'Bourbon', 8.0, 250), (1234567877, 'Smirnoff Nip', 'Paramount', 'Spirit', 'Vodka', 8.0, 500) , (1234567876, \
'Gordons Nip', 'Diageo', 'Spirit', 'Gin', 48.0, 500), (1234567875, 'Don Julio Blanco Nip', 'Diageo', 'Spirit', 'Tequilla', 8.0, 300 \
), (1234567874, 'Johnnie Walker Red Nip', 'Paramount', 'Spirit', 'Whiskey', 8.0, 300 \
) "
Product_info4 = "INSERT INTO ProductItems (Product_ID, Product_Name, Product_Brand, Product_Type, Product_Description, Product_Per_Unit_Cost, Stock_Level) VALUES (1234567873, 'Margarita', 'Parkhouse', 'Cocktail', 'Classic Coktails', 15.0, 300 \
), (1234567872, 'Cosmopolitan', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 15.0, 250), (1234567871, 'Mojito', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 16.0, 500) , (1234567870, \
'Old Fashioned', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 18.0, 500), (1234567869, 'Negroni', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 19.0, 300 \
), (1234567868, 'Espresso Martini', 'Parkhouse', 'Cocktail', 'Classic Cocktails', 18.0, 300 \
) "
Product_info5 = "INSERT INTO ProductItems (Product_ID, Product_Name, Product_Brand, Product_Type, Product_Description, Product_Per_Unit_Cost, Stock_Level) VALUES (1234567867, 'Jug of Beer', 'CUB', 'Beer', 'Local Australian Beer', 20.0, 300 \
) "

mycursor.execute(Product_info1)
mycursor.execute(Product_info2)
mycursor.execute(Product_info3)
mycursor.execute(Product_info4)
mycursor.execute(Product_info5)
db.commit()
#
# mycursor.execute("CREATE TABLE Stud (name varchar(50) NOT NULL, age INT(50), id int PRIMARY KEY NOT NULL AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO Stud (name, age) VALUES (%s,%s)",("Blake", 9))
# db.commit()
#
# mycursor.execute("CREATE TABLE test (name VARCHAR(255), created VARCHAR(255), gender VARCHAR(255))")
#
# mycursor.execute("INSERT INTO Test (name, created, gender) VALUES (%s,%s,%s)",("Joey", datetime.now(), "F"))
# db.commit()
#
# mycursor.execute("SELECT id, gender From Test WHERE first_name = 'Joe' ORDER BY id DESC")
# mycursor.execute("ALTER TABLE Test ADD COLUMN food VARCHAR(50) NOT NULL")
# mycursor.execute("ALTER TABLE Test CHANGE first_name first_name VARCHAR(4)")
# mycursor.execute('DESCRIBE ProductItems')
#
# mycursor.execute("CREATE TABLE Person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
# mycursor.execute("INSERT INTO Person (name, age) VALUES (%s,%s)", ("Joe", 22))
# db.commit()
# mycursor.execute("SELECT * FROM Person")
#
#
# mycursor.execute("CREATE TABLE Subjects (name varchar(50) NOT NULL, marks smallint NOT NULL)")
# mycursor.execute("INSERT INTO Subjects (name, marks) VALUES ('Karan',92)")
# db.commit()
#
# mycursor.execute("SELECT * FROM ProductItems")
# myresult = mycursor.fetchall()
# for x in myresult:
# 	print(x)
# for row in myresult:
# 	global ItemCost
# 	ItemCost = row;
#
# print(ItemCost)
#
# query1="SELECT COUNT(age) FROM Person"
# mycursor.execute(query1)
# cnt=mycursor.fetchone()
# print("Number of students :",cnt)
#
# query2="SELECT SUM(age) FROM Person "
# mycursor.execute(query2)
# sum=mycursor.fetchone()
# print(sum)
# abc = 1;
# print(abc)