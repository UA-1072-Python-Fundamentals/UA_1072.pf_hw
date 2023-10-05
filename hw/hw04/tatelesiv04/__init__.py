#task 1
C= float(input("Enter a temperature in Celsius: "))
if C < -273.15:
    print("Error")
else:
    F = (C * 9/5) + 32
    print(f"{C}°C is equivalent to {F}°F")
