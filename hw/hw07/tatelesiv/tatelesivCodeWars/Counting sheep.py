def count_sheeps(array):
    return array.count(True)


sheep_list = [True, True, True,
              False, True, True,
              True, True, True,
              False, True, False,
              True, False, False,
              True, True, True,
              True, False, False,
              True, True]

sheep_count = count_sheeps(sheep_list)
print("The number of sheep present is:", sheep_count)
