# Task 1

list1 = []
list2 = []
list3 = []
for x in range(1, 10):
    if x % 2 == 0:
        list1.append(x)
    elif x % 3 == 0:
        list2.append(x)
    else:
        list3.append(x)

print("Numbers that are even and devisible by 2: ", list1)
print("Numbers that are odd and devisible by 3: ", list2)
print("Numbers that are not devisible by 2 and 3: ", list3)