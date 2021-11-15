import tkinter as tk
from tkinter import ttk
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

def clicked():
    myLabel = tk.Label(root, text=f"Clicked {dropVar.get()}")
    myLabel.pack()

def selected(event):
    myLabel = tk.Label(root, text=f"Selected {dropVar.get()}")
    myLabel.pack()

def comboclick(event):
    myLabel = tk.Label(root, text=f"Combo {myCombo.get()}")
    myLabel.pack()

options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Satuday",
    "Sunday"
]

dropVar = tk.StringVar()
dropVar.set(options[0])

drop = tk.OptionMenu(root, dropVar, *options, command=selected)
drop.pack(pady=20)

myButton = tk.Button(root, text="Select from list", command=clicked)
myButton.pack(pady=20)

myCombo = ttk.Combobox(root, values=options)
myCombo.current(0)
myCombo.bind("<<ComboboxSelected>>", comboclick)
myCombo.pack()

root.mainloop()