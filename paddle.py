from turtle import Turtle 

class Paddle(Turtle):
  def __init__(self, x, y):
    super().__init__()
    self.color('white')
    self.shape('square')
    self.shapesize(5, 1)
    self.penup()
    self.goto(x, y)
    

  def up(self):
    if self.ycor() >= 200:
      pass
    else:
      yu = self.ycor() + 20
      self.goto(self.xcor(), yu)
    

  
    
  def down(self):
    if self.ycor() <= -200:
      pass
    else:
      uy = self.ycor() - 20
      self.goto(self.xcor(), uy)
    