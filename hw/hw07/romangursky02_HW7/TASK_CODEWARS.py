# Task -1 :Jenny's secret message
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return f"Hello, {name}!"

# Task -2: Find The Distance Between Two Points
# def distance(x1, y1, x2, y2):
#     return round(((x2-x1)**2 + (y2-y1)**2)**(1/2), 2)

# Task - 3: No yelling!
# def filter_words(st):
#     st = st.split()
#     st = " ".join(st)
#     st = st.capitalize()
#     return st
#

# Task - 4: Convert a Number to a String!
# def number_to_string(num):
#     num = str(num)
#     return num


# Task - 5: Reversing Words in a String
# def reverse(st):
#     st = st.split()
#     st = st[::-1]
#     st = " ".join(st)
#     return st
#
#
# Task - 6:Reverse List Order
# def reverse_list(l):
# #   return l.reverse()
#     l = l[::-1]
#     return l

# Task - 7 :Multiples of 3 or 5
# def solution(number):
#     if number == 0:
#         return 0
#     result = 0
#     for i in range(number):
#         if i % 3 == 0 or i % 5 == 0:
#             result += i
#
#     return result

# Task - 8 :Will you make it?
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     if distance_to_pump / mpg <= fuel_left:
#         return True
#     else:
#         return False

# Task - 9 :Are You Playing Banjo?
# def are_you_playing_banjo(name):
#     if name and (name[0] == 'R' or name[0] == 'r'):
#         return name + " plays banjo"
#     else:
#         return name + " does not play banjo"

# Task - 10 :Convert boolean values to strings 'Yes' or 'No'
# def bool_to_word(boolean):
#     if boolean:
#         return "Yes"
#     else:
#         return "No"

# Task - 11 :Counting sheep...
# def count_sheeps(sheep):
#     count = sheep.count(True)
#     return count

# # Task - 12 :Is this my tail?
# def correct_tail(body, tail):
#     return body[-1] == tail
