import sqlite3
conn=sqlite3.connect("test.db")
data=conn.execute('select * from student')
for d in data:
   print(d) #prints in TUple
   print(d[0],d[1],d[2])
conn.close()