import tkinter as tk
import os
from tkinter import font


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

        print(list(font.families()))

        self.bigFont = font.Font(
            family="Helvetica",
            size=42,
            weight="bold",
            slant="italic",
            underline=0,
            overstrike=0,
        )
        self.button1 = tk.Button(self.root, text="Helvetica", font=self.bigFont)
        self.button1.pack(pady=20)

        self.times = font.Font(
            family="Times",
            size=24,
            weight="normal",
            slant="italic",
            underline=0,
            overstrike=1,
        )
        self.button2 = tk.Button(self.root, text="Times", font=self.times)
        self.button2.pack(pady=20)

        self.lohit = font.Font(
            family="Lohit Tamil",
            size=32,
            weight="normal",
            slant="roman",
            underline=1,
            overstrike=0,
        )
        self.button3 = tk.Button(self.root, text="Lohit Tamil", font=self.lohit)
        self.button3.pack(pady=20)

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
