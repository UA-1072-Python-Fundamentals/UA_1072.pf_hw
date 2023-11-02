# 10.2

class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"\n{self.welcome()}\n{self.species()}\n{self.arb_mes()}"

    def welcome(self):
        return f"Hello, {self.name}. Welcome!"

    @classmethod
    def species(cls):
        return "Species of Homosapiens"

    @staticmethod
    def arb_mes():
        return "That is a static method"


c = Human("Bob")
b = Human("Amber")
print(c, b)

