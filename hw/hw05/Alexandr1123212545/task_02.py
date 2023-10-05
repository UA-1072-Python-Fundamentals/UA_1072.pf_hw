num = int(input('Enter your nymber '))
f1 = step = 0
f2 = 1
while f1 < num:
    print(f1, end=' ')
    f1, f2 = f2,f1 + f2 
    step += 1