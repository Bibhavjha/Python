# Create a GUI to input id, name, address,faculty with 3 text box, 1 combox box (for faculty) and a button (save). When button is clicked save the provided information to the database.
import tkinter as tk
import sqlite3
from tkinter.ttk import Combobox
from tkinter import messagebox

class GUI:
    def __init__(self, window):
        self.xlbl1 = tk.Label(window, text="Id")
        self.xlbl1.place(x=20, y=20)
        self.txt1 = tk.Entry(window, width=30)
        self.txt1.place(x=80, y=20)

        self.xlbl2 = tk.Label(window, text="Name")
        self.xlbl2.place(x=20, y=50)
        self.txt2 = tk.Entry(window, width=30)
        self.txt2.place(x=80, y=50)

        self.xlbl3 = tk.Label(window, text="Address")
        self.xlbl3.place(x=20, y=80)
        self.txt3 = tk.Entry(window, width=30)
        self.txt3.place(x=80, y=80)

        # Faculty
        self.xlbl4 = tk.Label(window, text="Faculty")
        self.xlbl4.place(x=20, y=110)
        self.cmb = Combobox(window, values=['BIM', 'BCA', 'BIT'])
        self.cmb.place(x=80, y=110)

        self.btn1 = tk.Button(window, text="Save", command=self.save)
        self.btn1.place(x=20, y=150)

    def save(self):
        id = int(self.txt1.get())
        name = self.txt2.get()
        address = self.txt3.get()
        faculty = self.cmb.get()

        # Connect to the SQLite database
        con = sqlite3.connect('college.db')
        cursor = con.cursor()

    #    create table
        # con.execute('create table student(id int primary key,name varchar(20) not null,address varchar(20),faculty varchar(20) not null)')
        # print('table creation succesfull')
        # con.close()
       # Insert data into the SQLite database
        cursor.execute(
                'INSERT INTO student (id, name, address, faculty) VALUES (?, ?, ?, ?)',
                (id, name, address, faculty)
            )
        con.commit()
        messagebox.showinfo("Success", "Record saved successfully")
        
        con.close()

# Main window setup
window = tk.Tk()
window.geometry('400x400')
ob = GUI(window)
window.mainloop()