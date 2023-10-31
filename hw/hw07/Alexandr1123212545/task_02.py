import math

def calc_area_triangele(side1: float, side2: float, side3: float) -> float:
    """Return area of triangle.

    :param side1: side1 lenght
    :type side1: float
    :param side2: side2 lenght
    :type side2: float
    :param side3: side3 lenght
    :param s: Heron's formula
    :type s: float
    :param p: semiperimeter
    :type p: float
    :return: area of a triangle according to Heron's formula
    """
    p = (side1 + side2 + side3) / 2
    s = math.sqrt(p * (p - side1) * (p - side2) * (p - side3))
    return s


def calc_area_circle(r: float) -> float:
    """Return area of circle.

    :param r: radius of circle
    :type r: float
    :param s: area of circle formula
    :type s: float
    :return: multiplication
    :rtype: float
    """
    s = math.pi * r**2
    return s


def calc_area_rectangle(side1: float, side2: float) -> float:
    """Return area of rectangle.

    :param side1: side1 lenght
    :type side1: float
    :param side2: side2 lenght
    :type side2: float
    :param s: area of rectangle formula
    :type s: float  
    :return: area of rectangle
    :rtype: float
    """
    s = side1 * side2
    return s


def call_action():
    """Select calculation. 
    The user must selected which figure will be calculated.
    Rectangle, triangle, circle.
    """

    print('Hello! \nYou can calculate the area of ​​any of the three figures.')
    while True:
        print('1 - area of triangle \n2 - area of rectangle \n3 - area of circle')
        user_choice = int(input('Make your choice\n'))
        match user_choice:
            case 1:
                side1, side2, side3 = map(float, input('Enter parametrs of \
                                                       three sides siparated by a space \n').split())
                print(calc_area_triangele(side1, side2, side3))
            case 2:
                side_a, side_b = map(float, input('Enter parametrs of two sides \
                                                  siparated by a space \n').split())
                print(calc_area_rectangle(side_a, side_b))
            case 3:
                radius = float(input('Enter radius of circle \n'))
                print(calc_area_circle(radius))
        if input('Try again? Yes - [Y], No - anything...\n').lower() == 'y':
            continue
        else:
            print('Good Luck =)')
            break


if __name__ == "__main__":
    call_action()