# Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"

#Find The Distance Between Two Points
import math
def distance(x1, y1, x2, y2):
    d = (x2-x1)**2 + (y2-y1)**2
    square_root = math.sqrt(d)
    result = round(square_root, 2)
    return result

#No yelling!

def filter_words(st):
    return " ".join(st.split()).capitalize

#Convert a Number to a String
def number_to_string(num):
    return str(num)