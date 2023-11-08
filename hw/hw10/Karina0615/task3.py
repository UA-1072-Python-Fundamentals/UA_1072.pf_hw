class Employee:
    '''
    This is a new class
    '''
    counter = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.counter += 1

    def __str__(self):
        return(f"{self.count_employee()}\n{self.info_emp()}")
                  
    def count_employee(self):
        return(f"Total number of employee: {Employee.counter}")
    
    def info_emp(self):
        return(f"{self.name} has {self.salary}$ per month")
    
a = Employee("Jon Piterson", 1000)
b = Employee('Lily Note', 4000)
print(a, b)

print(Employee.__base__) 
print(Employee.__dict__)
print(Employee.__module__) 
print(Employee.__name__) 
print(Employee.__doc__)  
    