import random
class Ghost:
    color_list = ["white", "yellow", "purple", "red"]
    def __init__(self,color=random.choice(color_list)):
        self.color=color

ghost=Ghost()
print(ghost.color)