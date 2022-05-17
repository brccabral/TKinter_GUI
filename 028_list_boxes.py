import tkinter as tk
import os
from tkinter.constants import (
    ANCHOR,
    BROWSE,
    END,
    EXTENDED,
    MULTIPLE,
    RIGHT,
    VERTICAL,
    Y,
)

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("600x800")

# without scrollbar the list can be scrolled, but user won't notice
my_frame = tk.Frame(root)
my_scrollbar = tk.Scrollbar(my_frame, orient=VERTICAL)
# select mode = SINGLE, BROWSE, MULTIPLE, EXTENDED
# MULTIPLE = normal mouse click to select multiple
##   ANCHOR doesn't work
##   use my_listbox.curselection() to return indexes of selected items
# EXTENDED = can select multiple as long as they are in sequence
##   ANCHOR is the first item in the extended list, even if reversed
##   use my_listbox.curselection() to return indexes of selected items
# BROWSE = need another function to use it
my_listbox = tk.Listbox(
    my_frame, width=50, yscrollcommand=my_scrollbar.set, selectmode=MULTIPLE
)
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)
my_frame.pack()

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
    my_label.config(text="")


def select():
    my_label.config(text=my_listbox.get(ANCHOR))


def delete_all():
    my_listbox.delete(0, END)


# used with MULTIPLE
def select_all():
    result = []
    for item in my_listbox.curselection():
        result.append(f"{item}={my_listbox.get(item)}")
    my_label.config(text="\n".join(result))


def delete_multiple():
    # need reversed because at each delete all indexes change
    for item in reversed(my_listbox.curselection()):
        my_listbox.delete(item)


my_button = tk.Button(root, text="Delete single", command=delete)
my_button.pack(pady=10)

my_button2 = tk.Button(root, text="Show single selected", command=select)
my_button2.pack(pady=10)

my_label = tk.Label(root, text="")
my_label.pack(pady=5)

my_button3 = tk.Button(root, text="Delete all", command=delete_all)
my_button3.pack(pady=10)

my_button4 = tk.Button(root, text="Show all selected", command=select_all)
my_button4.pack(pady=10)

my_button5 = tk.Button(root, text="Delete all selected", command=delete_multiple)
my_button5.pack(pady=10)

root.mainloop()
