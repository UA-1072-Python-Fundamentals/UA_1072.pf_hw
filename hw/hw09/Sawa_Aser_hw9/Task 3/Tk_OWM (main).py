import tkinter as tk
from tkinter import font
import OWM

HEIGHT = 350
WIDTH = 450


def get_weather():
    text = OWM.weather_owm(entry_field.get())
    label.config(text=text)


def widget():
    
    root = tk.Tk()    
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    root.title("Weather Application")
    canvas.pack()
       
    frame = tk.Frame(root, bg="deep sky blue", bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    global entry_field
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
    global label
    label = tk.Label(lower_frame, font=('Courier', 14))
    label.place(relx=0, rely=0, relwidth=1, relheight=1)
            
    root.mainloop()


if __name__ == "__main__":
    widget()
