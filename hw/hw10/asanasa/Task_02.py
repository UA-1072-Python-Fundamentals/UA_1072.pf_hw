class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, I am {self.name}!"

    @classmethod
    def species_info(cls):
        return "I am a species of Homosapiens."
    def arbitrary_message():
        return "This is an arbitrary message."

person1 = Human("Alice")
person2 = Human("Bob")


print(person1.say_hello())
print(person2.say_hello())


print(Human.species_info())


print(Human.arbitrary_message())