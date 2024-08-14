# Write a python program to input an id and delete record matching that id from the database.
import sqlite3
def delete_record():
    conn = sqlite3.connect('college.db')
    # Prompt the user to input an ID to delete
    deleteid = int(input("Enter the ID of the record you want to delete: "))

    # Delete the record with the matching ID
    conn.execute('DELETE FROM student WHERE id = ?', (deleteid,))
    conn.commit()

    # Fetch and print the remaining records
    cursor = conn.execute("SELECT * FROM student")
    print("Remaining records:")
    for d in cursor:
       print(d[0],d[1],d[2],d[3])

    # Close the database connection
    conn.close()

delete_record()