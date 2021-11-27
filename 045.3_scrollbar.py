import tkinter as tk
import os
from tkinter.constants import BOTH, BOTTOM, HORIZONTAL, LEFT, NW, RIGHT, VERTICAL, X, Y
from tkinter import Event, ttk

# Scrollbar can work with these widgets

# X scroll
# Text
# Canvas
# Treeview
# Entry
# Spinbox
# Combobox

# Y scroll
# Text
# Canvas
# Treeview


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

        self.canvas = tk.Canvas(self.root)
        self.canvas.configure(scrollregion=(0, 0, self.width, self.height))
        self.canvas.bind('<Configure>', lambda event: self.canvas.configure(
            scrollregion=self.canvas.bbox('all')))

        self.vertical_scroll = tk.Scrollbar(
            self.root, orient=VERTICAL, command=self.canvas.yview)
        self.vertical_scroll.pack(side=RIGHT, fill=Y)
        self.canvas.config(yscrollcommand=self.vertical_scroll.set)

        self.horizontal_scroll = tk.Scrollbar(
            self.root, orient=HORIZONTAL, command=self.canvas.xview)
        self.horizontal_scroll.pack(side=BOTTOM, fill=X)
        self.canvas.config(xscrollcommand=self.horizontal_scroll.set)

        # pack the canvas after the horizontal scroll to position correctly

        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)

        if os.name == 'nt':
            self.canvas.bind('<MouseWheel>', lambda event: self.canvas.yview(
                'scroll', -1 if event.num == 4 else 1, 'units'))
        else:
            self.canvas.bind('<Button-4>', lambda event: self.canvas.yview(
                'scroll', -1 if event.num == 4 else 1, 'units'))
            self.canvas.bind('<Button-5>', lambda event: self.canvas.yview(
                'scroll', -1 if event.num == 4 else 1, 'units'))

        self.canvas.bind('<1>', self.canvas_click)

        # if we add the button before mainloop(), the canvas changes sizes
        # and the scrollbar doesn't work
        # self.add_button()
        self.root.after(1000, self.add_button)

    def add_button(self):
        button = tk.Button(self.canvas, text=f'Sample {5} {5}')
        self.canvas.create_window(50, 50, window=button, anchor=NW)

    def canvas_click(self, event: Event):
        # need to translate the event position to the canvas position
        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        button = tk.Button(self.canvas, text=f'Sample {x} {y}')
        self.canvas.create_window(x, y, window=button)

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
