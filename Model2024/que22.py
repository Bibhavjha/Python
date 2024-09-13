# assuming your own database and tables, write a program to insert and retrieve data from the database.
import sqlite3
conn=sqlite3.connect('test.db')
conn.execute('Insert into student(id,name,faculty) values(101,"chandan","BBM"),(102,"Charan","BBA")')
conn.commit()
conn.close()
conn=sqlite3.connect('test.db')
data=conn.execute('Select * from student')
for d in data:
   print(d) #prints in TUple
   print(d[0],d[1],d[2])
conn.close()

