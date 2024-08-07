import sqlite3
conn=sqlite3.connect("test.db")
conn.execute('create table student(id int primary key,name varchar(20) not null,faculty varchar(20) not null)')
print('table creation succesfull')
conn.close()