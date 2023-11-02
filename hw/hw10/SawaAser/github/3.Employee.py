def print_count_employee():
    print('We have {} employee'.format(Employee.count_employee))


def information_all():
    for employee, salary in Employee.names.items():
        print("{} has {} salary".format(employee, salary))


class Employee:
    count_employee = 0
    names = {}

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count_employee += 1
        Employee.names[self.name] = self.salary

    def information(self):
        print("{} has {} salary".format(self.name, self.salary))


def info(x):
    print("Base Classes:", x.__base__)
    print("Class Namespace:", x.__dict__)
    print("Class Name:", x.__name__)
    print("Module Name:", x.__module__)
    print("Documentation bar:", x.__doc__)


Sawa = Employee("Sawa", 1000)
Aser = Employee("Aser", 2000)
somebody = Employee

print_count_employee()
information_all()
print('*'*50)
Sawa.information()
print('*'*50)
info(Employee)
