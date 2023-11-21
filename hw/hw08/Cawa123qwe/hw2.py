import re

def is_valid_password(password):
    # Check length
    if 6 <= len(password) <= 16:
        # Check for at least 1 lowercase letter
        if re.search("[a-z]", password):
            # Check for at least 1 uppercase letter
            if re.search("[A-Z]", password):
                # Check for at least 1 digit
                if re.search("[0-9]", password):
                    # Check for at least 1 special character from [$#@]
                    if re.search("[$#@]", password):
                        return True
                    else:
                        print("Password must contain at least 1 special character from [$#@]")
                else:
                    print("Password must contain at least 1 digit")
            else:
                print("Password must contain at least 1 uppercase letter")
        else:
            print("Password must contain at least 1 lowercase letter")
    else:
        print("Password length must be between 6 and 16 characters")
user_password = input("Enter your password: ")
if is_valid_password(user_password):
    print("Password is valid.")
else:
    print("Password is invalid.")
