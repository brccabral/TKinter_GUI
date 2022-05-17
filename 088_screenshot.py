import tkinter as tk
import os
import mss


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

        self.button = tk.Button(
            self.root, text="Take a screenshot", command=self.take_screenshot
        )
        self.button.pack(padx=5, pady=5)

        self.label = tk.Label(self.root, text="")
        self.label.pack(padx=5, pady=5)

    def take_screenshot(self):
        with mss.mss() as sct:
            filename = sct.shot(output="output.png")
            # filename = sct.shot(output="output.png", mon=-1) # mon=-1 to save multiple monitors
            self.label.config(text="Screen Shot has been saved")

    def start(self):
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
    app.start()


if __name__ == "__main__":
    main()
