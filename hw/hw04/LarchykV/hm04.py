celsius = float(input("Enter the temperature in Celsius: "))


def converter(celsius):
    if celsius < -273.15:
        print("Error: Temperature below absolute zero (-273.15C)")
    else:
        result = (celsius * 9/5) + 32
        print(celsius, "C is equivalent to ", result, "F")


result = converter(celsius)
