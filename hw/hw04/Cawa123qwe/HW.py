
celsius = float(input("temp: "))
if celsius > -273.15:
    fahrenheit = (celsius * 9/5) + 32
    print("ok")
    print (f"{celsius}°C is equivalent to {fahrenheit}°F")
else:
    print("error")

