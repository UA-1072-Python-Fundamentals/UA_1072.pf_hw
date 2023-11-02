def greet(name):
    if name=="Johnny":
        print(f"Hello, {name}!\u2764\uFE0F")
    else:
        print(f"Hello, {name}!")

greet(input("What is your name?: ").title())