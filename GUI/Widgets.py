# widgets-> component that are placed in a window/frame
# import tkinter as tk
# class GUI:
#     def __init__(self,window):
#         self.txt1=tk.Entry(window,width=30)
#         # self.txt1.pack()normally not used
#         self.txt1.place(x=20,y=20)
#         self.btn2=tk.Button(window,text='Click')
#         self.btn2.place(x=20,y=50)
# window=tk.Tk()
# window.geometry('400x400')
# ob=GUI(window)
# window.mainloop()


# function that call after occurance of event is called callback function for example somthing is shown after clicking button
# function with button

# create a gui with a text box and a button. when clicked diplay 'you clicked button' in the textbox
import tkinter as tk
class GUI:
    def __init__(self,window):
        self.txt1=tk.Entry(window,width=30)
        # self.txt1.pack()normally not used
        self.txt1.place(x=20,y=20)
        self.btn2=tk.Button(window,text='Click',command=self.show)
        self.btn2.place(x=20,y=50)
    def show(self):
        self.txt1.insert(0,'you clicked button')

window=tk.Tk()
window.geometry('400x400')
ob=GUI(window)
window.mainloop()
