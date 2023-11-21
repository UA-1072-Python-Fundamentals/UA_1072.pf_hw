Temperature = float(input("Please enter the temperature in degrees Celsius: "))

if Temperature < -273.15:
	print("This number doesn't work for us because this temperature in the universe is also known as absolute zero")
else:
	result = Temperature * (9/5) + 32
	print(result)

