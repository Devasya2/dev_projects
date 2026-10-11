import math
import random
import turtle

screen = turtle.Screen()
screen.setup(width=1500, height=1000)
screen.title("use arrow keys so the turtle can reach the beach")
screen.tracer(0)#I used this to depict a smooth flowing animation instead of painfully whatching the computer draw every frame.

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

t.penup()
t.goto(-750, 500)
t.pendown()
t.color("forestgreen")
t.begin_fill()
t.goto(750, 500)
t.goto(750, 200)
t.goto(-750, 200)#forming the upper rectangle(forest) from where the turtle starts
t.end_fill()

t.penup()
t.goto(-750, 200)
t.pendown()
t.color("wheat")
t.begin_fill()
t.goto(750, 200)
t.goto(750, -200)
t.goto(-750, -200)
t.end_fill()

texture = turtle.Turtle()
texture.hideturtle()
texture.speed(0)
for _ in range(600):
  x = random.randint(-740, 740)
  y = random.randint(-190, 190)
  texture.penup()
  texture.goto(x, y)
  texture.color("tan" if random.random() > 0.5 else "darkgoldenrod")
  texture.dot(random.randint(2, 5))

turtl = turtle.Turtle()
turtl.shape("turtle")
turtl.color("darkolivegreen")
turtl.shapesize(2.0)
turtl.penup()
turtl.goto(0, 320)  
turtl.setheading(270)  

def move_up():
  turtl.setheading(90)
  turtl.forward(20)


def move_down():
  turtl.setheading(270)
  turtl.forward(20)


def move_left():
  turtl.setheading(180)
  turtl.forward(20)


def move_right():
  turtl.setheading(0)
  turtl.forward(20)

#linking the above created function to theire respectice arrow keys
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

ocean = turtle.Turtle()
ocean.hideturtle()
ocean.speed(0)

step_count = 0#initialize

def waves():
  global step_count

  tide = -200 + int(25 * math.sin(step_count * 0.05))
  #200 start point for tide
  #25 amplitude
  #frequency 1 will be way too fast

  ocean.clear()

  ocean.penup()
  ocean.goto(-750, tide)
  ocean.pendown()
  ocean.color("deepskyblue")
  ocean.begin_fill()
  ocean.goto(750, tide)
  ocean.goto(750, -500)
  ocean.goto(-750, -500)
  ocean.end_fill()

  ocean.penup()
  ocean.goto(-750, tide)
  ocean.pendown()
  ocean.color("white")
  ocean.pensize(4)
  ocean.goto(750, tide)
  ocean.pensize(1)

  step_count = step_count + 1
  screen.update()

 
  screen.ontimer(waves, 30)

waves()

screen.mainloop()