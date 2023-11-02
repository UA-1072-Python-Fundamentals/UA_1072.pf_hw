## 1- Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
## If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

## 2- Color Ghost
import random
class Ghost:
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])

## 3-Basic subclasses - Adam and Eve
class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        super().__init__(name)

class Woman(Human):
    def __init__(self, name):
        super().__init__(name)

def God():
    adam = Man("Adam")
    eve = Woman("Eve")
    return [adam, eve]

# Example usage:
humans = God()
for human in humans:
    print(f"{human.name} is a {type(human).__name__}")
