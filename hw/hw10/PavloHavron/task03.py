class Employee:
    "Class Employee"

    counter = 0

    def __init__(self,name, salary,):
        self.name = name
        self.salary = salary
        Employee.counter+=1   

    def __str__(self):
        return(f"The salary of {self.name} is {self.salary}")  
      
    def count_employee(self):
        return(f"Number of employee: {Employee.counter}")
    
    def info_employee(self):
        return(f"{self.name} get {self.salary}$ per month")

firstE = Employee("Genadiy Bubkin", 1000)
secondE = Employee('Dariya Spesiva', 500)
print(firstE, secondE)

print(Employee.__base__) 
print(Employee.__dict__)
print(Employee.__module__) 
print(Employee.__name__) 
print(Employee.__doc__)  
    