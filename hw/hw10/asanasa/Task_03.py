class Employee:
    total_employees = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: ${self.salary}")

    @classmethod
    def total_employee_count(cls):
        print(f"Total Number of Employees: {cls.total_employees}")



employee1 = Employee("John", 50000)
employee2 = Employee("Alice", 60000)


employee1.display_info()
employee2.display_info()


Employee.total_employee_count()


print(f"Base classes: {Employee.__base__}")  
print(f"Class namespace: {Employee.__dict__}")
print(f"Class name: {Employee.__name__}")
print(f"Module name: {Employee.__module__}")
print(f"Documentation string: {Employee.__doc__}")