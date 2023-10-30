# Task 3
input_word = input("Enter the word to calculate letters: ")


def char_calculator(word):
    char_count = {}

    for x in word:
        if x in char_count:
            char_count[x] += 1
        else:
            char_count[x] = 1
    return char_count


print("Result: ", char_calculator(input_word))



