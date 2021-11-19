from turtle import Turtle
import random

class Ball(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.penup()
    self.pace = 0.1
    self.color('white')
    self.xmove = random.randint(5,16)
    self.ymove = random.randint(5,15)
    
    
  def moving(self):
    self.goto(self.xcor() + self.xmove, self.ycor() + self.ymove)
  
  def bounce(self):
    self.ymove *= -1
  
  def collide(self):
    self.xmove *= -1
    self.pace *= 0.9
    
  def reset(self):
    self.home()
    self.xmove *= -1
    self.pace = 0.1
  
