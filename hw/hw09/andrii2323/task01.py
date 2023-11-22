import random

rand_number = random.randint(1, 100)
count = 1

while count <= 10:
    user_input = input("Please enter your guess: ")

    try:
        user_guess = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if user_guess < 1 or user_guess > 100:
        print("Please enter a number between 1 and 100.")
        continue

    if user_guess > rand_number:
        print("The entered number is bigger than the hidden one.")
    elif user_guess < rand_number:
        print("The entered number is smaller than the hidden one.")
    else:
        print("You won! The entered number is correct.")
        break

    if count == 10:
        print(f"You lose. The correct number was {rand_number}. Try again!")
    count += 1
