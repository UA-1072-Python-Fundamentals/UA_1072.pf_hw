c = int(input("Enter the temperature in celsius: "))
absolute_zero = int(-273.15)
if c > absolute_zero:
    print((c*9/5)+32)
else:
    print("Error: Temperature below absolute zero (-273.15°C)")