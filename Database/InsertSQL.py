import mysql.connector
conn=mysql.connector.connect(host="localhost",
username="root",password="",database="pythondb")

mycursor=conn.cursor()
mycursor.execute('insert into student (id,name,faculty)values(1,"ram","BIM"),(2,"Shyam","BBA"),(3,"Sita","BCA")')
conn.commit()
conn.close()