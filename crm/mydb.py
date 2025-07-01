import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '1234',
)


# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create the database
cursorObject.execute("CREATE DATABASE db")

print('All Done, The database is created!')