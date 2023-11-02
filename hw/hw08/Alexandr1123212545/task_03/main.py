from area_calculation import *



def user_choice():
    choice = 'start'

    while choice != 'quit':
        print('The area of ​​which figure do you want to calculate?\n1 rectangle \n2 triangle \n3 circle \nor enter 4 to exit')
        choice = int(input('Make your choice...\n'))
        match choice:
            case 1:
                a, b = [float(x) for x in input('Enter the parameters of the two sides separated by a space\n').split()]
                print(area_rectangle(a, b), '\n')
            case 2:
                h, base = [float(x) for x in input('Enter high and base of triangle separated by a space\n').split()]
                print(area_triangle(h, base), '\n')
            case 3:
                r = float(input('Enter a radius of circle \n'))
                print(area_circle(r), '\n')
            case 4:
                print('Come again\n')
                break

user_choice()
