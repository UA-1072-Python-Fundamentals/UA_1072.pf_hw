from tkinter import *

win = Tk()
win.geometry('240x175')
win['bg'] = 'grey'
win.title('Calculator')
win.iconbitmap("1.png")


def add_digit(digit):
    value = calc.get()
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    calc.delete(0, END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    if value[-1] in "+-*/":
        value = value[:-1]
    elif '+' in value or '-' in value or '*' in value or '/' in value:
        calculate()
        value = calc.get()
    calc.delete(0, END)
    calc.insert(0, value + operation)


def calculate():   # =
    value = calc.get()
    if value[-1] in '-+*/':
        value = value+value[:-1]
    calc.delete(0, END)
    calc.insert(0, eval(value))


def clear():
    calc.delete(0, END)
    calc.insert(0, '0')


def digit_button(digit):
    return Button(win, text=digit, bd=5, font=15,
                  command=lambda: add_digit(digit))


def operation_button(operation):
    return Button(win, text=operation, bd=5, font=15, fg='blue',
                  command=lambda: add_operation(operation))


def calc_button(operation):
    return Button(win, text=operation, bd=5,font=15,  fg='green',
                  command=calculate)


def clear_button(operation):
    return Button(win, text=operation, bd=5, font=15, fg='red',
                  command=clear)


calc = Entry(win, justify=RIGHT, font=15, width=15)
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4, stick='we')

digit_button('1').grid(row=1, column=0, stick='wens')
digit_button('2').grid(row=1, column=1, stick='wens')
digit_button('3').grid(row=1, column=2, stick='wens')
digit_button('4').grid(row=2, column=0, stick='wens')
digit_button('5').grid(row=2, column=1, stick='wens')
digit_button('6').grid(row=2, column=2, stick='wens')
digit_button('7').grid(row=3, column=0, stick='wens')
digit_button('8').grid(row=3, column=1, stick='wens')
digit_button('9').grid(row=3, column=2, stick='wens')
digit_button('0').grid(row=4, column=0, stick='wens')

operation_button('+').grid(row=1, column=3, stick='wens')
operation_button('-').grid(row=2, column=3, stick='wens')
operation_button('*').grid(row=3, column=3, stick='wens')
operation_button('/').grid(row=4, column=3, stick='wens')


clear_button('C').grid(row=4, column=1, stick='wens')
calc_button('=').grid(row=4, column=2, stick='wens')

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=60)

win.mainloop()

