import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
tim.width(10)
tim.speed("fastest")


def walk():
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.right(angle)
    tim.forward(30)


while True:
    angle = 90*random.randint(1, 4)
    walk()
