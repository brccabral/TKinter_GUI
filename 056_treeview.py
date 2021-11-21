import tkinter as tk
from tkinter import ttk
import os
from tkinter.constants import CENTER, END, NO, W
from itertools import count

class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, heigth=400):
        self.root = tk.Tk()
        self.appname = appname
        self.root.title(appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file='python3.png'))
        self.root.geometry(f"{width}x{heigth}")

        self.iid = count()

        self.tree = ttk.Treeview(self.root)
        
        self.tree.config(columns=("Name", "ID", "Favorite Pizza"))
        self.tree.column("#0", width=0, stretch=NO) # used for Parent/Children
        self.tree.column("Name", anchor=W, width=120)
        self.tree.column("ID", anchor=CENTER, width=80)
        self.tree.column("Favorite Pizza", anchor=W, width=120)

        self.tree.heading("#0", text="Label", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("ID", text="ID", anchor=CENTER)
        self.tree.heading("Favorite Pizza", text="Favorite Pizza", anchor=W)

        self.tree.pack(pady=20)

    def insert_data(self, name, id, flavor, parent="", index=END, iid: int =None, text=""):
        if iid is None:
            iid = next(self.iid)
        
        self.tree.insert(parent=parent, index=index, iid=iid, text=text, values=(name, id, flavor))

    def start(self):
        self.root.mainloop()

def main():
    app = TkinterApp("Treeview", 500, 500)
    app.insert_data("John", 1, "Pepperoni")
    app.insert_data("Mary", 2, "Cheese")
    app.insert_data("Tina", 3, "Ham")
    app.insert_data("Bob", 4, "Supreme")
    app.insert_data("Erin", 5, "Cheese")
    app.insert_data("Wes", 6, "Onion")
    app.insert_data("Steve", 1.2, "Peppers", parent=0, index=0)
    app.insert_data("Lara", 2.2, "Corn", parent=1, index=0)
    app.start()

if __name__ == "__main__":
    main()