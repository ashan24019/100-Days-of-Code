# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('HirstSpotPainting.jpeg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle as t
from turtle import Screen
import random

t.colormode(255)
tim = t.Turtle()
color_list = [(235, 225, 207), (208, 157, 105), (215, 218, 228), (236, 214, 225), (141, 145, 160), (184, 70, 27), (227, 211, 115), (95, 105, 138), (191, 158, 26), (220, 234, 224), (202, 148, 175), (9, 18, 62), (97, 115, 175), (190, 17, 4), (13, 31, 14), (226, 169, 198), (29, 29, 10), (217, 81, 56), (235, 173, 159), (150, 164, 154), (32, 48, 119), (234, 208, 6), (129, 87, 97), (89, 104, 92), (180, 183, 220), (186, 11, 20), (200, 85, 104), (38, 19, 33), (76, 79, 33), (180, 201, 181)]

for i in range(10):
    tim.penup()
    tim.goto(-225, -250 + 50 * i)
    for j in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)

screen = Screen()
screen.exitonclick()