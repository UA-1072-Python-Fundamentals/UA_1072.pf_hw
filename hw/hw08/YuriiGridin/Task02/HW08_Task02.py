# Task02
def password_check():

    password = input("Input your password: ")
    check_set_letters_b = {chr(letter) for letter in range(ord("A"), ord("Z")+1)}
    check_set_letters_s = {chr(letter) for letter in range(ord("a"), ord("z")+1)}
    check_set_numbers = {str(number) for number in range(10)}
    check_set_character = {"$", "#", "@"}
    password_set = set(password)
    check = 0

    if not (6 <= len(password) <= 16):
        print(f"Minimum length 6 characters.\n"
                f"Maximum length 16 characters.")
        return password_check()

    if not ((password_set & check_set_letters_b) and (password_set & check_set_letters_s)):
        print(f"At least 1 letter between [a-z] and 1 letter between [A-Z].")
        check = 1
    if not (password_set & check_set_numbers):
        print(f"At least 1 number between [0-9].")
        check = 1
    if not (password_set & check_set_character):
        print(f"At least 1 character from [$#@].")
        check = 1
    if check == 1:
        return password_check()
    else:
        print("Your password is correct!")


password_check()