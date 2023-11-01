class Ball(object):
    def __init__(self, t="regular"):
        self.ball_type = t


print(Ball().ball_type)
print(Ball('super').ball_type)
