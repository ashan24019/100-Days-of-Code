from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape("square")
paddle.shapesize(stretch_wid=5, stretch_len=10)
paddle.color("white")
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


screen.listen()
screen.onkey(go_up, "up")
screen.onkey(go_down, "down")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()