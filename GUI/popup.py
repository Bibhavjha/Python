# create a GUI with a text box and a button when the buttton is clicked  check value of text box and print 
# odd even in a message box
import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self,window):
        self.lbl1=tk.Label(window,text="Num")
        self.lbl1.place(x=10,y=30)
        self.txt1=tk.Entry(window,width=30)
        self.txt1.place(x=50,y=30)
        self.btn1=tk.Button(window,text='Check',command=self.check)
        self.btn1.place(x=50,y=50)
    def check(self):
        a=int(self.txt1.get())
        if(a%2==0):
            messagebox.showinfo("oddEvenCheck",'Even')
        else:
            messagebox.showinfo("oddEvenCheck",'Odd')

window=tk.Tk()
window.geometry('400x400')
ob=GUI(window)
window.mainloop()