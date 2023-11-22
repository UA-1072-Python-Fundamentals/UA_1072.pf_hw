def reverse_list(l):
    a = []
    for i in range(1, len(l) + 1):
        a.append(l[-i])
    return a


print(reverse_list([1, 2, 3, 4]))
print(reverse_list([3, 1, 5, 4]))
print(reverse_list([3, 6, 9, 2]))
print(reverse_list([1]))