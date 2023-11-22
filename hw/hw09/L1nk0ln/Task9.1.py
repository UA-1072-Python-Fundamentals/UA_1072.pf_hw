#importing files
import random
from tkinter import *
from tkinter import ttk

#The root
win= Tk()
#The auto dimension of the window
win.geometry("1920x1720")
#defining the tries of the play
tries = 0
#function that displays if the user wins or loses and records attempts
def display_text():
    #taking the random number
    number = random.randint(1, 101)
    #Global the variables of the number of tries
    global tries
    global triess
    #check if the user have more tries or he finished all tries
    if tries < 10:
        #Globaling the entry variable that contains the box to be used out of the function
        global entry
        #Taking the value of the user try
        string = entry.get()
        #check if the code is more than the random number
        if int(string) > number:
            #printing on screen
            b = Label(win, text="Your number more than mine", font=("Courier 22 bold"))
            #showing the label on the screen
            b.pack()
            #define a variable to be used in showing the user the number of attempts and storage the number of tries in it
            triess = "Your attempts " + str(tries)
            #printing on screen
            v = Label(win, text=triess, font=("Courier 22 bold"))
            #showing on screen
            v.pack()
        #check if the code is less than the random number
        if int(string) < number:
            ## All the codes are explained in the previous if statment
            c = Label(win, text="Your number less than mine", font=("Courier 22 bold"))
            c.pack()
            triess = "Your attempts " + str(tries)
            v = Label(win, text=triess, font=("Courier 22 bold"))
            v.pack()
        #check if the code is equal to the random number
        if int(string) == number:
            #The number of tries has been converted into a string in order to print it
            tries = str(tries)
            d = Label(win, text="Congratulation, you're win", font=("Courier 22 bold"))
            d.pack()
            v = Label(win, text=triess, font=("Courier 22 bold"))
            v.pack()
        #the if statement checks if the user has won to stop increasing the number of tries
        if int(string) == number:
            pass
        else:
            tries += 1
    #in case there aren't more tries
    else:
        d = Label(win, text="Unfortunately, you're loser", font=("Courier 22 bold"))
        d.pack()
        v = Label(win, text=triess, font=("Courier 22 bold"))
        v.pack()

#The box which the user will write in int his prediction
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack()
#button to enter the prediction
ttk.Button(win, text= "Okay",width= 20, command= display_text).pack(pady=20)

win.mainloop()