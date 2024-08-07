import sqlite3
conn=sqlite3.connect('test.db')
conn.execute('Insert into student(id,name,faculty)values(1,"ram","BIM"),(2,"Shyam","BBA"),(3,"Sita","BCA")')
conn.commit()
conn.close()