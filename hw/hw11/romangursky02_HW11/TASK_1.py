def process_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")

    result = "even" if age % 2 == 0 else "odd"
    print(f"The entered age {age} is {result}.")


try:
    user_age = int(input("Enter your age: "))
    process_age(user_age)
except ValueError as ve:
    print(f"Error: {ve}")
