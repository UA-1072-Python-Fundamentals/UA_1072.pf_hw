class Employees:
    counter_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employees.counter_employees += 1

    def employee_info(self):
        return f"Employee: {self.name}\nSalary: {self.salary} $\n"

    @classmethod
    def total_employees(cls):
        return f"Total number of employees: {cls.counter_employees}"


employee1 = Employees("Tom", 65000)
employee2 = Employees("Miranda", 80000)

print(employee1.employee_info())
print(employee2.employee_info())

print(Employees.total_employees())
print()

print(Employees.__base__)
print(Employees.__name__)
print(Employees.__doc__)
print(Employees.__dict__)
print(Employees.__module__)


