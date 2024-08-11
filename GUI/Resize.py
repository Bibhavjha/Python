# to prevent resizing
# import tkinter as tk
# window=tk.Tk()
# window.resizable(False,False)
# window.geometry('400x400')
# window.mainloop()

# to set size of window
# import tkinter as tk
# window=tk.Tk()
# window.resizable(False,False)
# window.geometry('400x400')
# window.minsize(width=400,height=400)
# window.mainloop()

# to change bgcolor
import tkinter as tk
window=tk.Tk()
window.resizable(False,False)
window.geometry('400x400')
window.minsize(width=400,height=400)
# window.config(bg='blue')
window['bg']='yellow'
window.mainloop()


