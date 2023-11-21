def count_sheeps(sheep):
  n = sheep.count(True)
  return n


array1 = [True, True, True, False,
          True, True, True, True,
          True, False, True, False,
          True, False, False, True,
          True, True, True, True,
          False, False, True, True];

result = count_sheeps(array1)
print(result, 17, f"There are 17 sheeps in total, not {result}")