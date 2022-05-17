import tkinter as tk
import os


class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, heigth=400):
        self.root = tk.Tk()
        self.appname = appname
        self.root.title(appname)
        if os.name == "nt":
            self.root.wm_iconbitmap(bitmap="python3.ico")
        else:
            self.root.wm_iconbitmap(bitmap="@python3.xbm")
        self.root.iconphoto(self.root._w, tk.PhotoImage(file="python3.png"))

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(
            f"{width}x{heigth}+{screen_width//2-width//2}+{screen_height//2-heigth//2}"
        )

        self.label = tk.Label(self.root, text=f"{screen_width=} {screen_height}")
        self.label.pack(pady=10)

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("Center App", 500, 500)
    app.start()


if __name__ == "__main__":
    main()
