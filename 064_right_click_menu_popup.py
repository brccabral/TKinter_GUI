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
        self.root.iconphoto(self.root._w, tk.PhotoImage(file='python3.png'))

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        self.root.geometry(
            f"{width}x{heigth}+{screen_width//2-width//2}+{screen_height//2-heigth//2}")

        self.right_click_menu = tk.Menu(self.root, tearoff=False)
        self.right_click_menu.add_command(label="Say hello", command=self.hello)
        self.right_click_menu.add_command(label="Say goodbye", command=self.goodbye)
        self.right_click_menu.add_separator()
        self.right_click_menu.add_command(label="Exit", command=self.root.quit)

        self.root.bind("<Button-3>", self.open_right_click)

        self.label = tk.Label(self.root, text="",font=('DejaVu Sans', 32))
        self.label.pack(pady=10)

    def open_right_click(self, event: tk.Event):
        self.right_click_menu.tk_popup(x=event.x_root, y=event.y_root)

    def hello(self):
        self.label.config(text="Hello")

    def goodbye(self):
        self.label.config(text="Goodbye")

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("TkinterApp", 500, 800)
    app.start()


if __name__ == "__main__":
    main()
