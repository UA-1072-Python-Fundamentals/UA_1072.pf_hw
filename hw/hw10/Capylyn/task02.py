class Human():
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print(f"Hello {self.name}")

    def species(cls):
        return "This is a species of \"Homosapiens\""

    @staticmethod
    def staticmethod():
        return "Hello world"

ins = Human("Tkach")
ins.welcome()
print(ins.staticmethod())
print(ins.species())