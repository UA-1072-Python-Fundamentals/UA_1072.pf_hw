import tkinter as tk
from tkinter import font
from pyowm import OWM

def get_weather():
    city = entry_field.get()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        weather_status = w.detailed_status
        weather_temperature = w.temperature('celsius')
        weather_humidity = w.humidity
        result_text.delete(1.0, tk.END)  # Clear previous content
        result_text.insert(tk.END, f"Weather in {city}: {weather_status}\n"
                                   f"Temperature in {city}: {weather_temperature}\n"
                                   f"Humidity in {city}: {weather_humidity}")
    except Exception as e:
        result_text.delete(1.0, tk.END)  # Clear previous content
        result_text.insert(tk.END, f"Error: {e}")

API_KEY = 'ef2206ff5da67de63306d0b143e20872'
owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 350
WIDTH = 450

root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame,
                   text="Get Weather",
                   bg="gray", fg="white",
                   font=('Courier', 8),
                   command=get_weather)
button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

result_text = tk.Text(lower_frame, font=('Courier', 14))
result_text.place(relx=0, rely=0, relwidth=1, relheight=1)

root.mainloop()
