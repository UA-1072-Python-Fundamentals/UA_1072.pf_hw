import module
choice=int(input("Choose the figure:\n"
                 "1 - rectangle\n"
                 "2 - triangle\n"
                 "3 - circle\n"
                 "Your choice: "))

match choice:
    case 1:
        print("Input rectangle's measures:")
        a=int(input("a="))
        b=int(input("b="))
        print("Area of rectangle =",module.rectangle(a,b))
    case 2:
        print("Input triangle's measures:")
        a = int(input("h="))
        b = int(input("a="))
        print("Area of triangle =", module.triangle(a, b))
    case 3:
        print("Input circle radius:")
        a = int(input("r="))
        print("Area of circle =", module.circle(a))
