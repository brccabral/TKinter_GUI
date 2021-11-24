import tkinter as tk
import os
from tkinter import ttk
from tkinter.constants import EW, NSEW, NW, SE, SW, TOP

class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, height=400):
        self.appname = appname
        self.width = width
        self.height = height

        self.root = tk.Tk()
        self.root.geometry(
                    f"{self.width}x{self.height}")

        self.root.title(self.appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file='python3.png'))

        self.root.resizable(width=True, height=True)

        self.root.pack_propagate(False)

        self.frame = tk.Frame(self.root, width=self.width, height=self.height, background="green")
        self.frame.pack(padx=5, pady=5)
        self.frame.pack_propagate(False)
        self.frame.grid_propagate(False)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)
        
        self.frame_grid = tk.Frame(self.frame, highlightbackground="black", highlightthickness=1)
        self.frame_grid.grid(row=0, column=0, sticky=NSEW)
        self.frame_grid.grid_columnconfigure(0, weight=1)
        self.frame_grid.grid_rowconfigure(0, weight=1)
        self.frame_grid.grid_rowconfigure(1, weight=1)

        self.frame_pack = tk.Frame(self.frame, highlightbackground="red", highlightthickness=1)
        self.frame_pack.grid(row=0, column=1, sticky=NSEW)
        
        # Using grid
        self.label_grid = tk.Label(self.frame_grid, text='Hello World')
        self.label_grid.grid(row=0, column=0)
        self.sizegrip_grid = ttk.Sizegrip(self.frame_grid)
        self.sizegrip_grid.grid(row=1, sticky=NW)
        
        # Using pack
        self.label_pack = tk.Label(self.frame_pack, text='Hello World')
        self.label_pack.pack(padx=5, pady=5)
        self.sizegrip_pack = ttk.Sizegrip(self.frame_pack)
        self.sizegrip_pack.pack(side=TOP, anchor=NW)

    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}")


def main():
    app = TkinterApp("Sizegrip", 700, 500)
    app.start()


if __name__ == "__main__":
    main()
