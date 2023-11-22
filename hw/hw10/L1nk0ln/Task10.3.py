class Employee:
    """
For outputting information about employees and outputting count of them
    """
    a = 0
    def __init__(self, name, salary = 500):

        self.name = name
        self.salary = salary
        Employee.a += 1
    def ecounter():
        return Employee.a
    def __str__(self):
        return (f"Name:{self.name} , Salary: {self.salary}")

n = 3
while n > 0:
    imia = input("Enter the name of employee: ")
    zarplatnya = input("Enter the salary of employee: ")
    test = Employee(imia, int(zarplatnya))
    print(f"{test}, \n Count of employees: {Employee.ecounter()}")
    n -= 1


print(Employee.__base__)
print(test.__dict__)
print(Employee.__name__)
print(test.__module__)
print(test.__doc__)

