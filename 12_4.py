import mysql.connector as ms
 #Establising Connection
id=int(input("Enter ID:"))
sql = "SELECT * FROM products WHERE id=%d"
con = ms.connect(
 host="localhost",
 user="root",
 password="1234",
 database="mydb"
 )

 #Getting Cursor Object
cursor=con.cursor()
cursor.execute(sql%(id,))
row=cursor.fetchone()
if row is not None:
    print(row)
else:
    print("Not Existed")
