import tkinter as tk
import os
from tkinter.constants import CENTER, LEFT, RIGHT
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

        self.long_text = "This is some long text that I am typing so that we can look at it, isn't it cool?"
        self.label_font = font.Font(self.root, size=18)

        self.label = tk.Label(self.root, text=self.long_text, font=self.label_font)
        self.label.pack(padx=5, pady=5)

        self.label_frame = tk.LabelFrame(self.root, text="Right Justified")
        self.label_frame.pack(padx=5, pady=5)

        self.message = tk.Message(
            self.label_frame,
            text=self.long_text,
            aspect=100,
            font=self.label_font,
            justify=RIGHT,
        )
        self.message.pack(padx=5, pady=5)

        self.label_frame2 = tk.LabelFrame(self.root, text="Left Justified")
        self.label_frame2.pack(padx=5, pady=5)

        self.message2 = tk.Message(
            self.label_frame2,
            text=self.long_text,
            aspect=100,
            font=self.label_font,
            justify=LEFT,
        )
        self.message2.pack(padx=5, pady=5)

        self.label_frame3 = tk.LabelFrame(self.root, text="Center Justified")
        self.label_frame3.pack(padx=5, pady=5)

        self.message3 = tk.Message(
            self.label_frame3,
            text=self.long_text,
            aspect=100,
            font=self.label_font,
            justify=CENTER,
        )
        self.message3.pack(padx=5, pady=5)

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
    app = TkinterApp("TkinterApp", 700, 800)
    app.start()


if __name__ == "__main__":
    main()
