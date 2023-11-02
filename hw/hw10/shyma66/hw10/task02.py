class Human:
    def __init__(self,name):
        self.name = name
    def message(self):
        return f"Welcome {self.name}"
    @classmethod
    def information_message(cls):
        return "It is a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

first_name = Human(input("Enter your name -> "))
print(first_name.message())  
second_name = Human(input("Enter your name -> "))


print(second_name.message())

print(Human.information_message())
print(Human.arbitrary_message())