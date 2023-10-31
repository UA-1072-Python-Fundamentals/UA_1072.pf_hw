class Human:
    species = "Homosapiens"

    def __init__(self, name):
        self.name = name

    def welcomeMessage(self):
        return print(f"Hello, {self.name}")

    @classmethod
    def speciesMessage(cls):
        return f"Species is {cls.species}"

    @staticmethod
    def message(msg):
        return print(msg)


h1 = Human("Yura")
h1.welcomeMessage()
print(Human.species)
h1.message("It is an arbitrary message")


