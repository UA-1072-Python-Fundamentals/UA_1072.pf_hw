# Task 7.3

def count_characters(stri):
    char_count = {}
    for char in stri:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count


stri = input("Enter your word, please: ")
result = count_characters(stri)
print(result)
