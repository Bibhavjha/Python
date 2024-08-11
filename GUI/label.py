# create the follwoing GUI and perform respective operations on button click
import tkinter as tk

class GUI:
    def __init__(self,window):
        self.lbl1=tk.Label(window,text="Num1")
        self.lbl1.place(x=10,y=30)
        self.lbl2=tk.Label(window,text="Num2")
        self.lbl2.place(x=10,y=60)
        self.lbl3=tk.Label(window,text="Result")
        self.lbl3.place(x=10,y=90)
        self.txt1=tk.Entry(window,width=30)
        self.txt1.place(x=50,y=30)
        self.txt2=tk.Entry(window,width=30)
        self.txt2.place(x=50,y=60)
        self.txt3=tk.Entry(window,width=30)
        self.txt3.place(x=50,y=90)
        self.btn1=tk.Button(window,text='Add',command=self.add)
        self.btn1.place(x=50,y=110)
        self.btn2=tk.Button(window,text='Sub',command=self.sub)
        self.btn2.place(x=100,y=110)
        self.btn3=tk.Button(window,text='mul',command=self.mul)
        self.btn3.place(x=150,y=110)
        self.btn4=tk.Button(window,text='Div',command=self.div)
        self.btn4.place(x=200,y=110)
    def add(self):
        a=int(self.txt1.get())
        b=int(self.txt2.get())
        self.txt3.delete(0,tk.END)
        c=a+b
        self.txt3.insert(0,c)
    def sub(self):
        a=int(self.txt1.get())
        b=int(self.txt2.get())
        c=a-b
        self.txt3.delete(0,tk.END)
        self.txt3.insert(0,c)
    def mul(self):
        a=int(self.txt1.get())
        b=int(self.txt2.get())
        c=a*b
        self.txt3.delete(0,tk.END)
        self.txt3.insert(0,c)
    def div(self):
        a=int(self.txt1.get())
        b=int(self.txt2.get())
        c=a/b
        self.txt3.delete(0,tk.END)
        self.txt3.insert(0,c)
window=tk.Tk()
window.geometry('400x400')
ob=GUI(window)
window.mainloop()
