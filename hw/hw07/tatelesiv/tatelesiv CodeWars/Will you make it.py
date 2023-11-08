def can_reach_pump(distance, fuel_left, miles_per_gallon):
    max_distance = fuel_left * miles_per_gallon
    if max_distance >= distance:
        return True
    else:
        return False


distance_to_pump = 50
remaining_fuel = 2
miles_per_gallon = 25

result = can_reach_pump(distance_to_pump, remaining_fuel, miles_per_gallon)
print(result)
