x = range(1, 11)
for y in x:
    if (y %2 == 0):
        print(y, "Divisible by 2")
    elif y %3 == 0:
        print(y, "Divisible by 3")
    elif y /3 != 0 and y /2 != 0:
        print(y, "Are not divisible by 2 and 3")
