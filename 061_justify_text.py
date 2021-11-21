import tkinter as tk
import os
from tkinter.constants import LEFT, RIGHT, SUNKEN


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

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(
            f"{width}x{heigth}+{screen_width//2-width//2}+{screen_height//2-heigth//2}")

        demo_text = "Stuff\nStuff Stuff\nStuff Stuff Stuff"
        label = tk.Label(self.root, text=demo_text, font=(
            'DejaVu Sans', 18), bd=1, relief=SUNKEN)
        label.pack(pady=10)
        label = tk.Label(self.root, text=demo_text, font=(
            'DejaVu Sans', 18), bd=1, relief=SUNKEN, justify=LEFT)
        label.pack(pady=10)
        label = tk.Label(self.root, text=demo_text, font=(
            'DejaVu Sans', 18), bd=1, relief=SUNKEN, justify=RIGHT)
        label.pack(pady=10)

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("TkinterApp", 500, 800)
    app.start()


if __name__ == "__main__":
    main()
