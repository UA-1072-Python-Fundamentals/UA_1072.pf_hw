  ## Guess game with 10 tries:
import random

gamehost_number = random.randint(1, 100) # Set guessing range 1 to 100
max_tries = 10 # Set max for user`s tries
users_tries = 0

print('Lets play a Guess Game!\n'
      'Guess the number between 1 and 100 in just 10 tries.')

while users_tries < max_tries:
    guess = int(input('Guess my number: '))
    users_tries += 1

    if guess  < gamehost_number:
        print('No, my number is greater.')
    elif guess > gamehost_number:
        print('No, my number is smaller.')
    else:
        print(f'Congrats! You win! \U0001F929 My guessed number is {guess}')
        break
if users_tries == max_tries:
    print('You lose! I win! \U0001F61C.')
