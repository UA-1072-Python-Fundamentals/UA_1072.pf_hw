1. Jennys Secret Message

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
2. Find The Distance Between Two Points

def distance(x1, y1, x2, y2):
    return round(((x2-x1)**2+(y2-y1)**2)**0.5, 2)

3. No yelling!

def filter_words(st):
    a = st.casefold()
    b = a.capitalize()
    c = b.split()
    d = " ".join(c)
    return d
    pass

4. Convert a Number to a String

def number_to_string(num):
    return str(num)

5. Reversing Words in a String

def reverse(st):
    l = st.split()
    st = " ".join(l[::-1])
    return st
6. Reverse List Order


def reverse_list(l):
    'return a list with the reverse order of l'

    l.reverse()
    return l

7. Multiples of 3 or 5


def solution(number):
    if number < 0:
        return 0
    result = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)
    return sum(result)

8. Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump <= mpg * fuel_left:
        return True
    elif distance_to_pump > mpg * fuel_left:
        return False

9. Are You Playing Banjo?

def are_you_playing_banjo(name):
    if name.find("R") == 0 or name.find("r") == 0:
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

10.Convert boolean values to strings 'Yes' or 'No’

def bool_to_word(boolean):
    if boolean == True:
        return "Yes"
    elif boolean == False:
        return "No"

11. Counting sheep


def count_sheeps(sheep):
    return sheep.count(True)

12. Is this my tail?

def correct_tail(body, tail):
    body.split()
    if body[-1] == tail:
        return True
    else:
        return False




