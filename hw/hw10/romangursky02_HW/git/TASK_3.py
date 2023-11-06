class Employee:
    total_employees = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.total_employees += 1

    def display_info(self):
        return f"Name: {self.name}, Salary: {self.salary}"

    @classmethod
    def display_total_employees(cls):
        return f"Total Employees: {cls.total_employees}"

# Example usage:
employee1 = Employee("Alice", 50000)
employee2 = Employee("Bob", 60000)

print(employee1.display_info())
print(employee2.display_info())
print(Employee.display_total_employees())
