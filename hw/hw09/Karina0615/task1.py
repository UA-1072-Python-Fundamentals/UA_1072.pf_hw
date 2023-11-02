import random
import tkinter as tk


number = random.randint(1, 100)
count = 0

def get_number(num):
    global count
    print(number, int(num))
    count += 1
    if int(num) == number:
        label.config(text="Good job! You are a winner!")
            
    elif count == 3:
        label.config(text = "You don`t have gueses anymore")

    elif 1 <= int(num) <= 100 and int(num) < number:
        label.config(text = "Your number is more.")
            
    elif 1 <= int(num) <= 100 and int(num) > number:
        label.config(text = 'Your number is more.')
            
    elif not 1 <= int(num) <= 100:
        label.config( text = 'Your number is not in the range 1 to 100. Try again:)')
        
        
        
def display():
    
    HEIGHT = 350
    WIDTH = 450

    root = tk.Tk()
    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    root.title("Guess the number")
    canvas.pack()
    lower_frame = tk.Frame(root, bg='gold', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')
    # lower_frame.pack()

    msg2 = tk.Label(lower_frame,font=('Courier', 14), text = 'Well, I am thinking of a number between 1 and 100.')
    msg3 = tk.Label(lower_frame,font=('Courier', 14), text = 'Be aware, you have only 10 attempts')

    msg2.place(relx=0, rely=0, relwidth=1, relheight=1)
    # msg2.pack()
    msg3.place(relx=0, rely=0, relwidth=1, relheight=1)
    # msg3.pack()

    frame = tk.Frame(root, bg="deep sky blue", bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')
    # frame.pack()

    guess_number = tk.Entry(root)
    guess_number.place(relx=0, rely=0, relwidth=0.65, relheight=1)
    # guess_number.pack()

    b1 = tk.Button(root, text = 'get', width = 10, command = lambda:get_number(guess_number.get()))
    b1.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)
    # b1.pack()

    

    global label
    label = tk.Label(lower_frame, font=('Courier', 14))
    label.place(relx=0, rely=0, relwidth=1, relheight=1)
    # label.pack()

   

    root.mainloop()

display()
