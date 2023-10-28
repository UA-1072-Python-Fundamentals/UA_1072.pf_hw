class Person:
    """
    Class to initialize.
    """
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def info(self):
        return f"{self.name}s age is {self.age}"
    


if __name__ == "__main__":
    person = Person('Proton', 214)
    print(person.info)
