class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return (f"{self.welc_m()}\n{self.species()}\n{self.arbitr_message()}")
    
    def welc_m(self):
        return(f"Hello {self.name}!")
    
    def species(self):
        return("The species is Homosapiens")
    
    @staticmethod
    def arbitr_message():
        return('This is a static method')

a = Human('Leo')
print(a)

