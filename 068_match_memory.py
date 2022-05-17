from tkinter import Label, Menu, messagebox
from math import sqrt
import tkinter as tk
import os
import random
import logging
from tkinter.constants import DISABLED, NORMAL, RIDGE
from typing import List

logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


class MatchButton(tk.Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def set_value(self, value):
        self.value = value


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

        self.label = Label(self.root, text="")
        self.label.pack(pady=10)

        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(pady=10)

        self.buttons: List[MatchButton] = []

        self.current_selection: MatchButton = None

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.option_menu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Options", menu=self.option_menu)
        self.option_menu.add_command(label="Reset Game", command=self.reset)
        self.option_menu.add_separator()
        self.option_menu.add_command(label="Exit Game", command=self.root.quit)

    def select_matches(self, button: MatchButton):
        logging.debug(f"{button.value=}")
        if button["text"] != " ":
            logging.debug("button already selected")

        button["text"] = button.value
        if not self.current_selection:
            self.current_selection = button
        else:
            if button.value == self.current_selection.value:
                logging.debug("correct")
                button["text"] = button.value
                button["state"] = DISABLED
                self.current_selection["state"] = DISABLED
                self.current_selection = None
            else:
                logging.debug("wrong")
                messagebox.showerror(f"{self.appname}", "Not a match")
                button["text"] = " "
                self.current_selection["text"] = " "
                self.current_selection = None

        for b in self.buttons:
            if b["state"] == NORMAL:
                break
        else:
            logging.debug("winner")
            self.player_win()

    def player_win(self):
        self.label.config(text="Congratulations! You WIN!")

        for b in self.buttons:
            b.config(bg="yellow")

    def set_matches(self, matches: list):
        # repeat values to create the matches
        logging.debug(f"{matches}")
        matches.extend(matches)
        self.matches = matches

    def reset(self):
        self.label.config(text="")
        random.shuffle(self.matches)
        logging.debug(f"{self.matches}")

        # destroy existing buttons and clear buttons list
        if self.buttons:
            for b in self.buttons:
                b.destroy()
            self.buttons.clear()

        # add matches to buttons
        for m in self.matches:
            button = MatchButton(
                self.game_frame,
                text=" ",
                font=("DejaVu Sans", 20),
                height=3,
                width=4,
                relief=RIDGE,  # FLAT, GROOVE
            )
            button.set_value(m)
            # use "lambda x=x: FUNC(x)" so that lambda creates different
            # functions each time. Otherwise, it will call only last value
            # https://stackoverflow.com/questions/19837486/lambda-in-a-loop
            button.config(command=lambda button=button: self.select_matches(button))
            self.buttons.append(button)
        self.put_matches()

    def put_matches(self):
        total = len(self.buttons)
        if not total:
            logging.debug("no button")
            return
        if total % 2 != 0:
            logging.debug(f"Size must be even, given {total}")
            return

        # calculate the number of rows and columns
        # based on a square of "total"
        rows = int(sqrt(total))
        columns = total // rows
        logging.debug(f"{rows=} {columns=}")
        button: MatchButton
        b = 0
        for r in range(rows):
            for c in range(columns):
                button = self.buttons[b]
                button.grid(row=r, column=c, ipadx=5, ipady=5)
                b += 1

        # check if there are buttons left-over and add them to
        # a new row
        if rows * columns < total:
            for c in range(total - rows * columns):
                button = self.buttons[b]
                button.grid(row=r + 1, column=c, ipadx=5, ipady=5)
                b += 1

        self.width = columns * 200
        self.height = rows * 200
        self.center_window()

    def start(self):
        self.reset()
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
    app.set_matches([1, 2, 3, 4, 5, 6, 7])
    # app.set_matches([1, 2])
    app.start()


if __name__ == "__main__":
    main()
