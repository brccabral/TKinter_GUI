import tkinter as tk
import os
from tkinter.constants import E, W
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
root.configure(background='#DD66DD')

def ziplookup():
    zipcode = zip.get()
    label = ""
    weather_color = 'grey'
    try:
        api_request = requests.get(f"https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode={zipcode}&date=2021-10-21&distance=25&API_KEY=")
        api = json.loads(api_request.content)
        max_quality = -999
        areas = []
        for a in api:
            city = a['ReportingArea']
            quality = a['AQI']
            ParameterName = a['ParameterName']
            category = a['Category']['Name']

            areas.append(f"{city} {ParameterName} {quality} {category}")
            if quality>max_quality:
                max_quality = quality
                if category == "Good":
                    weather_color = '#0C0' # green
                elif category == "Moderate":
                    weather_color = '#FFFF00' # yellow
                elif category == "Unhealthy for Sensitive Groups":
                    weather_color = '#FF9900' # orange
                elif category == "Unhealthy":
                    weather_color = '#FF0000' # red
                elif category == "Very Unhealthy":
                    weather_color = '#990066' # purple
                elif category == "Hazardous":
                    weather_color = '#660000' # maroon
                elif category == "Unavailable":
                    weather_color = '#666666' # grey
                else:
                    weather_color = 'white'

            label = "\n".join(areas)

    except Exception as e:
        label = e
        weather_color = 'grey'
    

    mylabel = tk.Label(root, text=label, font=("Helvetica", 20), background=weather_color)
    mylabel.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

zip = tk.Entry(root)
zip.grid(row=0, column=0, sticky=W+E)

submit = tk.Button(root, text="Check weather", command=ziplookup)
submit.grid(row=0, column=1, sticky=W+E)

root.mainloop()