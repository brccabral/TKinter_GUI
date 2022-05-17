import tkinter as tk
import os
from tkinter.constants import ACTIVE, ANCHOR, END, SEL
import logging

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

        self.label = tk.Label(self.root, text="Start typing")
        self.label.pack(padx=5, pady=5)

        self.entry = tk.Entry(self.root)
        self.entry.pack(padx=5, pady=5)

        self.entry.bind("<KeyRelease>", self.search_list)

        self.toppings = [
            "Pepperoni",
            "Peppers",
            "Mushrooms",
            "Cheese",
            "Onions",
            "Ham",
            "Taco",
        ]
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack(padx=5, pady=5)
        self.listbox.bind("<<ListboxSelect>>", self.fill_entry)

        self.update_list(self.toppings)

    def search_list(self, event: tk.Event):
        content = self.entry.get()
        if not content:
            data = self.toppings
        else:
            data = []
            for item in self.toppings:
                if content.lower() in item.lower():
                    data.append(item)
        self.update_list(data)

    def fill_entry(self, event: tk.Event):
        self.entry.delete(0, END)
        self.entry.insert(0, self.listbox.get(ANCHOR))

    def update_list(self, toppings: list):
        self.listbox.delete(0, END)
        self.listbox.insert(END, *toppings)

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
    app = TkinterApp("TkinterApp", 700, 500)
    app.start()


if __name__ == "__main__":
    main()
