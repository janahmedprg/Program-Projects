import turtle
import time

wn = turtle.Screen()
wn.bgcolor('white')
wn.tracer(0)

snake_head = turtle.Turtle()
snake_head.shape("triangle")
snake_head.shapesize(stretch_wid=2, stretch_len=2, outline=None)
snake_head.color("green")
snake_head.penup()


speed = 5

def travel():
    snake_head.forward(speed)

def up():
    snake_head.setheading(90)

def down():bafs
    snake_head.setheading(270)

def left():
    snake_head.setheading(180)

def right():
    snake_head.setheading(0)

wn.onkey(up, 'Up')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')
wn.onkey(down, 'Down')

wn.listen()

while True:
    wn.update()
    travel()
    time.sleep(0.01)

wn.mainloop()
