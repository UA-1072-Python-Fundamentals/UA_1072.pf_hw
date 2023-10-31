name = input("Write your name: ")
name = name.lower()

def banjo(name):
    if name.startswith('r'):
        return name + " plays banjo"
    else:
        return name + " does not play banjo"

print (banjo(name))