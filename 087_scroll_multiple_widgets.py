import tkinter as tk
import os
from tkinter.constants import LEFT, NONE, RIGHT, VERTICAL, Y


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

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=5, pady=5)

        self.scrollbar = tk.Scrollbar(self.frame, orient=VERTICAL)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.scrollbar.config(command=self.multiple_scroll)

        self.textbox = tk.Text(self.frame, width=20, height=25)
        self.textbox.pack(padx=5, pady=5, side=RIGHT)
        self.textbox.config(
            font="-size 16", yscrollcommand=self.scrollbar.set, wrap=NONE
        )

        self.textbox2 = tk.Text(self.frame, width=20, height=25)
        self.textbox2.pack(padx=5, pady=5, side=LEFT)
        self.textbox2.config(
            font="-size 16", yscrollcommand=self.scrollbar.set, wrap=NONE
        )

    def multiple_scroll(self, *args):
        self.textbox.yview(*args)
        self.textbox2.yview(*args)

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
    app = TkinterApp("TkinterApp", 600, 500)
    app.start()


if __name__ == "__main__":
    main()
