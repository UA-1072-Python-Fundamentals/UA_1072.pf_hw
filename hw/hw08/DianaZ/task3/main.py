import Area

print("Enter the first letter of the name of the shape whose area you want to find\n")
shape = input()
if shape == 'r':
    a, b = int(input("Enter the height ")), int(input("Enter the width "))
    print(Area.rectangle(a,b))
if shape == 't':
    h, a = int(input("Enter the height ")), int(input("Enter the length"))
    print(Area.triangle(a,h))
if shape == 'c':
    r = int(input("Enter the radius "))
    print(Area.circle(r))
