import tkinter as tk
import logging
from itertools import cycle
from tkinter import Button, Menu, messagebox
from tkinter.constants import DISABLED, NORMAL
from tkinter.font import Font
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s', datefmt='%H:%M:%S', level=logging.DEBUG)
import os

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.appname = "Tic Tac Toe"
        self.root.title(self.appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file='python3.png'))
        self.add_buttons()
        self.players = cycle('XO')
        self.turn = next(self.players)
        self.count = 0

        self.menu = Menu(self.root)
        self.root.config(menu=self.menu)
        self.options_menu = Menu(self.menu, tearoff=False)
        self.menu.add_cascade(label="Options", menu=self.options_menu)
        self.options_menu.add_command(label="Reset Game", command=self.reset_game)
    
    def reset_game(self):
        self.b1.config(text=" ", bg="gray", state=NORMAL)
        self.b2.config(text=" ", bg="gray", state=NORMAL)
        self.b3.config(text=" ", bg="gray", state=NORMAL)
        self.b4.config(text=" ", bg="gray", state=NORMAL)
        self.b5.config(text=" ", bg="gray", state=NORMAL)
        self.b6.config(text=" ", bg="gray", state=NORMAL)
        self.b7.config(text=" ", bg="gray", state=NORMAL)
        self.b8.config(text=" ", bg="gray", state=NORMAL)
        self.b9.config(text=" ", bg="gray", state=NORMAL)
        self.count = 0

    def check_sequence(self, ba: Button, bb: Button, bc: Button):
        if not ba['text'] == " " and ba['text'] == bb['text'] and bb['text'] == bc['text']:
            ba.config(bg="red")
            bb.config(bg="red")
            bc.config(bg="red")
            return True
        return False
    
    def check_winner(self):
        if self.check_sequence(self.b1, self.b2, self.b3):
            return True
        elif self.check_sequence(self.b4, self.b5, self.b6):
            return True
        elif self.check_sequence(self.b7, self.b8, self.b9):
            return True
        elif self.check_sequence(self.b1, self.b4, self.b7):
            return True
        elif self.check_sequence(self.b2, self.b5, self.b8):
            return True
        elif self.check_sequence(self.b3, self.b6, self.b9):
            return True
        elif self.check_sequence(self.b1, self.b5, self.b9):
            return True
        elif self.check_sequence(self.b3, self.b5, self.b7):
            return True
        return False
    
    def disable_buttons(self):
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)
        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)

    def b_click(self, button: tk.Button):
        logging.debug(f'clicked')
        if button['text'] == " ":
            button['text'] = self.turn
            if self.check_winner():
                messagebox.showinfo(self.appname, f"{self.turn} WON!")
                self.disable_buttons()
                return
            self.turn = next(self.players)
            self.count += 1
            if self.count >= 9:
                self.disable_buttons()
                messagebox.showerror(self.appname, "It's a Tie!\nNo one wins.")
        else:
            messagebox.showerror(self.appname, "Box already selected! Pick another bok")

    def add_buttons(self):
        font = Font(self.root, size=20)
        self.b1 = tk.Button(self.root, text=" ", font=font, height=3, width=6, bg="gray", command=lambda: self.b_click(self.b1))
        self.b2 = tk.Button(self.root, text=" ", font=font, height=3, width=6, bg="gray", command=lambda: self.b_click(self.b2))
        self.b3 = tk.Button(self.root, text=" ", font=font, height=3, width=6, bg="gray", command=lambda: self.b_click(self.b3))
        self.b4 = tk.Button(self.root, text=" ", font=font, height=3, width=6, bg="gray", command=lambda: self.b_click(self.b4))
        self.b5 = tk.Button(self.root, text=" ", font=font, height=3, width=6, bg="gray", command=lambda: self.b_click(self.b5))
        self.b6 = tk.Button(self.root, text=" ", font=font, height=3, width=6, bg="gray", command=lambda: self.b_click(self.b6))
        self.b7 = tk.Button(self.root, text=" ", font=font, height=3, width=6, bg="gray", command=lambda: self.b_click(self.b7))
        self.b8 = tk.Button(self.root, text=" ", font=font, height=3, width=6, bg="gray", command=lambda: self.b_click(self.b8))
        self.b9 = tk.Button(self.root, text=" ", font=font, height=3, width=6, bg="gray", command=lambda: self.b_click(self.b9))

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)
        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)
        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

    def start(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TicTacToe()
    app.start()