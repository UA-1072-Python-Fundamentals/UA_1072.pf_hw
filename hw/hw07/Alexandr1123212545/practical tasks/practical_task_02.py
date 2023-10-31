# Simple: Find The Distance Between Two Points
import math


def distance(x1, y1, x2, y2):
    result = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    return round(result, 2)


if __name__ == "__main__":
    print(distance(1, 1, 0, 0)) # 1.41