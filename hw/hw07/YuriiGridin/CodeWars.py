# I. Jenny's secret message
def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return f"Hello, {name}!"


# II. Find The Distance Between Two Points
def distance(x1, y1, x2, y2):
    return round(((x2-x1)**2 + (y2-y1)**2)**(1/2), 2)


# III. No yelling!
def filter_words(st):
    st = st.split()
    st = " ".join(st)
    st = st.capitalize()
    return st


# IV. Convert a Number to a String
def number_to_string(num):
    num = str(num)
    return num


# V. Reversing Words in a String
def reverse(st):
    st = st.split()
    st = st[::-1]
    st = " ".join(st)
    return st


# VI. Reverse List Order
def reverse_list(l):
    l = l[::-1]
    return l


# VII. Multiples of 3 or 5
def solution(number):
    s = []
    if number < 0:
        return 0
    else:
        for i in range(number):
            if i%3 == 0 or i%5 == 0:
                s.append(i)
        s = sum(s)
        return s


# VIII. Will you make it?
def zero_fuel(distance_to_pump, mpg, fuel_left):
    if distance_to_pump / mpg <= fuel_left:
        return True
    else:
        return False


# IX. Are You Playing Banjo?
def are_you_playing_banjo(name):
    return f"{name} plays banjo" if name[0] == "R" or name[0] == "r" else f"{name} does not play banjo"


# X. Convert boolean values to strings 'Yes' or 'No’
def bool_to_word(boolean):
    return "Yes" if boolean else "No"


# XI. Counting sheep
def count_sheeps(sheep):
    count = sheep.count(True)
    return count


# XII. Is this my tail?
def correct_tail(body, tail):
    sub = body[-1]
    if sub == tail:
        return True
    else:
        return False
