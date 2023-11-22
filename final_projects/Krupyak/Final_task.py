def add(x, y):
    return x + y
def cos(a):
    return cos(a)

def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def exponentiation(x, y):
    return x ** y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exponentiation")

while True:
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ('1', '2', '3', '4', '5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError as err:
            print("Invalid input. Please enter a number.", type(err), err)
            continue
        if num2 == 0:
            try:
                num1/num2
            except ZeroDivisionError as err:
                print("Invalid input. Division by zero.", type(err), err)
                continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        elif choice == '5':
            print(num1, "**", num2, "=", exponentiation(num1, num2))

        next_calculation = input("Do you want the next calculation? If 'Yes' press Y, if 'No' press N): ")
        if next_calculation == "N":
            break
        if next_calculation == "Y":
            continue
        else:
            break
    else:
        print("Invalid Input")
