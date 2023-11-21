def distance(x1, y1, x2, y2):
    x = x1-x2
    y = y1-y2
    return round((x**2+y**2)**(1/2),2)
    # Your code here
print( distance(1, 1, 0, 0))