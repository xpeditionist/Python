import mysql.connector as ms
con = ms.connect(
 host="localhost",
 user="root",
 passwd="1234",
 database="mydb"
)

cursor = con.cursor()
cursor.execute("CREATE TABLE products (id INT, name VARCHAR(255), price VARCHAR(10))")

cursor.execute("SHOW TABLES")
tables = cursor.fetchall()
for x in tables:
  print(x)

  
