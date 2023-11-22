import random
def guess_the_number():
    secret_number = random.randint(1, 100)
    max_attempts = 10
    print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

    for attempt in range(1, max_attempts + 1):
        # Get user input for the guess
        user_guess = int(input("Enter your guess: "))
        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempt} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")
        if attempt == max_attempts:
            print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")
if __name__ == "__main__":
     guess_the_number()