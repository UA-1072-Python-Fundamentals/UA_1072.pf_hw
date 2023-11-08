cel = float(input("to enter a temperature in Celsius: "))
zero = -273.15

if cel > zero:
    fahr = (cel * 9/5) + 32
    print (cel, "C is equivalent to", fahr, "F")
else:
    print("Error, you entered a temperature below -273.15")
