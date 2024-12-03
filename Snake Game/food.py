from turtle import Turtle
import random


class Food(Turtle):
    
    def __int__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch.len=10.5, strtch.wid=0.5)
        self.color("blue")
        self.speed("faster")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto()