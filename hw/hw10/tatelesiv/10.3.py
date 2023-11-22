# 10.3
class Employee:
    counter = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    @property
    def num_em(self):
        return f"Total number of employees is {Employee.counter}"

    def information(self):
        return f"{self.name} - {self.salary}$ per month"

    def __str__(self):
        return f"\n{self.num_em}\n{self.information()}"


employee1 = Employee("Alice Hart", 50000)
employee2 = Employee("Bob Bobovych", 60000)
print(employee1)
print(employee2)

print(Employee.__base__)
print(Employee.__dict__)
print(Employee.__module__)
print(Employee.__name__)
print(Employee.__doc__)
