def solution(number):
    l = []
    if number<0:
        return 0
    else:
        for i in range(number):
            if i % 3 == 0 or i % 5 == 0:
                l.append(i)       
    return sum(l)
                