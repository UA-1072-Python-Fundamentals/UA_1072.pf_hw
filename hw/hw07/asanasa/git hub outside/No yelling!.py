my_string = input("Write your string: ")

def normal_string(my_string):
    word = my_string.capitalize()
    words = word.split()
    filtered_str = ' '.join(words)
    return filtered_str
print(normal_string(my_string))