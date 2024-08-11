# create a GUI with a text box and two buttons (ok and clear).when ok is clicked,
# display "hello" in the text box. when clear is clicked, clear the text box
# delete function is used 
import tkinter as tk

# Function to display "hello" in the text box
def display_hello():
    text_box.delete("1.0", tk.END)  # Clear the text box first
    text_box.insert(tk.END, "hello")

# Function to clear the text box
def clear_text():
    text_box.delete("1.0", tk.END)

# Create the main window
window = tk.Tk()
window.title("Simple GUI")

# Create a text box
text_box = tk.Text(window)
text_box.pack()

# Create the "OK" button
ok_button = tk.Button(window, text="OK", command=display_hello)
ok_button.pack(side=tk.LEFT)

# Create the "Clear" button
clear_button = tk.Button(window, text="Clear", command=clear_text)
clear_button.pack(side=tk.RIGHT)

# Start the main event loop
window.geometry('400x400')
window.mainloop()
