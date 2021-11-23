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

        self.bitmaps = ["error", "gray75", "gray50", "gray12",
                        "hourglass", "info", "questhead", "question", "warning"]

        for bitmap in self.bitmaps:
            button = tk.Button(self.root, bitmap=bitmap, fg="red",
                               command=lambda b=bitmap: self.function_name(b), width=50, height=50)
            button.pack(padx=5, pady=5)

    def function_name(self, bitmap):
        logging.debug(f'{bitmap=}')

    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}")


def main():
    app = TkinterApp("TkinterApp", 150, 650)
    app.start()


if __name__ == "__main__":
    main()
