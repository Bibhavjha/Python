import mysql.connector
conn=mysql.connector.connect(host="localhost",
username="root",password="",database="pythondb")

mycursor=conn.cursor()
mycursor.execute("select * from student")
data=mycursor.fetchall()
for d in data:
    print(d[0],d[1],d[2])
conn.close()