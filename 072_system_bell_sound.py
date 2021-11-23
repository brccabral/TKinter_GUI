import tkinter as tk
import os


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

        self.bell_img = tk.PhotoImage(file="images/bell.png")
        self.bell_label = tk.Label(self.root, image=self.bell_img)
        self.bell_label.pack(pady=20)

        self.button = tk.Button(self.root, text="Ring the bell",
                                command=self.ring,
                                font=('DejaVu Sans', 24), fg="#4d4d4d"
                                )
        self.button.pack(pady=20)

    def ring(self):
        self.root.bell()

    def start(self):
        self.center_window()
        self.root.mainloop()

    def center_window(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        self.root.geometry(
            f"{self.width}x{self.height}+{screen_width//2-self.width//2}+{screen_height//2-self.height//2}")


def main():
    app = TkinterApp("TkinterApp", 700, 500)
    app.start()


if __name__ == "__main__":
    main()
