class Human:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        return f"Hello, I am {self.name}."

    @classmethod
    def species_info(cls):
        return "I am a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

