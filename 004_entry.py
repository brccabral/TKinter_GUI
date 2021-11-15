import tkinter as tk
from tkinter.constants import END

root = tk.Tk()
root.geometry("400x400")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))

e = tk.Entry(root, width=50, bg="red", fg="white", borderwidth=10)
e.pack()
e.insert(0, "Name here: ")

def myClick():
    myLabel = tk.Label(root, text="Hello " + e.get())
    e.delete(0, END)
    myLabel.pack()

myButton = tk.Button(root, text="Enter you name!", padx=50, pady=25, command=myClick)
myButton.pack()

root.mainloop()