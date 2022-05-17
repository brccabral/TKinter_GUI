from tkinter import Listbox, filedialog
import pickle
import tkinter as tk
import os
import logging
from tkinter.constants import END

logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, height=400):
        self.appname = appname
        self.width = width
        self.height = height

        self.root = tk.Tk()

        self.root.title(self.appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file="python3.png"))

        self.sizes = ["Small", "Medium", "Large"]

        self.text = tk.Text(self.root, width=40, height=10)
        self.text.pack(pady=(20, 0))

        self.button1 = tk.Button(self.root, text="Save File", command=self.save_file)
        self.button1.pack(pady=10)
        self.button2 = tk.Button(self.root, text="Open File", command=self.open_file)
        self.button2.pack(pady=10)

        self.listbox = Listbox(self.root)
        self.listbox.pack(pady=20)
        self.listbox.insert(END, *self.sizes)

        self.button3 = tk.Button(self.root, text="Clear list", command=self.clear_list)
        self.button3.pack(padx=5, pady=5)

        self.button4 = tk.Button(self.root, text="Load list", command=self.load_list)
        self.button4.pack(padx=5, pady=5)

        self.button5 = tk.Button(self.root, text="Save list", command=self.save_list)
        self.button5.pack(padx=5, pady=5)

    def save_list(self):
        filename = filedialog.asksaveasfilename(
            initialdir=".", filetypes=(("DAT files", "*.dat"),)
        )
        if not filename:
            return
        content = self.listbox.get(0, END)
        if not content:
            return
        with open(filename, "wb") as f:
            pickle.dump(content, f)

    def load_list(self):
        filename = filedialog.askopenfilename(
            initialdir=".", filetypes=(("DAT Files", "*.dat"),)
        )
        if not filename:
            return
        content = []
        with open(filename, "rb") as f:
            content = pickle.load(f)
        if not content:
            return
        self.listbox.insert(END, *content)

    def clear_list(self):
        self.listbox.delete(0, END)

    def save_file(self):
        logging.debug(f"save")
        content = self.text.get(1.0, END)
        if not content:
            return
        filename = filedialog.asksaveasfilename(
            initialdir=".", filetypes=(("DAT files", "*.dat"),)
        )
        if not filename:
            return
        with open(filename, "wb") as f:
            pickle.dump(content, f)

    def open_file(self):
        logging.debug(f"open")
        filename = filedialog.askopenfilename(
            initialdir=".", filetypes=(("DAT files", "*.dat"),)
        )
        if not filename:
            return
        content = ""
        with open(filename, "rb") as f:
            content = pickle.load(f)
        if not content:
            return
        self.text.insert(1.0, content)

    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}"
        )


def main():
    app = TkinterApp("TkinterApp", 700, 700)
    app.start()


if __name__ == "__main__":
    main()
