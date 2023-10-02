cel=int(input("Enter the temperature in Celsius: "))
if cel>=-273.15:
    fahr=(cel*9/5)+32
    print(f"{cel}\u00b0C is equivalent to {fahr}\u00b0F")
else:
    print(f"Error: Temperature below absolute zero (-273.15\u00b0C)")
