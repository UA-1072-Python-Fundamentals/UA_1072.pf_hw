def area(*arg):
    if len(arg) == 1:#radius
        return arg[0]**2*3.1415
    if len(arg) == 2:#height and width
        return arg[0]*arg[1]
    if len(arg) == 3:#three sides
        p=0
        for i in arg:
            p+=i
        p=p/2
        return (p*(p-arg[0])*(p-arg[1])*(p-arg[2]))**(1/2)

my_data = list(map(float, input("Enter data separated by a space to calculate the area\n").split()))

print(area(*my_data))