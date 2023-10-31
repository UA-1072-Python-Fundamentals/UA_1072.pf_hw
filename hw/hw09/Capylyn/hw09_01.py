import random

rand_number = random.randint(1, 100)
count = 1

while count <= 10:
    user_guess = int(input("Please enter your guess: "))
    if user_guess > rand_number:
        print("The entered number is bigger than the hidden one.")
    elif user_guess < rand_number:
        print("The entered number is smaller than the hidden one.")
    else:
        print("You won! The entered number is correct.")
        break

    if count == 10:
        print("You lose. Try again!")
    count += 1