import tkinter as tk
import os


class TkinterApp:
    def __init__(self, appname="TkinterApp", width=400, heigth=400):
        self.appname = appname
        self.width = width
        self.height = heigth

        self.splash_root = tk.Tk()
        screen_width = self.splash_root.winfo_screenwidth()
        screen_height = self.splash_root.winfo_screenheight()

        self.splash_root.title(f"{self.appname} Loading")
        self.splash_root.geometry(
            f"{width}x{heigth}+{screen_width//2-width//2}+{screen_height//2-heigth//2}"
        )

        self.splash_root.overrideredirect(True)

        self.label = tk.Label(
            self.splash_root, text="Splash screen!", font=("DejaVu Sans", 32)
        )
        self.label.pack(pady=10)

        # do something that takes a long time (database loading, user login, internet connection)
        self.splash_root.after(3000, self.main_window)

    def main_window(self):
        self.splash_root.destroy()

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
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}"
        )

        self.label = tk.Label(self.root, text="Main window", font=("DejaVu Sans", 32))
        self.label.pack(pady=10)

    def start(self):
        tk.mainloop()


def main():
    app = TkinterApp("TkinterApp", 700, 500)
    app.start()


if __name__ == "__main__":
    main()
