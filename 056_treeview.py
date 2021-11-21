from tkinter import messagebox
import tkinter as tk
from tkinter import Button, Entry, Frame, Label, ttk
import os
from tkinter.constants import CENTER, END, NO, W
from itertools import count
from typing import Union
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG)


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

        self.tree.config(columns=("Name", "ID", "Topping"))
        self.tree.column("#0", width=0, stretch=NO)  # used for Parent/Children
        self.tree.column("Name", anchor=W, width=140)
        self.tree.column("ID", anchor=CENTER, width=100)
        self.tree.column("Topping", anchor=W, width=140)

        self.tree.heading("#0", text="Label", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("ID", text="ID", anchor=CENTER)
        self.tree.heading("Topping", text="Topping", anchor=W)

        self.tree.pack(pady=20)

        self.insert_frame = Frame(self.root)
        self.insert_frame.pack(pady=10)

        self.name_label = Label(self.insert_frame, text="Name")
        self.name_label.grid(row=0, column=0)
        self.id_label = Label(self.insert_frame, text="ID")
        self.id_label.grid(row=0, column=1)
        self.topping_label = Label(self.insert_frame, text="Topping")
        self.topping_label.grid(row=0, column=2)

        self.name_entry = Entry(self.insert_frame)
        self.name_entry.grid(row=1, column=0)
        self.id_entry = Entry(self.insert_frame)
        self.id_entry.grid(row=1, column=1)
        self.topping_entry = Entry(self.insert_frame)
        self.topping_entry.grid(row=1, column=2)

        self.insert_button = Button(
            self.root, text="Insert record", command=self.insert_record)
        self.insert_button.pack(pady=10)

        self.remove_all_button = Button(
            self.root, text="Remove all", command=self.remove_all)
        self.remove_all_button.pack(pady=10)

        self.remove_one_button = Button(
            self.root, text="Remove one", command=self.remove_one)
        self.remove_one_button.pack(pady=10)

        self.remove_many_button = Button(
            self.root, text="Remove many", command=self.remove_many)
        self.remove_many_button.pack(pady=10)

    def remove_all(self):
        for record in self.tree.get_children():
            self.tree.delete(record)

    def remove_one(self):
        if not self.tree.selection():
            logging.debug(f'no selection')
            return
        record = self.tree.selection()[0]
        self.tree.delete(record)

    def remove_many(self):
        if not self.tree.selection():
            logging.debug(f'no selection')
            return
        for record in self.tree.selection():
            self.tree.delete(record)

    def insert_record(self):
        if not self.name_entry.get() or not self.id_entry.get() or not self.topping_entry.get():
            messagebox.showerror("Treeview", "One or more entries is blank")
            return

        self.insert_data(self.name_entry.get(),
                         self.id_entry.get(), self.topping_entry.get())
        self.name_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.topping_entry.delete(0, END)

    def insert_data(self, name: str, id: Union[str, int], topping: str, parent="", index=END, iid: int = None, text=""):
        if iid is None:
            iid = next(self.iid)

        self.tree.insert(parent=parent, index=index, iid=iid,
                         text=text, values=(name, id, topping))

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("Treeview", 500, 600)
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
