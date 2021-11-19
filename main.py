import time
import turtle 
from paddle import Paddle 
from ball import Ball
from score import Score


wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(600, 400)
wn.title('Pong Game')
wn.tracer(0)



pad1 = Paddle(290, 0)
pad2 = Paddle(-290, 0)
score = Score()
ball = Ball()


wn.listen()
wn.onkey(pad2.up, 'w')
wn.onkey(pad2.down, 's')
wn.onkey(pad1.up, 'Up')
wn.onkey(pad1.down, 'Down')

game_is_on = True
score.up()

while game_is_on:
  ball.moving()
  time.sleep(ball.pace)
  wn.update()
  if ball.ycor() > 190 or ball.ycor() < -190:
    ball.bounce()
  elif ball.xcor() > 280 and ball.distance(pad1) < 50 or ball.xcor() < -280 and ball.distance(pad2) < 50:
    ball.collide()
  elif ball.xcor() > 280:
      score.score1 += 1
      score.up()
      ball.reset()
  elif ball.xcor() < -280:
      score.score2 += 1
      score.up()
      ball.reset()
      









