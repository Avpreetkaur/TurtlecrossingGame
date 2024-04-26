from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 280
# Create a turtle player that starts at the bottom of the screen and
# listen for the "Up" keypress to move the turtle north. If you get stuck,
# check the video walkthrough in Step 3.

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("cyan")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def move(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



