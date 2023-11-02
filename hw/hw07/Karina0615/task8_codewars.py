def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding! ;)
    consump = distance_to_pump / mpg
    if fuel_left >= consump:
        return True
    else:
        return False