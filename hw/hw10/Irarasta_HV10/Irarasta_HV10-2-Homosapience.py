class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f'Welcome, {self.name}'

    @classmethod
    def species_info(cls):
        return "You have been detected as species of Homo Sapiens."

    @staticmethod
    def arbitrary_message():
        return "No need to be that loud, no one can hear you anymore 👽. Welcome to the AREA 51."


person = Human("Liubomyr")

print(person.welcome_message())

print(Human.species_info())

# Call the static method to get an arbitrary message
print(Human.arbitrary_message())
