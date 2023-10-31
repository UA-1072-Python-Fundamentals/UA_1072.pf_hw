def reverse_list(input_list):
    return list(reversed(input_list))


user_input = input("Enter a list of values separated by spaces: ")
user_list = [int(x) for x in user_input.split()]


reversed_list = reverse_list(user_list)


print("Original List:", user_list)
print("Reversed List:", reversed_list)
