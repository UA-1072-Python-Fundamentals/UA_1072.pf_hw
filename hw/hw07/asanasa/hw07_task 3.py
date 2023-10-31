input_string = input("Input your string: ")
def count_characters(input_string):

    char_count = {}
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


result = count_characters(input_string)
print(result)
