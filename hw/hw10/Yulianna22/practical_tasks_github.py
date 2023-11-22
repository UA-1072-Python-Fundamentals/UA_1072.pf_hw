#Task1
class Polygon:
    def __init__(self, sides):
        self.sides = sides

    def get_area(self):
        pass  

class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__(4)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

rectangle = Rectangle(10, 15)
print("Area of the rectangle:", rectangle.get_area())

#Task2
class Human:
    def __init__(self,name):
        self.name=name
    
    def welcome_message(self):
        return f'Hello {self.name}. Welcome to the Earth!'
    
    @classmethod
    def species(cls):
        return 'We are Homosapiens'
    
    @staticmethod
    def arbituary_message():
        return 'You are cool!'
    
user_1=Human('Katty')
user_2=Human('John')
user_3=Human('Ann')
print(f'{user_1.welcome_message()}\n{user_2.welcome_message()}\n{user_3.welcome_message()}')
print(Human.species())
print(Human.arbituary_message())

#Task3
class Employee:
   
    employee_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1

    def display_employee_info(self):
        print(f'Name: {self.name}, Salary: {self.salary}$')

    @classmethod
    def display_total_employees(cls):
        print(f'Total number of employees: {cls.employee_count}')


employee1 = Employee('Nastia', 1500)
employee2 = Employee('Natali', 600)
employee3 = Employee('Alex', 3500)
employee4 = Employee('Andrew', 2000)


employee1.display_employee_info()
employee2.display_employee_info()
employee3.display_employee_info()
employee4.display_employee_info()


Employee.display_total_employees()


print("Base classes:", Employee.__base__)
print("Class namespace:", Employee.__dict__)
print("Class name:", Employee.__name__)
print("Module name:", Employee.__module__)
print("Documentation:", Employee.__doc__)
    


