#Task1
def largest_number(num1, num2):
    '''This function returns the largest number of two numbers'''
    if num1>num2:
        return num1
    elif num2>num1:
        return num2
    
user_number_1=int(input('What`s your first number?'))
user_number_2=int(input('What`s your second number?'))
user_largest_number=largest_number(user_number_1,user_number_2)
print(f'Your largest number is {user_largest_number}')

#Task2
def triangle_area(height,base):
    area=0.5*height*base
    return area

def rectangle_area (length, width):
    area=length*width
    return area

def circle_area(radius):
    area=3.14*(radius**2)
    return area

user_shape=str(input('What is your shape: triangle, rectangle, circle?'))
user_shape=user_shape.lower()

if user_shape=='triangle':
    user_height=float(input('What is the height of your triangle?'))
    user_base=float(input('What is the base of your triangle?'))
    user_triangle_area=triangle_area(user_height, user_base)
    print(f'The area of the triangle is {user_triangle_area}')
elif user_shape=='rectangle':
    user_length=float(input('What is the length of the rectangle?'))
    user_width=float(input('What is the width of the rectangle?'))
    user_rectangle_area=rectangle_area(user_length, user_width)
    print(f'Your rectangle area is {user_rectangle_area}')
elif user_shape=='circle':
    user_radius=float(input('What is the radius?'))
    user_circle_area=circle_area(user_radius)
    print(f'Your circle area is {user_circle_area}')

#Task3
def letters_number(word):
    letter_count={}
    for l in word:
        letter_count[l]=letter_count.get(l,0)+1
    return letter_count

user_word=input('What is your word?')
user_count=letters_number(user_word) 
print(user_count)   



