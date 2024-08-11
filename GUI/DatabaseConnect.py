import tkinter as tk
import mysql.connector
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


        self.xlbl3 = tk.Label(window, text="Faculty")
        self.xlbl3.place(x=20, y=80)
        self.cmb = Combobox(window,values=['BIM', 'CSIT', 'BBA', 'BSW'])
        self.cmb.place(x=80, y=80)

        self.btn1 = tk.Button(window, text="Save", command=self.save)
        self.btn1.place(x=20, y=120)

        

# Database sanga connect gareko
    def save(self):
        id=int(self.txt1.get())
        name=self.txt2.get()
        faculty=self.cmb.get()
        con=mysql.connector.connect(host='localhost',username='root',password='',database='pythondb')
        mycursor=con.cursor()
        mycursor.execute(f'insert into student(id,name,faculty) values({id},"{name}","{faculty}")')
        con.commit()
        con.close()
        messagebox.showinfo("title","Record saved")
        

window = tk.Tk()
window.geometry('400x400')
ob = GUI(window)
window.mainloop()