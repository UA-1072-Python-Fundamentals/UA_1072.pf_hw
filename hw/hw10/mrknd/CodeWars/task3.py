class Human:
    def __init__(self, name):
        self.name = name

class Man(Human):
    def __init__(self, name):
        Human.__init__(self, name)


class Woman(Human):
    def __init__(self, name):
        Human.__init__(self, name)

def God():
    man = Man('Adam')
    women = Woman('Eve')
    return [man, women]
