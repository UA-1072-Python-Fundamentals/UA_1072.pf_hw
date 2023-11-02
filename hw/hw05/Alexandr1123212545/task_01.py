g# Option_1

length_list = int(input('Enter list length -> '))
some_list = list(range(length_list))
print(some_list)
for i in range(len(some_list)):
    some_list[i] = float(i)
print(some_list)
# Option 2

length_list = int(input('Enter list length -> '))
some_list = list(range(length_list))
print(some_list)
some_list = [float(some_list[i]) for i in range(len(some_list))] # Why did the id change?
print(some_list)