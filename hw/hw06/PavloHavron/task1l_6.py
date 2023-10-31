even = []
odds = []
list3 = []
for i in range(10):
    if i%2==0:
        even.append(i)
    elif i%3==0:
        odds.append(i)
    elif i%2 or 3!=0:
        list3.append(i)
print(even)
print(odds)
print(list3)