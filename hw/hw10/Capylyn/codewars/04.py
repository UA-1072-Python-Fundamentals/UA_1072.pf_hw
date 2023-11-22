class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def info(self):
        return (f"{self.name}s age is {self.age}")


x = Person('John', 15)

print(x.info)


# OR

class Person:
    def __init__(self, name, age):
        self.info = f"{name}s age is {age}"


x = Person("John", 15)
print(x.info)