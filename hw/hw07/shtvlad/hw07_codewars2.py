a=input("Input x1,y1: ")
b=input("Input x2,y2: ")
lst1=a.split(",")
lst2=b.split(",")

print(round((
    (int(lst2[0])-int(lst1[0]))**2+
    (int(lst2[1])-int(lst1[1]))**2)**0.5,2))