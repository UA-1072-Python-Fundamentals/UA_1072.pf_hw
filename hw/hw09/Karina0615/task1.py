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
    # canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    root.title("Guess the number")
    # canvas.pack()
    lower_frame = tk.Frame(root, bg='white', bd=10)
    lower_frame.pack()

    msg2 = tk.Label(lower_frame,font=('Courier', 14), text = 'Well, I am thinking of a number between 1 and 100.')
    msg3 = tk.Label(lower_frame,font=('Courier', 14), text = 'Be aware, you have only 10 attempts')

    msg2.pack()
    msg3.pack()

    frame = tk.Frame(root, bg="grey", bd=5)
    frame.pack()

    guess_number = tk.Entry(root)
    guess_number.pack()

    global label
    label = tk.Label(frame, font=('Courier', 14))
    label.pack()

    b1 = tk.Button(root, text = 'get', width = 10, command = lambda:get_number(guess_number.get()))
    b1.pack()

   

    root.mainloop()

display()
