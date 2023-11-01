d2=set()
d3=set()
for i in range(1, 10+1):
    if i%2==0:
        d2.add(i)
    elif i%3==0:
        d3.add(i)
print(d2, d3, d2|d3, end="\n")