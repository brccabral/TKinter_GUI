import tkinter as tk
import os
from tkinter.constants import ANCHOR, END

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

my_listbox = tk.Listbox(root)
my_listbox.pack(pady=15)
my_listbox.insert(END, "Item1")
my_listbox.insert(END, "Item2")
my_listbox.insert(0, "Item0")


item_list = ["One", "Two", "Three"]
for item in item_list:
    my_listbox.insert(END, item)

my_listbox.insert(4, "New item")

def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text='')

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

my_button = tk.Button(root, text="Delete", command=delete)
my_button.pack(pady=10)

my_button2 = tk.Button(root, text="Select", command=select)
my_button2.pack(pady=10)

my_label = tk.Label(root, text='')
my_label.pack(pady=5)

root.mainloop()