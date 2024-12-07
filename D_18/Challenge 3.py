import random
import turtle as t

t.colormode(255)
arrow = t.Turtle()
num_sides = 3
arrow.width(3)

while True:
    for _ in range(num_sides):
        arrow.color(random.randint(0, 256), random.randint(0, 256), random.randint(0, 256))
        arrow.forward(100)
        arrow.right(360/num_sides)
    num_sides += 1

screen = t.Screen()
screen.exitonclick()
