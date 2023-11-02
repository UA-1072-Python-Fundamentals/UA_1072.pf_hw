
  ## 1- Jenny`s sectet message
def greet(name):
    if name != 'Johnny':
        result = "Hello, {name}!".format(name=name)
    else:
        result = "Hello, my love!"
    return result

names = ['Max', 'Nick', 'Tom', 'Johnny']
greetings = []

for name in names:
    greeting = greet(name)
    greetings.append(greeting)

for greeting in greetings:
    print(greeting)



  ## 2- Find the distance between two points# def distance(x1, y1, x2, y2):
import math

def calculate_distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    distance = math.sqrt(dx ** 2 + dy ** 2)
    return round(distance, 2)
x1 = 5
y1 = 6
x2 = 34
y2 = 18

result = calculate_distance(x1, y1, x2, y2)
print(f"The distance between the points is: {result}")


  ## 3-  Format the text with Upper and Lower case and with extra spaces
def filter_words(st):
    words = st.split()
    formatted_words = []

    for index, word in enumerate(words):
        if index == 0:
            formatted_word = word.capitalize()
        else:
            formatted_word = word.lower()
        formatted_words.append(formatted_word)

    formatted_result = ' '.join(formatted_words)
    return formatted_result

st = "WOW this is REALLY          amazing"
formatted_result = filter_words(st)
print(formatted_result)



  ## 4 -Integer to a string
def number_to_string(num):
    return f'{num}'

numbers = [123, 999, -100]
converted_strings = [number_to_string(num) for num in numbers]
print(converted_strings)












