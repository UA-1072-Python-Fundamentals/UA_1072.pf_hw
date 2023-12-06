def divide_numbers():
    try:
        user_input = input("Enter two numbers separated by a comma (e.g., 5,2): ")
        num1, num2 = map(float, user_input.split(','))

        result = num1 / num2

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid input. Please enter two valid numbers separated by a comma.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    else:
        print(f"The result of {num1} / {num2} is: {result}")
    finally:
        print("Program execution complete.")

if __name__ == "__main__":
    divide_numbers()