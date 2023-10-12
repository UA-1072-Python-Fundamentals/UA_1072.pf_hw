cel = float(input("Enter temperature in Celsius\n"))
F = ((cel * (9 / 5)) + 32)
if cel < -273.15:
    print("Error. Temperature below absolut zero")
else:
    print(F)