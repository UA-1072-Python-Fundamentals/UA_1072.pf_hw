from areal1 import areacirc, areatria, arearec

def main():
    choice = input("The area of which figure do you want to find?\n Circle - 1\n Rectangle - 2\n Triangle - 3\n")
    if int(choice) == 1:
        r = int(input("Enter the radius of circle: "))
        areacirc(r)
    elif int(choice) == 2:
        a = int(input("Enter the first base of rectangle: "))
        b = int(input("Enter the second base of rectangle: "))
        arearec(a,b)
    elif int(choice) == 3:
        a = int(input("Enter the base of triangle: "))
        h = int(input("Enter the height of tringle: "))
        areatria(a, h)
    else:
        print("Invalid symbol")

if __name__ == "__main__":
    main()
