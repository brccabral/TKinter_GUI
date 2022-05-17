import tkinter as tk
import os
import logging
from tkinter import Button, font
import _tkinter

logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


class AnimatedButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font = self.get_font()
        self.original_font_size = self.font["size"]
        logging.debug(f"{self.original_font_size=}")

    def animate(self):
        logging.debug("animate")
        self.original_pady = self.pack_info()["pady"]
        logging.debug(f"{self.original_pady=}")
        # self.font['size'] = 8
        self.expand()

    def contract(self):
        if self.font["size"] - self.original_font_size > 0:
            self.font["size"] -= 2
            # need config() for widgets that were not created
            # with a font object
            self.config(font=self.font)

            self.pack_configure(pady=self.pack_info()["pady"] - 10)

            self.after(10, self.contract)

    def expand(self):
        logging.debug(f'{self.font} {self.original_font_size=} {self.font["size"]=}')
        if self.font["size"] - self.original_font_size < 20:
            self.font["size"] += 2
            # need config() for widgets that were not created
            # with a font object
            self.config(font=self.font)

            self.pack_configure(pady=self.pack_info()["pady"] + 10)

            self.after(10, self.expand)
        else:
            self.contract()

    def get_font(self) -> font.Font:
        current_font = self.cget("font")
        try:
            new_font = font.nametofont(current_font)
        except _tkinter.TclError as e:
            logging.debug(f"{e}")
            logging.debug(f"{current_font=}")
            new_font = font.Font(self, font=current_font)
        finally:
            return new_font


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

        self.button_font = font.Font(self.root, "-size 32")

        self.button = AnimatedButton(self.root, font=self.button_font, text="Click me")
        self.button.config(command=self.button.animate)
        self.button.pack(padx=5, pady=5)

        self.button2 = AnimatedButton(self.root, font="-size 8", text="Click me")
        self.button2.config(command=self.button2.animate)
        self.button2.pack(padx=5, pady=5)

        self.button3 = AnimatedButton(self.root, font=("Times", 22), text="Click me")
        self.button3.config(command=self.button3.animate)
        self.button3.pack(padx=5, pady=5)

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
