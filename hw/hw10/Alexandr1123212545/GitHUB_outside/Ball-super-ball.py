class Ball(object):

    def __init__(self, ball_type = 'regular') -> None:
        self.ball_type = ball_type
        print(ball_type)



if __name__ == "__main__":
    ball1 = Ball()
    ball2 = Ball("super")
    ball1.ball_type         # "regular"
    ball2.ball_type         # "super"