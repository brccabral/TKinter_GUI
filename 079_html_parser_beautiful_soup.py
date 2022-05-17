import tkinter as tk
import os
from tkinter.constants import BOTTOM, E, N, S, X
from bs4 import BeautifulSoup
from urllib import request
from datetime import datetime
import logging

from bs4.element import Tag

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

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=5, pady=20)

        self.logo = tk.PhotoImage(file="images/bitcoin.png")

        self.logo_label = tk.Label(self.frame, image=self.logo, bd=0)
        self.logo_label.grid(row=0, column=0, rowspan=2)

        self.bit_label = tk.Label(
            self.frame, text="Test", foreground="#ffc107", font=("Helvetica", 45)
        )
        self.bit_label.grid(row=0, column=1, padx=20, sticky=S)

        self.latest_move = tk.Label(
            self.frame, text="move test", fg="grey", font=("Helvetica", 9)
        )
        self.latest_move.grid(row=1, column=1, sticky=N)

        self.previous = 0

        self.status_bar = tk.Label(
            self.root, text="Last updated", bd=0, anchor=E, fg="grey"
        )
        self.status_bar.pack(padx=5, pady=5, fill=X, side=BOTTOM, ipady=2)

    def update_price(self):
        try:  # avoid internet connection error
            page_read = request.urlopen("https://www.coindesk.com/price/bitcoin").read()
            html = BeautifulSoup(page_read, "html.parser")
            kPwwwV: Tag = html.find(class_="kPwwwV")
            logging.debug(f"{kPwwwV.get_text()=}")
            bit_price = kPwwwV.get_text()

            self.bit_label.config(text=f"${bit_price}")

            now = datetime.now()
            current_time = now.strftime("%I:%M:%S %p")
            self.status_bar.config(text=f"Last updated {current_time}")
            current_price = float(bit_price.replace(",", ""))
            if self.previous == current_price:
                logging.debug("same price")
                pass
            elif self.previous > current_price:
                self.bit_label.config(fg="red")
                self.latest_move.config(
                    text=f"Price down {current_price-self.previous:.2f}", fg="red"
                )
            else:
                self.bit_label.config(fg="green")
                self.latest_move.config(
                    text=f"Price up {current_price-self.previous:.2f}", fg="green"
                )
            self.previous = current_price
        except Exception as exception:
            logging.debug(f"{exception}")
        finally:
            self.root.after(60000, self.update_price)

    def start(self):
        self.center_window()
        self.update_price()
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
