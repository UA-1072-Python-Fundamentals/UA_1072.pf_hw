def check_even_odd(number):
    try:
        number = int(number)
        if number % 2 == 0:
            return "Even"
        else:
            return "Odd"
    except ValueError:
        return "Invalid input. Please enter a valid integer."

def main():
    user_input = input("Enter an integer: ")
    result = check_even_odd(user_input)
    print(result)

if __name__ == "__main__":
    main()