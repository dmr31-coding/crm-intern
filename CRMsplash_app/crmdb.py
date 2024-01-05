import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "rootyahoo",
    
)

# prepare a cursor object 
cursorObject = database.cursor()

# create a database 
cursorObject.execute("CREATE DATABASE crmsplash_db")

print("All done!")