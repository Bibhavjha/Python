import sqlite3
conn=sqlite3.connect("test.db")
conn.execute('update  student set faculty="csit" where id=3')
conn.commit()
conn.close()