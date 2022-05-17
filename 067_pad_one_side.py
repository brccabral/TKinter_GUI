import tkinter as tk
import os


class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, heigth=400):
        self.appname = appname
        self.width = width
        self.height = heigth

        self.root = tk.Tk()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.title(self.appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file="python3.png"))

        self.root.geometry(
            f"{width}x{heigth}+{screen_width//2-width//2}+{screen_height//2-heigth//2}"
        )

        self.root.config(bg="blue")

        # use padx or pady as a tuple
        # padx=(left, right)
        # pady=(top, bottom)

        self.label = tk.Label(
            self.root,
            text="Hello World 1",
            bg="white",
            fg="black",
            font=("DejaVu Sans", 20),
        )
        self.label.grid(row=0, column=0, pady=(50, 0))

        self.label2 = tk.Label(
            self.root,
            text="Hello World 2",
            bg="white",
            fg="black",
            font=("DejaVu Sans", 20),
        )
        self.label2.grid(row=0, column=1, padx=(10, 0))

        self.label3 = tk.Label(
            self.root,
            text="Hello World 3",
            bg="white",
            fg="black",
            font=("DejaVu Sans", 20),
        )
        self.label3.grid(row=0, column=2)

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("TkinterApp", 700, 500)
    app.start()


if __name__ == "__main__":
    main()
