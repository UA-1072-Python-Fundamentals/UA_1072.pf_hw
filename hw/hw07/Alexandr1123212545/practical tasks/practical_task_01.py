# Jenny's secret message

def greet(name):
    if name == "Johnny":
        return f"Hello, my love!"
    return "Hello, {name}!".format(name=name)


if __name__ == "__main__":
    print(greet("James"))    # Hello, James!
    print(greet("Jane"))     # Hello, Jane!
    print(greet("Jim"))      # Hello, Jim!
    print(greet("Johnny"))   # Hello, my love!