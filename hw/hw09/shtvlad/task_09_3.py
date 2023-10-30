import tkinter as tk
from tkinter import font
from tkinter import Message
from pyowm import OWM


HEIGHT = 550
WIDTH = 650


root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()

def get_location():
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    # ---------- FREE API KEY examples ---------------------

    owm = OWM(API_KEY)
    mgr = owm.weather_manager()

    # Search for current weather in London (Great Britain) and get details
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather
    txt = (f"{w.detailed_status}\n"
           f"{str(w.wind())}\n"
           f"{w.humidity}\n"
           f"{w.temperature('celsius')}\n"
           f"{w.rain}\n"
           f"{w.clouds}")
    label_weather = tk.Label(lower_frame, text=txt, font=('Courier', 6))
    label_weather.place(relx=0, rely=0, relwidth=1, relheight=1)

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_location)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame,font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)



root.mainloop()

