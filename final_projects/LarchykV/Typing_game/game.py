from tkinter import *
import tkinter as tk
from tkinter import messagebox
import random
from timeit import default_timer as timer
from words import word_list


root = tk.Tk()
root.title("Typing Game")
root.iconbitmap("myIcon.ico")
root.geometry("800x500")
root.configure(bg="#E6E6E6")

root.resizable(width=False, height=False)


matched = 0
not_matched = 0
timeleft = 60


def time():
    global timeleft, matched
    if timeleft > 0:
        timeleft -= 1
        timercount.configure(text=timeleft)
        timercount.after(1000, time)
        if timeleft in range(0, 11):
            timercount.configure(fg="#ff1717")
            timer.configure(fg="#ff1717")

    else:
        count.configure(text=matched)
        scorelabel.configure(text="Your typing speed is:    WPM")

        retry = messagebox.askretrycancel('Notification', 'Do you want to play again?')

        if retry:
            timeleft = 60
            matched = 0
            feedback.configure(text='')
            count.configure(text='')
            scorelabel.configure(text='')
            timercount.configure(text=timeleft, fg="#29353C")
            timer.configure(fg="#29353C")
            entry_box.delete(0, END)


def start(event):
    global matched, not_matched

    if timeleft == 60:
        time()

    if entry_box.get() == word["text"]:
        matched += 1
    elif entry_box.get() != word["text"]:
        not_matched += 1

    random.shuffle(word_list)
    word.configure(text=word_list[0])
    entry_box.delete(0,
                     END)
    label.configure(text="")


bold_f = ("fonts/Roboto-Bold.ttf", 50, "bold")
bold_f1 = ("fonts/Roboto-Bold.ttf", 30, "bold")
usual_f = ("fonts/Roboto-Bold.ttf", 25)
usual_f1 = ("fonts/Roboto-Bold.ttf", 18)


h1 = Label(root, text="Good luck!", bg="#E6E6E6", fg="#29353C", font=bold_f, anchor="center")
h1.pack(pady=60)

word = Label(root, text=("Type:", word_list[0]), font=bold_f1, fg="#29353C", bg="#E6E6E6", width=15, anchor="center")
word.place(relx=0.5, rely=0.4, anchor=CENTER)

entry_box = Entry(root, font=usual_f, fg="#29353C", bg="#768A96", justify="center", bd=7)
entry_box.place(relx=0.5, rely=0.5, anchor=CENTER)


timercount = Label(root, text="60", fg="#29353C", bg="#E6E6E6", font=bold_f)
timercount.place(relx=0.5, rely=0.67, anchor=CENTER)

label = Label(root, text="*Enter a word to start the game", bg="#E6E6E6", fg="#29353C",
              font=usual_f1)
label.place(relx=0.03, rely=0.9)


scorelabel = Label(root, text="", bg="#E6E6E6", fg="#29353C", font=usual_f)
scorelabel.place(relx=0.5, rely=0.8, anchor=CENTER)

count = Label(root, text="", bg="#E6E6E6", fg="#29353C", font=usual_f)
count.place(relx=0.63, rely=0.8, anchor=CENTER)

feedback = Label(root, text="", bg="#E6E6E6", fg="#29353C", font=usual_f)
feedback.place(x=53, y=350)

root.bind('<Return>', start)
root.mainloop()
