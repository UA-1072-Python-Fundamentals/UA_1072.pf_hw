# Simple: Find The Distance Between Two Points
import math

def calculate_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return round(distance, 2)


point1 = (1, 2)
point2 = (4, 6)
distance = calculate_distance(point1, point2)
print(f"The distance between {point1} and {point2} is {distance}")
