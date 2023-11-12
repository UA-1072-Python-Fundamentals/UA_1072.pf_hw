def count_sheeps(sheep):
    return sheep_array.count(True)



sheep_array = [True, True, True, False,
               True, True, True, True,
               True, False, True, False,
               True, False, False, True,
               True, True, True, True,
               False, False, True, True]

result = count_sheeps(sheep_array)
print("Number of sheep present:", result)