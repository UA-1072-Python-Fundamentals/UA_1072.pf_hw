  ## Assign the symbol for user`s choice
def figure():
    print('R - for rectangle')
    print('T -for triangle')
    print('C - for circle')

  ## Define calculations of areas
def rectangle_area(length, width):
    return  length * width

def triangle_area(base, height):
    return  (base * height)/2

def circle_area(radius):
    return 3.14 * radius**2

  ## Entering message for user
user_choice = input('Enter the symbol -  \n'
                    'R - for rectangle\n'
                    'T - for triangle\n'
                    'C - for circle\n'
                    'to receive the calculation of the area:  ').lower()

  ## Calculations based on users choice
if user_choice == 'r':
    length = float(input('Enter length, cm: '))
    width = float(input('Enter width, cm: '))
    area = round(rectangle_area(length, width),2)
    print(f'The area of the Rectangle is:  {area} cm².')

elif user_choice == 't':
    base = float(input('Enter base, cm: '))
    height = float(input('Enter height, cm: '))
    area = round(triangle_area(base, height),2)
    print(f'The area of the Triangle is:  {area} cm².')

elif user_choice == 'c':
    radius = float(input('Enter radius, cm: '))
    area = round(circle_area(radius),2)
    print(f'The area of the Circle is:  {area} cm².')

  ## Correction of the input mistake from user
else:
    print('Symbol Error. Enter a correct symbol  for chosen figure.')

