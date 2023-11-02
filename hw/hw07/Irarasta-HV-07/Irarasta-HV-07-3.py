## Get input from user
text = input('Enter any message here : ')

## Initialize empty dictionary
char_number = {}

## Count the occurence of each character
for char in text:
    if char in char_number:
        char_number[char] += 1
    else:
        char_number[char] = 1

## Display the result
print('We have this number of each character in your message: ')
for char, number in char_number.items():
    print(f'"{char}" : {number}')

