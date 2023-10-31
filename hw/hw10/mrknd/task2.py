class Human:
    SPECIES = 'Homo Sapiens'

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f"Welcome {self.name}")

    @classmethod
    def species_info(cls):
        print(f"Your species is {cls.SPECIES}")

    @staticmethod
    def arbitrary_message():
        print("Do you think our species is the smartest in the universe?👀 ")


person = Human('Gandalf')
person.greeting()
Human.species_info()
Human.arbitrary_message()



