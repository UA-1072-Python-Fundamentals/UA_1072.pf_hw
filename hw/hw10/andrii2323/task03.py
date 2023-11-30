class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_employee_data(self):
        print(f"Employee Name: {self.name}")
        print(f"Employee Salary: ${self.salary}")

    @classmethod
    def display_total_employees(cls):
        print(f"Total Employees: {cls.total_employees}")


print("Base Classes:", Employee.__base__)
print("Class Namespace:", Employee.__dict__)
print("Class Name:", Employee.__name__)
print("Module Name:", Employee.__module__)
print("Documentation bar:", Employee.__doc__)

employee1 = Employee("Andrii", 11000)
employee2 = Employee("Olha", 15000)
employee3 = Employee("Pavlo", 9500)
employee4 = Employee("Mike", 11250)

employee1.display_employee_data()
employee2.display_employee_data()
employee3.display_employee_data()
employee4.display_employee_data()

Employee.display_total_employees()
