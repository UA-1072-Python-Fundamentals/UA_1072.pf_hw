# Multiples of 3 or 5
from functools import reduce


def solution(number):
    return reduce(lambda x, y: x + y if not (y % 3 and y % 5) else x, range(number), 0)


if __name__ == "__main__":
        print(solution(4))   # 3
        print(solution(6))   # 8
        print(solution(16))  # 60
        print(solution(3))   # 0
        print(solution(5))   # 3
        print(solution(15))  # 45
        print(solution(0))   # 0
        print(solution(-1))  # 0
        print(solution(10))  # 23
        print(solution(20))  # 78
        print(solution(200)) # 9168