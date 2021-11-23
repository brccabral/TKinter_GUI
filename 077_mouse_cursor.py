import tkinter as tk
import os
import logging
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(name)s - %(message)s',
                    datefmt='%H:%M:%S', level=logging.DEBUG)


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
        self.root.iconphoto(self.root._w, tk.PhotoImage(file='python3.png'))

        self.cursors = list(reversed(["arrow", "circle", "clock", "cross", "dotbox", "exchange", "fleur", 
        "heart", "man", "mouse", "pirate", "plus", "shuttle", "sizing", "spider", 
        "spraycan", "star", "target", "tcross", "trek"]))

        for r in range(4):
            for c in range(5):
                cursor = self.cursors.pop()
                button = tk.Button(self.root, text=cursor, fg="red", cursor=cursor,
                                command=lambda cursor=cursor: self.function_name(cursor))
                button.grid(row=r, column=c, padx=5, pady=5)

    def function_name(self, cursor):
        logging.debug(f'{cursor=}')
        self.root.config(cursor=cursor)

    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}")


def main():
    app = TkinterApp("TkinterApp", 600, 300)
    app.start()


if __name__ == "__main__":
    main()
