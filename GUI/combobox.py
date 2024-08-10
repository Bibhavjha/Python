import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox
import mysql.connector

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

        self.xlbl3 = tk.Label(window, text="Faculty")
        self.xlbl3.place(x=20, y=80)
        self.cmb = Combobox(window, values=['BIM', 'CSIT', 'BBA', "BSW"])
        self.cmb.place(x=80, y=80)

        self.txt3 = tk.Text(window, width=40, height=10)
        self.txt3.place(x=20, y=160)

        self.btn1 = tk.Button(window, text="Save", command=self.save)
        self.btn1.place(x=20, y=120)
        self.btn2 = tk.Button(window, text="Show Records", command=self.show)
        self.btn2.place(x=80, y=120)

    def save(self):
        id = int(self.txt1.get())
        name = self.txt2.get()
        faculty = self.cmb.get()
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='',
            database='pythondb'
        )
        mycursor = conn.cursor()
        mycursor.execute(f'INSERT INTO student (id, name, faculty) VALUES ({id},"{name}","{faculty}")')
        conn.commit()
        conn.close()
        messagebox.showinfo("Title", "Record Saved")

    def show(self):
        conn = mysql.connector.connect(
            host='localhost',
            username='root',
            password='',
            database='pythondb'
        )
        mycursor = conn.cursor()
        mycursor.execute('SELECT * FROM student')
        data = mycursor.fetchall()
        s = ""
        for d in data:
            for m in d:
               s += str(m)
               s+=''
            s+='\n'
        conn.close()
      
        self.txt3.insert(tk.END, s)

window = tk.Tk()
window.geometry('400x400')
ob = GUI(window)
window.mainloop()