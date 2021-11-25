from turtle import Turtle, Screen

wn = Screen()
wn.bgcolor('lightblue')

snake_head = Turtle()
snake_head.shape("triangle")
snake_head.shapesize(stretch_wid=2, stretch_len=2, outline=None)
snake_head.color("green")
snake_head.penup()

snake_eyes1 = Turtle()
snake_eyes1.shape("circle")
snake_eyes1.shapesize(stretch_wid=0.25, stretch_len=0.25, outline=None)
snake_eyes1.color("red")
snake_eyes1.penup()
snake_eyes1.goto(0, 10)

snake_eyes2 = Turtle()
snake_eyes2.speed(0)
snake_eyes2.shape("circle")
snake_eyes2.shapesize(stretch_wid=0.25, stretch_len=0.25, outline=None)
snake_eyes2.color("red")
snake_eyes2.penup()
snake_eyes2.goto(0, -10)

snake_tongue = Turtle()
snake_tongue.speed(0)
snake_tongue.shape("circle")
snake_tongue.shapesize(stretch_wid=0.25, stretch_len=0.50, outline=None)
snake_tongue.color("red")
snake_tongue.penup()
snake_tongue.goto(20, 0)




speed = 1

def travel():
    snake_head.forward(speed)
    snake_eyes1.forward(speed)
    snake_eyes2.forward(speed)
    snake_tongue.forward(speed)
    wn.ontimer(travel, 10)

wn.onkey(lambda: snake_head.setheading(90), 'Up')
wn.onkey(lambda: snake_head.setheading(180), 'Left')
wn.onkey(lambda: snake_head.setheading(0), 'Right')
wn.onkey(lambda: snake_head.setheading(270), 'Down')

wn.listen()

travel()

wn.mainloop()
