import random
from tkinter import *
from tkinter import ttk

win= Tk()

win.geometry("800x600")
tries = 0
number = random.randint(1, 101)

def display_text():
    # declare tries as global variable
    global tries

    if tries >= 10:
        # game is over
        return

    try:
        guess = int(entry.get())
    except ValueError:
        errmsg = Label(win, text="Invalid number", font=("Courier 22 bold"), fg="red")
        errmsg.pack()
        # remove the error message one second later
        errmsg.after(3000, errmsg.destroy)
        return

    tries += 1
    if guess == number:
        d = Label(win, text="Congratulation, you win!", font=("Courier 22 bold"))
        d.pack()
        d.after(3000, d.destroy)
        tries = 10  # game over
    else:
        msg = f"Your number {guess} is {'more' if guess > number else 'less'} than mine"
        b = Label(win, text=msg, font=("Courier 22 bold"))
        b.pack()
        b.after(3000, b.destroy)
        triess = "Your attempts: " + str(tries)
        v = Label(win, text=triess, font=("Courier 22 bold"))
        v.pack()
        v.after(3000, v.destroy)
        if tries >= 10:
            d = Label(win, text=f"Unfortunately, you lose.\nThe number is {number}", font=("Courier 22 bold"))
            d.pack()
            d.after(3000, d.destroy)


entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()