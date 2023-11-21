import random
x = random.randint(1, 100)
count = 0
while count<=10:
    guess = int(input("Let's play:) Please, guess the number. You have 10 attempts! "))
   
    if x<guess:
        print("Your number is greater than the number you guess.")
    elif x>guess:
        print("Your number is lesser than the number you guess.")
    elif x==guess:
        print("Congratulations, you guessed it")
        break
    if count == 10:
        print("You have used 10 attempts. Game over. Try again!")
    count += 1