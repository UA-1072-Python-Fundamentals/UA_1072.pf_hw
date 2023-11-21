class Employee:
    count_emp = 0

    def __init__(self, name: str, salary: float):
        self.name = name
        self.salary = salary
        Employee.count_emp += 1

    @classmethod
    def total_number(cls):
        return f"The total number of employees is: {cls.count_emp}"

    def info(self):
        return f"Name: {self.name} | Salary: {self.salary}"


emp1 = Employee("Monkey", 1000)
print(emp1.info())
emp2 = Employee("Goose", 1200)
print(emp2.info())
emp3 = Employee("Donkey", 2300)
print(emp3.info())

print(Employee.total_number())

print(f"The Employee class is inherited from: {Employee.__base__}")
print(f"The class namespace: {Employee.__dict__}")
print(f"The class name: {Employee.__name__}")
print(f"The module name: {Employee.__module__}")
print(f"The documentation bar {Employee.__doc__}")
