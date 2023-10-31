class Employee:
    """ Class Employee"""
    total = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total += 1

    @classmethod
    def totalEmployees(cls):
        print(f"Total employees = {cls.total}")

    def employeeInformation(self):
        print(f"Employee {self.name}, salary {self.salary}")


e1 = Employee("Yurii", 2500)
e1.employeeInformation()
Employee.totalEmployees()
e2 = Employee("Sergey", 3500)
e2.employeeInformation()
Employee.totalEmployees()

print(f"The employee class is inherited from {Employee.__base__}")
print(f"The class namespace -  {list(Employee.__dict__.keys())}")
print(f"The class name -  {Employee.__name__}")
print(f"The module name in which the class is defined - {Employee.__module__}")
print(f"The documentation bar -  {Employee.__doc__}")
