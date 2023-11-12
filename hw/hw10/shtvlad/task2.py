class Human():
    species="Homo sapien"
    def __init__(self,name):
        self.name=name

    def greet(self):
        print(f"Hello, {self.name}")
    @classmethod
    def spicies(cls):
        print(f"You are {cls.species}")
    @staticmethod
    def definicion():
        print("The word 'Homo sapien' means 'the wise human'")
h=Human('Nick')
h.greet()
h.spicies()
h.definicion()
