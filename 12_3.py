import mysql.connector as ms
 #Establising Connection
con = ms.connect(
 host="localhost",
 user="root",
 password="1234",
 database="mydb"
 )

 #Getting Cursor Object
cursor=con.cursor()
 #Execute SQL Queries
cursor.execute("SELECT * FROM products")
 #Fetch the result from Cursor object
data=cursor.fetchall()
for row in data:
    print(row)