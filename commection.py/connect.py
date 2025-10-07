import mysql.connector as Myconn
myDb=Myconn.connect(host="localhost",user="root",password="SHORK@w3#421")
print(myDb,"established")