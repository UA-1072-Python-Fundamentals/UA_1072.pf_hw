from task3 import  *


type_of_figure = input("The area of ​​which figure you want to calculate?: Rectangle, Triangle or Circle? ")

if type_of_figure == "Rectangle":
    print(area_of_rectangle())
elif type_of_figure == "Cicle":
    print(area_of_cicle())
elif type_of_figure == "Triangle":
    print(area_of_triangle())
else:
    print("Sorry, there is no such figure.")
