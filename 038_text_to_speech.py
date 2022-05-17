import tkinter as tk
from tkinter.constants import END
import pyttsx3
import os

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file="python3.png"))
root.geometry("500x400")


# engine = pyttsx3.init()

# """ RATE"""
# rate = engine.getProperty('rate')   # getting details of current speaking rate
# print (rate)                        #printing current voice rate
# engine.setProperty('rate', 200)     # setting up new voice rate


# """VOLUME"""
# volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
# print (volume)                          #printing current volume level
# engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

# """VOICE"""
# voices = engine.getProperty('voices')       #getting details of current voice
# print(len(voices))
# # print("\n".join(f"{i:>2}: {voice}" for i, voice in enumerate(voices)))

# for v in voices:
#     if v.gender == "female":
#         print(v)

# engine.setProperty('voice', voices[0].id)   #changing index, changes voices. 1 for female

# engine.say("Hello World!")
# # engine.say('My current speaking rate is ' + str(rate))
# engine.runAndWait()
# engine.stop()

my_entry = tk.Entry(root, font=("Helvetica", 28))
my_entry.pack(pady=10)


def talk():
    engine = pyttsx3.init(driverName="espeak", debug=True)
    # on terminal
    # this lists the languages only
    ## espeak --voices=
    # with the language we can check the available voices (female/different accents)
    ## espeak --voices=en
    engine.setProperty("voice", "us-mbrola-1")
    engine.setProperty("rate", 150)
    engine.say(my_entry.get())
    engine.runAndWait()
    engine.stop()
    my_entry.delete(0, END)


my_button = tk.Button(root, text="Speak", command=talk)
my_button.pack()


root.mainloop()
