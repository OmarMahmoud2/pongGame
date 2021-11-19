from turtle import Turtle 

class Score(Turtle):
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.pencolor('white')
    self.penup()
    self.goto(0, 180)
    self.score1 = 0 
    self.score2 = 0 
  
  def up(self):
    self.clear()
    self.write(f"Score: {self.score1}   Vs   Score: {self.score2}", align = 'center', font = ('Ariel', 16, 'normal'))
    