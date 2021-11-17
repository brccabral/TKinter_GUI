import tkinter as tk
from pydub import AudioSegment
import simpleaudio
import os

from simpleaudio.shiny import PlayObject

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
root.geometry("400x400")

# pydub doesn't have a stop feature
# use simpleaudio to have a PlayObject() to get stop() method
sound = AudioSegment.from_mp3("sounds/forward_operating_base.mp3")
play_obj: PlayObject = None
def start_music():
    global play_obj
    play_obj = simpleaudio.play_buffer(
        sound.raw_data,
        num_channels= sound.channels,
        bytes_per_sample= sound.sample_width,
        sample_rate= sound.frame_rate
    )

def stop_music():
    global play_obj
    play_obj.stop()


my_button = tk.Button(root, text="Start music", command=start_music)
my_button.pack(pady=10)
my_button = tk.Button(root, text="Stop music", command=stop_music)
my_button.pack(pady=10)



root.mainloop()