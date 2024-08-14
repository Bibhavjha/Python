# Write a program to insert any 5 records (id, name, address, faculty) to a table 'student'.
import sqlite3
conn=sqlite3.connect('college.db')
print('database created')
conn.execute('create table student(id int primary key,name varchar(20) not null,address varchar(50) not null,faculty varchar(20) not null)')
print('table creation succesfull')
conn.execute('Insert into student(id,name,address,faculty)values(1,"ram","ktm","BIM"),(2,"Shyam","brt","BBA"),(3,"Sita","pkr","BCA"),(4,"Hari","Ilam","BIM"),(5,"Gita","BKt","BBA")')
conn.commit()
conn.close()