import random


def guess_the_number():
    # Generate a random number between 1 and 100
    target_number = random.randint(1, 100)

    # Set the maximum number of attempts
    max_attempts = 10

    print("Welcome to the Guess the Number game!")
    print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        # Get the user's guess
        user_guess = int(input("Enter your guess: "))

        # Check if the guess is correct
        if user_guess == target_number:
            print(f"Congratulations! You guessed the number {target_number} in {attempt} attempts.")
            break
        elif user_guess < target_number:
            print("The target number is greater than your guess. Try again.")
        else:
            print("The target number is less than your guess. Try again.")

    else:
        print(f"Sorry, you've run out of attempts. The correct number was {target_number}.")


# Run the game
guess_the_number()
