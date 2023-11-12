# HW01
#def find_largest_number(num1, num2):
   # return max(num1, num2)
#number1 = 153
#number2 = 235
#largest_number = find_largest_number(number1, number2)
#print(f"The largest number between {number1} and {number2} is: {largest_number}")

# HW3
def calculate_character_counts(input_string):
    char_counts = {}
    for char in input_string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1

    return char_counts
input_str = "ALer"
result = calculate_character_counts(input_str)
print(f"Input string: '{input_str}'")
print("Character counts:", result)
