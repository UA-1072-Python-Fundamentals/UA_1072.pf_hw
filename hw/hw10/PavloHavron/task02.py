class Human():
    def __init__(self,name):
        self.name = name
    def welcome_message(self):
        print(f"My greetings {self.name} :)")

    def species(cls):
        return "A species of Homo sapiens."
     
    @staticmethod
    def staticmethod():
        return "May force be with you!"
    
x = Human("Jackson")
x.welcome_message()
print(x.staticmethod())
print(x.species())