import tkinter as tk
import os
from tkinter import Button, Canvas, Entry, Event, Frame
from tkinter import font as tkFont
from tkinter.constants import BOTH, END, NW
from PIL import ImageTk, Image
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

        # change default font size
        self.default_font = tkFont.nametofont("TkDefaultFont")
        self.default_font.config(size=20)

        # make app not resizable
        self.root.resizable(width=False, height=False)

        # need PIL to resize images
        self.bg_original = Image.open("images/cam_logo.png")
        self.bg_image = ImageTk.PhotoImage(self.bg_original)

    def set_root_bg(self):
        self.label = tk.Label(self.root, image=self.bg_image)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

        self.welcome_label = tk.Label(
            self.root, text="Welcome", font=("DejaVu Sans", 32)
        )
        self.welcome_label.pack(pady=20)

        self.frame = Frame(self.root)
        self.frame.pack(pady=100)

        self.login_button = Button(self.frame, text="Button 1")
        self.button2 = Button(self.frame, text="Button 2")
        self.button3 = Button(self.frame, text="Button 3")
        self.login_button.grid(row=0, column=0, padx=10)
        self.button2.grid(row=0, column=1, padx=10)
        self.button3.grid(row=0, column=2, padx=10)

    def set_canvas_bg(self):
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)

        # keep return value to be used in resize function
        self.canvas_bg = self.canvas.create_image(0, 0, image=self.bg_image, anchor=NW)

        # create username Entry field
        self.username = Entry(
            self.root, width=17, fg="red", bd=0, font=self.default_font
        )
        self.username.insert(0, "username")
        self.username.bind("<Button-1>", self.clear_entries)
        self.username_window = self.canvas.create_window(
            34, 290, anchor=NW, window=self.username
        )

        # create password Entry field
        # the config to change to * is done in clear_entries() below
        self.password = Entry(
            self.root, width=17, fg="red", bd=0, font=self.default_font
        )
        self.password.insert(0, "password")
        self.password.bind("<Button-1>", self.clear_entries)
        self.password_window = self.canvas.create_window(
            34, 370, anchor=NW, window=self.password
        )

        # create login button
        self.login_button = Button(
            self.root, text="Login", width=15, command=self.check_login
        )
        self.login_window = self.canvas.create_window(
            36, 470, anchor=NW, window=self.login_button
        )

        self.canvas.bind("<Configure>", self.resize)

    def clear_entries(self, event: Event):
        # this "if" is to clear only at first click
        if self.username.get() == "username" and self.password.get() == "password":
            self.username.delete(0, END)
            self.password.delete(0, END)
            # and here we set the field to show * for each character
            self.password.config(show="*")

    def check_login(self):
        self.username.destroy()
        self.password.destroy()
        self.login_button.destroy()

        self.canvas.create_text(
            200, 40, text="Welcome", font=("DejaVu Sans", 32), fill="red"
        )

    def resize(self, event: Event):
        logging.debug(f"resize {event=}")
        resized = self.bg_original.resize((event.width, event.height), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(resized)
        self.canvas.itemconfig(self.canvas_bg, image=self.bg_image)

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
    app = TkinterApp("TkinterApp", 398, 600)
    # app.set_root_bg()
    app.set_canvas_bg()
    app.start()


if __name__ == "__main__":
    main()
