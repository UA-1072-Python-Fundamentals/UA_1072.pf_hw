def is_valid_password(password):
    # Check the length of the password
    if len(password) < 6 or len(password) > 16:
        return False

    # Initialize flags for lowercase, uppercase, digit, and special character presence
    has_lower = False
    has_upper = False
    has_digit = False
    has_special = False

    special_characters = "$#@"

    # Check each character in the password
    for char in password:
        if char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True

    # Check if all criteria are met
    if has_lower and has_upper and has_digit and has_special:
        return True

    return False

# Get input from the user
password = input("Enter a password: ")

# Check the validity of the password
if is_valid_password(password):
    print("Password is valid.")
else:
    print("Password is not valid.")



    