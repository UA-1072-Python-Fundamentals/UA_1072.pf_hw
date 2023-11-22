def zero_fuel(distance_to_pump, mpg, fuel_left):
    return fuel_left * mpg >= distance_to_pump
    # Happy Coding! ;)


print(zero_fuel(50, 25, 2), True)
print(zero_fuel(100, 50, 1), False)
