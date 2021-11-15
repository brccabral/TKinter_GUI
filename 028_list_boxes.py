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
root.geometry("600x800")

my_listbox = tk.Listbox(root, width=50)
my_listbox.pack(pady=15)
my_listbox.insert(END, "Item1")
my_listbox.insert(END, "Item2")
my_listbox.insert(0, "Item0")


item_list = ["One", "Two", "Three"]
for item in item_list:
    my_listbox.insert(END, item)

for i in range(50):
    my_listbox.insert(END, i)

my_listbox.insert(4, "New item")

def delete():
    my_listbox.delete(ANCHOR)
    my_label.config(text='')

def select():
    my_label.config(text=my_listbox.get(ANCHOR))

def delete_all():
    my_listbox.delete(0, END)

my_button = tk.Button(root, text="Delete", command=delete)
my_button.pack(pady=10)

my_button2 = tk.Button(root, text="Select", command=select)
my_button2.pack(pady=10)

my_label = tk.Label(root, text='')
my_label.pack(pady=5)

my_button3 = tk.Button(root, text="Delete all", command=delete_all)
my_button3.pack(pady=10)

root.mainloop()