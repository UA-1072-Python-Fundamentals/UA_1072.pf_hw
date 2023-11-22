from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


root = tk.Tk()
root.title("Typing Game")
root.geometry("800x500")
root.configure(bg="#E6E6E6")

root.resizable(width=False, height=False)


def play_game():
   root.destroy()
   import game


welcome_f = ("fonts/Roboto-Bold.ttf", 40, "bold")
text_f = ("fonts/Roboto-Bold.ttf", 20)

label1 = Label(root, text="Welcome to my typing game!", font=welcome_f, fg="#29353C", bg="#E6E6E6", anchor="center")
label1.pack(pady=50)

label2 = Label(root, text="Enter the given words and find your typing speed!", font=text_f, fg="#29353C", bg="#E6E6E6", wraplength=500)
label2.pack(pady=10)

play_image = Image.open("start_img.png")
resize_image = play_image.resize((306, 244))
play_image = ImageTk.PhotoImage(resize_image)
play_button = Button(root, image=play_image, borderwidth=0, bg="#E6E6E6", command=play_game, bd=0, anchor="center")
play_button.pack(pady=50)

root.mainloop()
