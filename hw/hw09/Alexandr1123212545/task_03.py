import tkinter as tk
from tkinter import font
from pyowm import OWM

HEIGHT = 350
WIDTH = 450
API_KEY = '62ead591e45261a878bc2cff354c53b3'


def get_weather():
    city = entry_field.get()
    owm = OWM(API_KEY)
    mgr = owm.weather_manager()
    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather
        result_1 = 'Status - No data' if not w.detailed_status else f'Status - {w.detailed_status}'
        result_2 = 'Temperature - No data' if not w.temperature('celsius')['temp'] \
            else f'Temperature - {w.temperature('celsius')['temp']}\u00b0С'
        result_3 = 'Humidity - No data' if not w.humidity else f'Humidity - {w.humidity}%'
        result_4 = 'Wind speed - No data' if not w.wind else f'Wind speed - {w.wind()['speed']}m/s'
        result_5 = 'Rain - No data' if not w.rain else f'Rain - {w.rain['1h']}mm'
        all = f'{result_1}\n{result_2}\n{result_3}\n{result_4}\n{result_5}'
        label['text'] = all
    except FileNotFoundError:
        label['text'] = 'City not found. Try again.'

root = tk.Tk()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
root.title("Weather Application")
canvas.pack()



frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0, rely=0, relwidth=0.65, relheight=1)

button = tk.Button(frame, 
                   text="Get Weather", 
                   bg="gray", fg="white", 
                   font=('Courier', 8), 
                   command=lambda: get_weather())

button.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)



lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, font=('Courier', 14))
label.place(relx=0, rely=0, relwidth=1, relheight=1)

print(type(label))
root.mainloop()

