#Task3
number = int(input("Please, enter a number to calculate its factorial: "))

if number < 0:
    print("Sorry, impossible to calculate the factorial :( ")
else:
    fact = 1
    for x in range(1, number+1):
        fact *= x
    print("The result would be: ", fact)