class Polygon:

    def __init__(self) -> None:
        pass

class Rectangle(Polygon):
    """
    This class for manipulating a rectangle.
    """

    def __init__(self, side_1=0, side_2=0) -> None:
        super().__init__()
        self.side_1 = side_1
        self.side_2 = side_2
    
    def square(self):
        """
        This method returns area of the rectangle.
        """
        
        return self.side_1 * self.side_2
    

if __name__ == "__main__":
    rec_1 = Rectangle()
    rec_2 = Rectangle()
    rec_3 = Rectangle()
    rec_1.side_1 = 2
    rec_1.side_2 = 4
    print(rec_1.square())
    rec_2.side_1 = 3
    rec_2.side_2 = 7.2
    print(rec_2.square())
    rec_1.side_1 = 0.15
    rec_1.side_2 = 12.654
    print(rec_3.square())