from tkinter import *
from tkinter.ttk import Combobox


def change1(evnt):
    # global pos1
    global ent1
    global ent2

    if Entry2.get() != "":
        if not Entry2.get()[-1].isdigit() and Entry2.get()[-1] != ".":
            Entry2.config(state="normal")
            Entry2.delete(len(Entry1.get()) - 1, END)
            Entry2.config(state="disabled")
        else:
            pos1 = names.index(cb1.get())
            pos2 = names.index(cb2.get())
            ent2 = float(Entry2.get())
            ent1 = ent2 * conversionMatrix[pos2][pos1]
            Entry1.delete(0, END)
            Entry1.insert(0, str(ent1))
    else:
        Entry1.delete(0, END)


def change2(evnt):
    # global pos2
    global ent1
    global ent2

    if Entry1.get() != "":
        if not Entry1.get()[-1].isdigit() and Entry1.get()[-1] != ".":
            Entry1.delete(len(Entry1.get())-1, END)
        else:
            pos1 = names.index(cb1.get())
            pos2 = names.index(cb2.get())
            ent1 = float(Entry1.get())
            ent2 = ent1 * conversionMatrix[pos1][pos2]
            Entry2.config(state="normal")
            Entry2.delete(0, END)
            Entry2.insert(0, str(ent2))
            Entry2.config(state="disabled")
    else:
        Entry2.config(state="normal")
        Entry2.delete(0, END)
        Entry2.config(state="disabled")

conversionMatrix = [
                      [1, 0.1, 0.001, 0.000001, 0.0393701, 0.00328084, 0.00109361, 6.2137e-7],  # millimeters
                      [10, 1, 0.01, 0.00001, 0.393701, 0.0328084, 0.0109361, 6.2137e-6],  # centimeters
                      [1000, 100, 1, 0.001, 39.3701, 3.28084, 1.09361, 0.000621371],  # meter
                      [1000000, 100000, 1000, 1, 39370.1, 3280.84, 1093.61, 0.621371],  # kilometer
                      [25.4, 2.54, 0.0254, 0.0000254, 1, 0.0833333, 0.0277778, 0.0000158],  # inchs
                      [304.8, 30.48, 0.3048, 0.0003048, 12, 1, 0.333333, 0.000189394],  # foots
                      [914.4, 91.44, 0.9144, 0.0009144, 36, 3, 1, 0.000568182],  # yards
                      [1609344, 160934.4, 1609.344, 1.609344, 63360, 5280, 1760, 1]  # mile
                    ]

names = ["millimeter", "centimeter", "meter", "kilometer", "inch", "foot", "yard", "mile"]

wnd = Tk()
wnd.title("Unit Converter for length")
wnd.geometry("440x120+500+200")
wnd.resizable(False, False)

ent1 = StringVar()
ent2 = StringVar()
ent1.set("")
ent2.set("")
index = 0

# my_font = ("Calibri", 12, "bold")

lbl = Label(master=wnd, text="Unit Converter for length")
lbl.configure(font=("Calibri", 24, ))
lbl.place(x=5, y=0)

Entry1 = Entry(wnd, width=20, textvariable=ent1)
Entry1.configure(font=("Calibri", 14, "bold"))
Entry1.bind("<KeyRelease>", change2)
Entry1.place(x=10, y=45)

cb1 = Combobox(wnd, state="readonly")
cb1.configure(values=names)
cb1.current(index)
cb1.configure(font=("Calibri", 14))
cb1.bind("<<ComboboxSelected>>", change2)
cb1.place(x=10, y=80, width=205, height=30)

Entry2 = Entry(wnd, width=20, textvariable=ent2, state="disabled", disabledforeground="black")
Entry2.configure(font=("Calibri", 14, "bold"))
Entry2.bind("<KeyRelease>", change1)
Entry2.place(x=225, y=45)

cb2 = Combobox(wnd, state="readonly")
cb2.configure(values=names)
cb2.current(index)
cb2.configure(font=("Calibri", 14))
cb2.bind("<<ComboboxSelected>>", change2)
cb2.place(x=225, y=80, width=205, height=30)

wnd.mainloop()
