class Human():
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

def God() -> list:
    m, w = Man(), Woman()
    return [m, w]


if __name__ == "__main__":
    paradise = God()
    print(isinstance(paradise[0], Man))

