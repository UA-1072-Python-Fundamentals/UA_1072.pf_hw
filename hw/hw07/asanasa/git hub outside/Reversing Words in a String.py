input_str = input("Write your string fo reverse: ")

def reverse_words(input_str):
    words = input_str.split()
    reversed_str = ' '.join(reversed(words))
    return reversed_str



print("Your reverse string: ", reverse_words(input_str) )