class Employee():
    """This is Employee class which can return info about headcount and about each employee"""
    qty_employee=0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.qty_employee+=1

    def info_total_employee():
        print(Employee.qty_employee)

    def info_employee(self):
        print(f"name: {self.name}, salary: {self.salary}")


em1=Employee("Paul",1000)
em2=Employee("Peter",1500)
Employee.info_total_employee()
em1.info_employee()
em2.info_employee()

print("Base classes of Employee class:",Employee.__base__)
print("The class namespace:", list(Employee.__dict__.keys()))
print("The class name:",Employee.__name__)
print("The module name in which the class is defined:", Employee.__module__)
print("Docs:",Employee.__doc__)