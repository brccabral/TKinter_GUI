from configparser import ConfigParser
from tkinter import Event, Menu, Scrollbar, messagebox
import tkinter as tk
from tkinter import Button, Entry, Frame, Label, ttk, colorchooser
import os
from tkinter.constants import BROWSE, CENTER, END, NO, NONE, RIGHT, W, Y
from itertools import count
from typing import Union
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG)


class TkinterApp:

    def change_color_oddrow(self):
        rgb, color_hex = colorchooser.askcolor()
        if not color_hex:
            return
        self.tree.tag_configure('oddrow', background=color_hex)
        self.configurations.set('color', 'oddrow', color_hex)

        with open(self.config_file, 'w') as configfile:
            self.configurations.write(configfile)

    def change_color_evenrow(self):
        rgb, color_hex = colorchooser.askcolor()
        if not color_hex:
            return
        self.tree.tag_configure('evenrow', background=color_hex)
        self.configurations.set('color', 'evenrow', color_hex)

        with open(self.config_file, 'w') as configfile:
            self.configurations.write(configfile)

    def change_color_selectedrow(self):
        rgb, color_hex = colorchooser.askcolor()
        if not color_hex:
            return
        self.style.map(self.appname, background=[('selected', color_hex)])
        self.configurations.set('color', 'selectedrow', color_hex)

        with open(self.config_file, 'w') as configfile:
            self.configurations.write(configfile)

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

        self.config_file = "treeview.ini"
        self.configurations = ConfigParser()
        self.configurations.read(self.config_file)
        oddrow_color = self.configurations.get('color', 'oddrow')
        evenrow_color = self.configurations.get('color', 'evenrow')
        selectedrow_color = self.configurations.get('color', 'selectedrow')

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.color_menu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Colors", menu=self.color_menu)
        self.color_menu.add_command(
            label='Change oddrow color', command=self.change_color_oddrow)
        self.color_menu.add_command(
            label='Change evenrow color', command=self.change_color_evenrow)
        self.color_menu.add_command(
            label='Change selectedrow color', command=self.change_color_selectedrow)
        self.color_menu.add_separator()
        self.color_menu.add_command(label="Exit", command=self.root.quit)

        self.iid = count()

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(self.appname, background="silver",
                             foreground="black", rowheight=25, fieldbackground="grey")
        self.style.map(self.appname, background=[
                       ('selected', selectedrow_color)])

        self.tree_frame = Frame(self.root)
        self.tree_frame.pack(pady=10)

        self.tree_scroll = Scrollbar(self.tree_frame)
        self.tree_scroll.pack(side=RIGHT, fill=Y)

        self.tree = ttk.Treeview(
            self.tree_frame, yscrollcommand=self.tree_scroll.set)
        # self.tree.config(selectmode=NONE) # disables selection
        # self.tree.config(selectmode=BROWSE) # allows select only one item

        self.tree_scroll.config(command=self.tree.yview)

        self.tree.config(columns=("Name", "ID", "Topping"))
        # used for Parent/Children
        self.tree.column("#0", width=20, stretch=NO)
        self.tree.column("Name", anchor=W, width=140)
        self.tree.column("ID", anchor=CENTER, width=100)
        self.tree.column("Topping", anchor=W, width=140)

        self.tree.heading("#0", text="", anchor=W)
        self.tree.heading("Name", text="Name", anchor=W)
        self.tree.heading("ID", text="ID", anchor=CENTER)
        self.tree.heading("Topping", text="Topping", anchor=W)

        self.tree.tag_configure('oddrow', background=oddrow_color)
        self.tree.tag_configure('evenrow', background=evenrow_color)

        self.tree.pack()

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

        self.move_frame = Frame(self.root)
        self.move_frame.pack(pady=10)

        self.move_up_button = Button(
            self.move_frame, text="Move up", command=self.move_up)
        self.move_up_button.grid(row=0, column=0)

        self.move_down_button = Button(
            self.move_frame, text="Move down", command=self.move_down)
        self.move_down_button.grid(row=0, column=1)

        self.edit_buttons_frame = Frame(self.root)
        self.edit_buttons_frame.pack(pady=10)

        self.insert_button = Button(
            self.edit_buttons_frame, text="Insert record", command=self.insert_record)
        self.insert_button.grid(row=0, column=0, padx=5)

        self.select_button = Button(
            self.edit_buttons_frame, text="Select record", command=self.select_record)
        self.select_button.grid(row=0, column=1, padx=5)

        self.update_button = Button(
            self.edit_buttons_frame, text="Update record", command=self.update_record)
        self.update_button.grid(row=0, column=2, padx=5)

        self.remove_buttons_frame = Frame(self.root)
        self.remove_buttons_frame.pack(pady=10)

        self.remove_all_button = Button(
            self.remove_buttons_frame, text="Remove all", command=self.remove_all)
        self.remove_all_button.grid(row=0, column=0, padx=5)

        self.remove_one_button = Button(
            self.remove_buttons_frame, text="Remove one", command=self.remove_one)
        self.remove_one_button.grid(row=0, column=1, padx=5)

        self.remove_many_button = Button(
            self.remove_buttons_frame, text="Remove many", command=self.remove_many)
        self.remove_many_button.grid(row=0, column=2, padx=5)

        # self.tree.bind("<Double-1>", func=self.clicker)
        # the Button-1 gets called before focus(), so, nothing is selected yet
        # need to be ButtonRelease-1
        # self.tree.bind("<Button-1>", func=self.clicker)
        self.tree.bind("<ButtonRelease-1>", func=self.clicker)

    def move_up(self):
        rows = self.tree.selection()
        if not rows:
            logging.debug(f'nothing selected')
            return

        for row in rows:
            self.tree.move(row, self.tree.parent(row), self.tree.index(row)-1)

    def move_down(self):
        rows = self.tree.selection()
        if not rows:
            logging.debug(f'nothing selected')
            return

        # need reversed() in case two selections are in sequence
        for row in reversed(rows):
            self.tree.move(row, self.tree.parent(row), self.tree.index(row)+1)

    def clicker(self, event: Event):
        self.select_record()

    def update_record(self):
        selected = self.tree.focus()
        if not selected:
            logging.debug(f'no selection')
            return

        if not self.name_entry.get() or not self.id_entry.get() or not self.topping_entry.get():
            messagebox.showerror("Treeview", "One or more entries is blank")
            return

        name = self.name_entry.get()
        id = self.id_entry.get()
        topping = self.topping_entry.get()

        self.tree.item(selected, values=(name, id, topping))

        self.name_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.topping_entry.delete(0, END)

    def select_record(self):
        selected = self.tree.focus()
        if not selected:
            logging.debug(f'no selection')
            return

        self.name_entry.delete(0, END)
        self.id_entry.delete(0, END)
        self.topping_entry.delete(0, END)

        name, id, topping = self.tree.item(selected, 'values')
        self.name_entry.insert(0, name)
        self.id_entry.insert(0, id)
        self.topping_entry.insert(0, topping)

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

        if parent:
            tag = self.tree.item(parent, 'tag')
        else:
            tag = 'evenrow' if len(
                self.tree.get_children()) % 2 == 0 else 'oddrow'
        self.tree.insert(parent=parent, index=index, iid=iid,
                         text=text, values=(name, id, topping), tags=tag)

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("Treeview", 600, 700)
    app.insert_data("John", 1, "Pepperoni")
    app.insert_data("Mary", 2, "Cheese")
    app.insert_data("Tina", 3, "Ham")
    app.insert_data("Bob", 4, "Supreme")
    app.insert_data("Erin", 5, "Cheese")
    app.insert_data("Wes", 6, "Onion")
    app.insert_data("Steve", 1.2, "Peppers", parent=0, index=0)
    app.insert_data("John", 1, "Pepperoni")
    app.insert_data("Lara", 2.2, "Corn", parent=1, index=0)
    app.insert_data("Mary", 2, "Cheese")
    app.insert_data("Tina", 3, "Ham")
    app.insert_data("Bob", 4, "Supreme")
    app.insert_data("Erin", 5, "Cheese")
    app.insert_data("Wes", 6, "Onion")
    app.insert_data("John", 1, "Pepperoni")
    app.insert_data("Mary", 2, "Cheese")
    app.insert_data("Tina", 3, "Ham")
    app.insert_data("Bob", 4, "Supreme")
    app.insert_data("Erin", 5, "Cheese")
    app.insert_data("Wes", 6, "Onion")
    app.insert_data("John", 1, "Pepperoni")
    app.insert_data("Mary", 2, "Cheese")
    app.insert_data("Tina", 3, "Ham")
    app.insert_data("Bob", 4, "Supreme")
    app.insert_data("Erin", 5, "Cheese")
    app.insert_data("Wes", 6, "Onion")
    app.insert_data("John", 1, "Pepperoni")
    app.insert_data("Mary", 2, "Cheese")
    app.insert_data("Tina", 3, "Ham")
    app.insert_data("Bob", 4, "Supreme")
    app.insert_data("Erin", 5, "Cheese")
    app.insert_data("Wes", 6, "Onion")
    app.start()


if __name__ == "__main__":
    main()
