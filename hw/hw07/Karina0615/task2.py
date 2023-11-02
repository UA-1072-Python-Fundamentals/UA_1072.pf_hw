def area_rectangle(length=1,width=1):
    
    length = int(input("Please, enter a length of rectangle "))
    width = int(input("Please, enter a width of rectangle  "))
    a_rect = length*width
    return (f"The area of rectangle is {a_rect}")


def area_triangle(base=1, hight=1):

    base = int(input("Please, enter a base of triangle "))
    hight = int(input("Please, enter a hight of triangle "))
    a_t = 1/2*base*hight
    return (f"The area of triangle is {a_t}")


def area_circle(radius=1):

    radius = int(input("Please, enter a radius of circle "))
    PI = 3.14
    a_circ = PI * radius * radius
    return (f"The area of circle is {a_circ}")


def area_calculation():

    shape = input("Please, chose a geometric shape. Rectangle or triangle or circle? ")
    if shape.lower() == "rectangle":
        return area_rectangle(1,1)
    elif shape.lower() == 'triangle':
        return area_triangle(1,1)
    else:
        return area_circle(1)
    

print(area_calculation())
