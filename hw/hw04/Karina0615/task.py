cel = int(input("Enter the temperature in Celsius"))

if cel > -273.15:
    far = (cel * (9/5))+ 32
    print(f"{cel}\u00b0C is the equivalent to {far}\u00b0F")
else:
    print("Error: Temperature below absolute zero(-273.5\u00b0C)")