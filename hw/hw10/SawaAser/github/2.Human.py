class Human:
    def __init__(self, name):
        self.name = name
        print("Welcome {}!".format(self.name))

    @classmethod
    def is_homosapiens(cls):
        return "This is homosapiens"

    @staticmethod
    def something():
        return 'arbitrary message'


somebody1 = Human("Sawa")
somebody2 = Human("Aser")
print(somebody1.something())