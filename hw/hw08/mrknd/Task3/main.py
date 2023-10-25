from other import area_rectangle, area_triangle, area_circle


def calculates_area():
    while True:
        ask = int(input("""Enter a number what area do you want calculates:
        1 - area of a rectangle
        2 - area of a triangle
        3 - area of a circle
        0 - Exit
        Your choice: 
        """))

        if ask == 1:
            a = float(input("Enter side A: "))
            b = float(input("Enter side B: "))
            print("Area of your rectangle is: ", area_rectangle(a, b))

        elif ask == 2:
            h = float(input("Enter the height: "))
            a = float(input("Enter the side : "))
            print("Area of your triangle is: ", area_triangle(h, a))

        elif ask == 3:
            r = float(input("Enter the radius: "))
            print(area_circle(r))

        else:
            print('Goodbye!')
            break


calculates_area()
