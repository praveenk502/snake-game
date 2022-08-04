from turtle import Turtle

STARTING_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180

class Snake:

    def __init__(self):
        self.all_segment=[]
        self.create_snake()
        self.head=self.all_segment[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self,position):
        t1 = Turtle("square")
        t1.color("white")
        t1.penup()
        t1.goto(position)
        self.all_segment.append(t1)

    def extend(self):
        self.add_segment(self.all_segment[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move(self):

        for seg in range(len(self.all_segment)-1,0,-1):
            x=self.all_segment[seg-1].xcor()
            y = self.all_segment[seg - 1].ycor()
            self.all_segment[seg].goto(x,y)
        self.head.forward(MOVE_DISTANCE)
