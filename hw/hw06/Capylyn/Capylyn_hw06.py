#Task 6.1
evenBy2 = []
oddBy3 = []
notDivisible = []
for i in range(1, 11):
    if not i % 2:
        evenBy2.append(i)
    elif not i % 3:
        oddBy3.append(i)
    else:
        notDivisible.append(i)


print("Even numbers in range from 1 to 10 that are divisible by 2:",', '.join(map(str, evenBy2)))
print("Odd numbers in range from 1 to 10 that are divisible by 3:",', '.join(map(str, oddBy3)))
print("Numbers that are not divisible by 2 and 3:",', '.join(map(str, notDivisible)))

#Task 6.2
loginEnter = input("Please enter your login: ")

while loginEnter != "First":
    loginEnter = input("The entered login is incorrect. Please enter the correct one: ")
    if loginEnter == "First":
        print("Welcome!")