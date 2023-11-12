class Employee:
    """
    The class Employee is responsible for creating and processing employees.
    """
    NAME = None
    SALARY = None
    STAFF = 0
    
    def __init__(self) -> None:
        self.__class__.STAFF += 1               # addition to the staff with each new initialization.


    def get_info(self) -> str:
        """
        This method return personal information about the employee
        """

        return f"Employee - {self.NAME}\nSalary - {self.SALARY}.00$\n_ _ _ _ _ __"
    

    def get_staff(self) -> str:
        """
        This method return number of all employees.
        Only employee whose NAME  "BOSS" has access!
        """

        if self.NAME == 'BOSS':
            return f"Currently there are {self.STAFF} employees"
        else:
            return "NO ACCESS"



if __name__ == "__main__":
    # emp_0 = Employee()
    # emp_1 = Employee()
    # emp_2 = Employee()
    # emp_3 = Employee()
    # emp_4 = Employee()
    # emp_5 = Employee()
    # emp_0.NAME = 'BOSS'
    # emp_0.SALARY = 1
    # emp_1.NAME = 'Aleksa'
    # emp_1.SALARY = 900
    # emp_2.NAME = 'Ostap'
    # emp_2.SALARY = 1500
    # emp_3.NAME = 'Bogdan'
    # emp_3.SALARY = 1200
    # emp_4.NAME = 'Antonio'
    # emp_4.SALARY = 1800
    # emp_5.NAME = 'Varvara'
    # emp_5.SALARY = 2100
    # print(emp_1.get_info())
    # print(emp_2.get_info())
    # print(emp_3.get_info())
    # print(emp_4.get_info())
    # print(emp_5.get_info())
    # print(emp_0.get_staff())
    # print(emp_1.get_staff())

    print(Employee.__doc__)
    print(f"Class name - {Employee.__name__}\n_ _ _ _ _ _ _ _")
    print(f"Module name - {Employee.__module__}\n_ _ _ _ _ _ _ _")
    print(f"\nParent class - {Employee.__base__}\n_ _ _ _ _ _ _ _")
    # print('Class namespace :\n', *Employee.__dict__, sep='\n')
    print(f"Class namespace : {[*Employee.__dict__]}")
