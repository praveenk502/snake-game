from turtle import Turtle, Screen

t1 = Turtle()
s1 = Screen()

class Score:
    def __init__(self):
        self.score = 0
        t1.penup()
        t1.hideturtle()
        t1.goto(-10, 270)
        t1.color("white")
        t1.write(f"score: {self.score}", True, "center", font=("Arial", 15, "normal"))

    def over(self):
        t1.goto(0,0)
        t1.write("GAME OVER !", True, "center", font=("Arial", 15, "normal"))

    def update_score(self):
        self.score += 1
        t1.clear()
        t1.goto(-10, 270)
        t1.write(f"score: {self.score}", True, "center", font=("Arial", 15, "normal"))


