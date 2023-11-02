from math import pi as PI

class Sphere(object):
    """
    Class for calculating sphere parameters.
    """


    def __init__(self, radius: int | float, mass: int | float) -> int | float:
        self.radius = radius
        self.mass = mass
    

    def get_radius(self):
        return self.radius


    def get_mass(self):
        return self.mass
    
    
    def get_volume(self):
        return round((4 / 3) * PI * self.radius**3, 5)
    
    
    def get_surface_area(self):
        return round(4 * PI * self.radius**2, 5)
    
    
    def get_density(self):
        try:
            return round(self.mass / self.get_volume(), 5)
        except ZeroDivisionError:
            return 0

if __name__ == "__main__":
    ball = Sphere(2, 50)
    print(ball.get_radius())            # 2,        margin=1e-5, message="Check radius")
    print(ball.get_mass())              # 50,       margin=1e-5, message="Check mass")
    print(ball.get_volume())            # 33.51032, margin=1e-5, message="Check volume")
    print(ball.get_surface_area())      # 50.26548, margin=1e-5, message="Check area")
    print(ball.get_density())           # 1.49208,  margin=1e-5, message="Check density")