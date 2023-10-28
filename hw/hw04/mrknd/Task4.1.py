temp_cel = float(input("Enter a temperature and I will convert it to Fahrenheit: "))

if temp_cel <= 273.15:
    temp_fahr = (temp_cel * 9/5) + 32
    print(f"It will be {temp_fahr}F")
else:
    print("Error: Temperature below absolute zero (-273.15°C)")