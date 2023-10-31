
  ## Write a program for area calculation, working inside another module

import math

def rectangle_area(width, length):
    return width * length

def triangle_area(height, base):
    return 0.5 * height * base

def circle_area(radius):
    return math.pi * pow(radius, 2)

if __name__ == '__main__':
    while True:
        print('Choose figure for area calculation:')
        print('Type "R" for rectangle')
        print('Type "T" for triangle')
        print('Type "C" for circle')

        choice = input('Enter the symbol of the figure to start calculation: ')

        if choice.lower() == 'r':
            width = float(input('Enter width, cm: '))
            length = float(input('Enter length, cm: '))
            area = rectangle_area(width, length)
            print(f'The area of the Rectangle is: {area} cm².')
            break

        elif choice.lower() == 't':
            height = float(input('Enter height, cm: '))
            base = float(input('Enter base, cm: '))
            area = round(triangle_area(height, base),2)
            print(f'The area of the Triangle is: {area} cm².')
            break

        elif choice.lower() == 'c':
            radius = float(input('Enter radius, cm: '))
            area = round(circle_area(radius), 2)
            print(f'The area of the Circle is: {area} cm².')
            break


        else:
            print('Make a correct choice.')
            break







