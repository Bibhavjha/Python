import sqlite3
conn=sqlite3.connect("test.db")
conn.execute('Delete from student where id=1')
conn.commit()
conn.close()