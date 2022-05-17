import tkinter as tk
import os
from tkinter import Button, Canvas, Event, Frame
from tkinter.constants import BOTH, NW
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

        self.bg_original = Image.open("images/cam_logo.png")
        # self.bg_image = tk.PhotoImage(file="images/cam_logo.png")
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

        self.button1 = Button(self.frame, text="Button 1")
        self.button2 = Button(self.frame, text="Button 2")
        self.button3 = Button(self.frame, text="Button 3")
        self.button1.grid(row=0, column=0, padx=10)
        self.button2.grid(row=0, column=1, padx=10)
        self.button3.grid(row=0, column=2, padx=10)

    def set_canvas_bg(self):
        self.canvas = Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas_bg = self.canvas.create_image(0, 0, image=self.bg_image, anchor=NW)

        self.canvas.create_text(
            200, 40, text="Welcome", font=("DejaVu Sans", 32), fill="red"
        )

        self.button1 = Button(self.root, text="Button 1")
        self.button2 = Button(self.root, text="Button 2")
        self.button3 = Button(self.root, text="Button 3")

        self.button1_window = self.canvas.create_window(
            10, 150, anchor=NW, window=self.button1
        )
        self.button2_window = self.canvas.create_window(
            150, 150, anchor=NW, window=self.button2
        )
        self.button3_window = self.canvas.create_window(
            270, 150, anchor=NW, window=self.button3
        )

        self.canvas.bind("<Configure>", self.resize)

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
