import tkinter as tk
import os
from tkinter import Event, Frame, Listbox, ttk
import logging
from tkinter.constants import ANCHOR, END
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG)


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
        self.root.iconphoto(self.root._w, tk.PhotoImage(file='python3.png'))

        self.size_colors = {"Small": ["Red", "Green", "Blue", "Black"],
                            "Medium": ["Red", "Green"],
                            "Large": ["Blue", "Black"]
                            }

        self.size_combo = ttk.Combobox(
            self.root, values=list(self.size_colors.keys()))
        self.size_combo.current(0)
        self.size_combo.pack(pady=20)

        self.size_combo.bind("<<ComboboxSelected>>", self.combo_selected)

        self.color_combo = ttk.Combobox(
            self.root, values=self.size_colors["Small"])
        self.color_combo.current(0)
        self.color_combo.pack(pady=20)

        self.frame = Frame(self.root)
        self.frame.pack(pady=50)

        self.size_list = Listbox(self.frame)
        self.size_list.grid(row=0, column=0)

        self.size_list.bind("<<ListboxSelect>>", self.list_selected)

        self.size_list.insert(END, *self.size_colors.keys())

        self.color_list = Listbox(self.frame)
        self.color_list.grid(row=0, column=1, padx=20)

    def combo_selected(self, event: Event):
        size = self.size_combo.get()
        self.color_combo.config(values=self.size_colors[size])
        # if you don't select current, previous selected value will remain
        self.color_combo.current(0)

    def list_selected(self, event: Event):
        size = self.size_list.get(ANCHOR)
        self.color_list.delete(0, END)
        self.color_list.insert(END, *self.size_colors[size])

    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}")


def main():
    app = TkinterApp("TkinterApp", 700, 500)
    app.start()


if __name__ == "__main__":
    main()
