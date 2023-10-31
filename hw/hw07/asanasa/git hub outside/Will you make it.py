def can_reach_pump(distance_to_pump, fuel_left, miles_per_gallon):

    max_distance = fuel_left * miles_per_gallon

    return max_distance >= distance_to_pump


distance_to_pump = 50
fuel_left = 2
miles_per_gallon = 25

result = can_reach_pump(distance_to_pump, fuel_left, miles_per_gallon)

if result:
    print("It is possible to reach the pump.")
else:
    print("It is not possible to reach the pump.")