def greetings(name):
    if name == "Johnny":
        return "Hello, darling!"
    else:
        return "Hello, {name}.".format(name=name)
print(greetings("John"))