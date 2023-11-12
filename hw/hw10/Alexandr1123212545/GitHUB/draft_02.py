class Human:

    SPECIES = 'We are Homosapiens'

    def __init__(self) -> None:
        pass
        

    def greetings(self, name='User') -> str:
        """
        This method greets every user
        """

        self.name = name
        return f"Hello {name}! Welcome to my world!"


    @classmethod
    def species (cls):
        """
        This method says who we are.
        """
        return cls.SPECIES
    

    @staticmethod
    def some_text():
        """
        This method displays some text.
        """
        
        return 'With the lights out we are dangerous!'


if __name__ == "__main__":
    user_1 = Human()
    user_2 = Human()
    print(user_1.greetings())
    print(user_1.greetings())
    print(user_1.greetings('Ivan'))
    print(user_1.greetings('Varvara'))
    print(Human.species())
    print(user_1.some_text())

