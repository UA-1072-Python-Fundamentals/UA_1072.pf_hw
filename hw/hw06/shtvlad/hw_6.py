#task1
lst_even=[]
lst_odd=[]
lst_other=[]
for i in range(10):
    if (i+1)%2==0 and not (i+1)%3==0:
        lst_even.append(i+1)
    elif (i+1)%3==0 and not (i+1)%2==0:
        lst_odd.append(i+1)
    elif (i+1)%3==0 and (i+1)%2==0:
        lst_even.append(i + 1)
        lst_odd.append(i + 1)
    else:
        lst_other.append(i+1)
print(lst_even)
print(lst_odd)
print(lst_other)

#task2
login=input("Login: ")
while True:
    if login=="First":
        break
    else:
        login=input("Such user doesn't exist. Please, enter another login: ")
print(f"Welcome, {login}")
