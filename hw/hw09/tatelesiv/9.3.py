# Task 9.3
import tkinter
from tkinter import font

def weather():
    from pyowm import OWM
    API_KEY = 'ef2206ff5da67de63306d0b143e20872'
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(entry_field.get())
    w = observation.weather
    return (f"City: {entry_field.get().capitalize()}\n\n"
            f"Weather: {w.detailed_status.capitalize()}\n"
            f"Temp: {round(w.temperature('celsius')['temp'], 1)} C\U000000B0\n"
            f"Wind speed: {round(w.wind('km_hour')['speed'], 2)} km\\h\n")


def get_weather():
    label["text"] = weather()
    root.title("Weather in " + entry_field.get().capitalize())


HEIGHT = 350
WIDTH = 450
root = tkinter.Tk()
canvas = tkinter.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()
frame = tkinter.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
entry_field = tkinter.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tkinter.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=lambda: get_weather())
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tkinter.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tkinter.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
