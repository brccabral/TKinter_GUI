import tkinter as tk
from tkinter import Label, Menu, ttk, filedialog
import os
from tkinter.constants import END
import pandas as pd
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

        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        self.tree = ttk.Treeview(self.frame)

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)

        self.file_menu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label='Spreadsheets', menu=self.file_menu)
        self.file_menu.add_command(label='Open', command=self.load_data)

        self.label = Label(self.root, text="")
        self.label.pack(pady=10)

    def load_data(self):
        self.filename = self.file_open()
        if not self.filename:
            logging.debug(f'no file selected')
            return
        logging.debug(f'{self.filename}')
        if not self.read_data():
            logging.debug(f'no data')
            return
        self.clear_tree()
        self.setup_tree()

    def file_open(self):
        logging.debug(f'file_open')
        filename = filedialog.askopenfilename(initialdir=".", title="Open a .xls", filetypes=(
            ("xlss files", "*.xlsx"), ("xls files", "*.xls")))
        if not filename:
            logging.debug(f'no file selected')
            return False
        # r string to avoid backslash \ escape
        filename = r"{}".format(filename)
        return filename

    def read_data(self):
        logging.debug(f'read_data')
        try:
            self.df = pd.read_excel(self.filename)
            logging.debug(f'{self.df.head()}')
            return True
        except ValueError:
            self.label.config(text="File couldn't be open")
        except FileNotFoundError:
            self.label.config(text="File couldn't be found")
        except Exception as ex:
            self.label.config(text=ex)

        return False

    def clear_tree(self):
        self.tree.delete(*self.tree.get_children())

    def setup_tree(self):
        self.tree.config(columns=list(self.df.columns), show="headings")
        # Loop thru column list for headers
        for column in self.tree['column']:
            self.tree.heading(column, text=column)

        # put data in treeview
        df_rows: list = self.df.to_numpy().tolist()
        for row in df_rows:
            self.tree.insert("", END, values=row)

        self.tree.pack(pady=10)

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("Excel Treeview", 700, 400)
    app.start()


if __name__ == "__main__":
    main()
