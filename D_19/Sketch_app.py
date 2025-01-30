import turtle as t
screen = t.Screen()
tim = t.Turtle()
tim.color("purple")
tim.width(3)


def forward():
    tim.forward(15)


def backward():
    tim.backward(15)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


t.onkey(forward, "w")
t.onkey(backward, "s")
t.onkey(clockwise, "Right")
t.onkey(counter_clockwise, "Left")
t.onkey(clear, "c")


t.listen()
screen.exitonclick()