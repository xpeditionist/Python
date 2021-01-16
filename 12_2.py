import mysql.connector as ms
try:
  id = int(input("Enter Id: "))
  name=input("Enter Name: ")
  price=int(input("Enter price: "))
  sql="insert into products values(%d,'%s','%s')"
  con = ms.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="mydb")
  cursor=con.cursor()
  cursor.execute(sql%(id,name,price))
  con.commit()
  print("Record Inserted Successfully")

except ms.DatabaseError as e:
  if con:
    con.rollback()
    print("There is a problem with sql",e)
finally:
  if cursor:
    cursor.close()
  if con:
    con.close()

