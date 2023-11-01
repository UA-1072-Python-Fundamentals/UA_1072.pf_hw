def rectangle():
    a = int(input("Input length: "))
    b = int(input("Input width: "))
    s=a*b
    return (s)
def triangle():
    a = int(input("Input height: "))
    b = int(input("Input base: "))
    s = a*b/2
    return (s)
def circle():
    a = int(input("Input radius: "))
    s = 3.14*a**2
    return (s)

figure=input("What figure's area would you like to calculate?\n"
             "1-rectangle, 2-triangle, 3-circle\n"
             "Please, make your choice: ")
match figure:
    case "1":
        print(f"Rectangle's area = {rectangle()}")
    case "2":
        print(f"Triangle's area = {triangle()}")
    case "3":
        print(f"Circle's area = {circle()}")