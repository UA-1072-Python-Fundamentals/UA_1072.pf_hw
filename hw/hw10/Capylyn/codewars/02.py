import random

class Ghost:

    def __init__(self):
        lst = ["white", "yellow", "purple", "red"]
        self.color = random.choice(lst)

