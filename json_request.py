import tkinter as tk
import os
import requests
import json

root = tk.Tk()
root.title("TKinter GUI")
if os.name == "nt":
    root.wm_iconbitmap(bitmap="python3.ico")
else:
    root.wm_iconbitmap(bitmap="@python3.xbm")
root.iconphoto(root._w, tk.PhotoImage(file='python3.png'))
# root.geometry("400x50")

label = ""
try:
    api_request = requests.get("https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=98037&date=2021-10-21&distance=25&API_KEY=XXXX")
    api = json.loads(api_request.content)
    city = api[0]['ReportingArea']
    quality = api[0]['AQI']
    category = api[0]['Category']['Name']
    label = f"{city} AirQuality {quality}, {category}"
except Exception as e:
    label = e

mylabel = tk.Label(root, text=label, font=("Helvetica", 20))
mylabel.pack(pady=10, padx=10)

root.mainloop()