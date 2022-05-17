import tkinter as tk
import os
import logging

logging.basicConfig(
    format="%(levelname)s - %(asctime)s - %(name)s - %(message)s",
    datefmt="%H:%M:%S",
    level=logging.DEBUG,
)


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
        self.root.geometry(f"{width}x{heigth}")

        self.button = tk.Button(self.root, text="Click me!", command=self.open_popup)
        self.button.pack(pady=10)

        self.image = tk.PhotoImage(file="images/star.png", format="png")

        self.return_label = tk.Label(self.root)
        self.return_label.pack(pady=10)

    def open_popup(self):
        self.pop = tk.Toplevel(self.root)
        self.pop.title("My popup")
        self.pop.geometry("250x150")
        pop_main_color = "green"
        self.pop.config(bg=pop_main_color)

        label = tk.Label(
            self.pop, text="Would you like to proceed?", bg=pop_main_color, fg="white"
        )
        label.pack(pady=10)

        frame = tk.Frame(self.pop, bg=pop_main_color)
        frame.pack(pady=5)

        # even if it is a .png image, need to set background color
        pip = tk.Label(frame, image=self.image, borderwidth=0, bg=pop_main_color)
        pip.grid(row=0, column=0, padx=5)

        yes_button = tk.Button(
            frame, text="YES", command=lambda: self.pop_choice("yes"), bg="orange"
        )
        yes_button.grid(row=0, column=1, padx=5)
        no_button = tk.Button(
            frame, text="NO", command=lambda: self.pop_choice("no"), bg="red"
        )
        no_button.grid(row=0, column=2, padx=5)

    def pop_choice(self, return_choice: str):
        self.pop.destroy()
        logging.debug(f"{return_choice}")
        self.return_label.config(text=return_choice)

    def start(self):
        self.root.mainloop()


def main():
    app = TkinterApp("Custom message box", 500, 300)
    app.start()


if __name__ == "__main__":
    main()
