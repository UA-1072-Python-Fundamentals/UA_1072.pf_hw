name = input("Write your name: ")

def greeting():
    if name != "Johnny":
        return f"Hello, {name}! Nice to see you."
    else:
        return "Hello, my love!"


print (greeting())