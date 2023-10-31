class Ball:
    def __init__(self, ball_type="regular"):
        self.ball_type = ball_type

regular_ball = Ball()
super_ball = Ball("super")

print(regular_ball.ball_type)
print(super_ball.ball_type)    