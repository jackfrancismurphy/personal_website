def zero_fuel(distance_to_pump, mpg, fuel_left):
    return not fuel_left*mpg < distance_to_pump