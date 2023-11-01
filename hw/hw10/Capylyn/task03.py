class Work():
    pass
class Employee(Work):
    """
Information about employees
    """
    count = 0
    def __init__(self, name = "Capy", salary = 500):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def __str__(self):
        return(f"The salary of {self.name} is {self.salary}")

    def total_count():
        return (f"The total number of employees is {Employee.count}")

ins01 = Employee("Yevhen", 800)
print(f"{ins01}, \n{Employee.total_count()}")
ins02 = Employee("Anna", 800)
print(f"{ins02}, \n{Employee.total_count()}")

print(Employee.__base__)
print(ins01.__dict__)
print(Employee.__name__)
print(ins01.__module__)
print(ins01.__doc__)
