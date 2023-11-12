# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)


# II. Find The Distance Between Two Points
import math


def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 2)


# Example usage
x1, y1 = 1, 2
x2, y2 = 4, 6
distance = calculate_distance(x1, y1, x2, y2)
print("Distance:", distance)


#   III. No yelling!
def filter_words(s):
    words = s.split()
    words = [words[0].capitalize()] + [word.lower() for word in words[1:]]
    result = ' '.join(words)
    return result



# IV. Convert a Number to a String
def number_to_string(num):
    # Return a string of the number here!
    return str(num)


# V. Reversing Words in a String
def reverse(st):
    words = st.strip().split()[::-1]
    return ' '.join(words)


# VI. Reverse List Order
def reverse_list(l):
    return l[::-1]


# VII. Multiples of 3 or 5
def sum_of_multiples(n):
    if n < 0:
        return 0

    return sum(x for x in range(n) if x % 3 == 0 or x % 5 == 0)


# VIII. Will you make it?
def zeroFuel(distance_to_pump, fuel_left, mpg):
    return fuel_left * mpg >= distance_to_pump


# IX. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return name + " plays banjo"
    else:
        return name + " does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(b):
    return "Yes" if b else "No"


# XI. Counting sheep

def count_sheeps(array):
    return array.count(True)


# XII. Is this my tail?
def correct_tail(body, tail):
    last_letter_body = body[-1]
    return last_letter_body == tail
