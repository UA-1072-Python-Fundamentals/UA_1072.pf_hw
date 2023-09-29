# Temperature Converter

def converter(temp):
    if ( temp > -273.15 ):
        F = (temp * 9 / 5) + 32
        return f"{temp}°C is equivalent to {F}°F"
    else:
        return (f"Error: Temperature below "
                f"absolute zero (-273.15°C)")

C = float(input("Input temperature in Celsius: "))
print(converter(C))