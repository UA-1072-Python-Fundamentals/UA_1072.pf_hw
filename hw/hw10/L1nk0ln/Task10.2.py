class Human:
    def hello(name):
        return f"Hello, {name}"
    @staticmethod
    def arbitrary():
        return "by L1nk0ln"
    @classmethod
    def homos(cls):
        return "You're homosapiens species"
a = input("Enter your name: ")
print(Human.hello(a))
print(Human.arbitrary())
print(Human.homos())