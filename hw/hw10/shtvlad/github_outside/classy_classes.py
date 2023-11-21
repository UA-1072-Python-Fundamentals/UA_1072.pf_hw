class Person():
    def __init__(self,name,age):
        self.name=str(name)
        self.age=int(age)
    @property
    def get_info(self):
        print(f"{self.name}'s age is {self.age}")

p1=Person("Peter","35")
p1.get_info
