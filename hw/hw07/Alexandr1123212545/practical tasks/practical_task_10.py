# Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


if __name__ == "__main__":
    print(bool_to_word(True))  # 'Yes'
    print(bool_to_word(False)) # 'No'