import mysql.connector as myconn
mydb=myconn.connect(host="localhost",user="root",password="SHORK@w3#421",database="learncoding")
db_cursor=mydb.cursor()
db_cursor.execute("show tables")
for i in db_cursor:
    print(i)
    


