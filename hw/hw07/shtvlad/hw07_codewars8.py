to_pump=int(input("How far is nearest pump: "))
gal=int(input("How much gallons are there left?: "))
fuel_cons=int(input("What is your fuel consumption?: "))
demand=to_pump/fuel_cons
print(True if demand<=gal else False)




