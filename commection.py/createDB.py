import mysql.connector as myconn
myDb=myconn.connect(host="localhost",user="root",password="SHORK@w3#421")
db_cursor=myDb.cursor()
db_cursor.execute("create database learncoding")
