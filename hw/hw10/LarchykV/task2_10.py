class Human:
    species = "Homo sapiens"

    def __init__(self, name: str):
        self.name = name

    def welcome(self):
        print(f"Hello, {self.name} :) Welcome!")

    @classmethod
    def species_inf(cls):
        print(f"Your species is: {cls.species}")

    @staticmethod
    def arbitrary_message():
        print("Let's begin our adventure!")


human1 = Human("Gehrman")
human1.welcome()
human1.species_inf()
human1.arbitrary_message()
