C = int(input("Please, enter a temperature in Celsius"))
f = int(C*(9/5)+32)
r ="{}°C is equivalent to {} °F".format(C,f)
print(r)
if C < -273.15:
    print("Error:Temperature below absolute zero (-273.15°C)")
    