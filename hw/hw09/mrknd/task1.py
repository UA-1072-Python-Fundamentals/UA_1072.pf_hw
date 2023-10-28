import random
from tkinter import *
import random

random_num = random.randint(1, 100)
count = 9

window = Tk()
window.geometry('280x120+100+100')
window.title("Guess the number")


def check_guess():
    global random_num
    global count
    num = int(guess_entry.get())
    if count > 0:
        if num == random_num:
            out_text.config(text=f'You won!')
        elif num > random_num:
            out_text.config(text=f'My number is smaller, you have {count} attempts')
            count -= 1
        elif num < random_num:
            out_text.config(text=f'My number is higher, you have {count} attempts')
            count -= 1
    else:
        out_text.config(text=f'You lose')


label = Label(text='Guess number 1 between 100')
label.pack()

guess_entry = Entry(window)
guess_entry.pack()

btn = Button(window, text='Submit', command=check_guess)
btn.pack()

out_text = Label(text='')
out_text.pack()

window.mainloop()
