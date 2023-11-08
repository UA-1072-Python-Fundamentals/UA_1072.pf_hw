from random import choice
class Ghost(object):
    color = 'Unknown'

    def __init__(self) -> None:
        self.__class__.color = choice(["white", "yellow", "purple", "red"])
        

if __name__ == "__main__":
    ghost = Ghost()
    print(ghost.color)
    ghost = Ghost()
    print(ghost.color)
    ghost = Ghost()
    print(ghost.color)
