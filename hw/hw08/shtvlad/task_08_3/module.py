import math
def rectangle(a,b):
    s=a*b
    return(round(s,2))
def triangle(a,b):
    s=0.5*a*b
    return (round(s,2))
def circle(a):
    s=math.pi*math.pow(a,2)
    return(round(s,2))