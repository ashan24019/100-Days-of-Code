import turtle as t
import random

is_race_on = False
screen = t.Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="witch tutle will win the race? Enter color: ")
colors = ("red", "orange", "yellow", "green", "blue", "purple")
all_turtles = []

if user_bet:
    is_race_on = True


for turtle_index in range(0, 6):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-200 + 75 * turtle_index)
    all_turtles.append(new_turtle)

while is_race_on:

    for turtle in all_turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You have won!. The {winning_color} turtle is the winner")
            else:
                print(f"You have lost!. The {winning_color} turtle is the winner")

        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)




screen.exitonclick()

