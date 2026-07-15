from turtle import Turtle,Screen
import random


t1 = Turtle(shape = "turtle")   
t2 = Turtle(shape="turtle")
t3 = Turtle(shape="turtle")
t4 = Turtle(shape="turtle")
t5 = Turtle(shape = "turtle")
t6 = Turtle(shape = "turtle")

screen = Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="make your bet",prompt="which turtle will win the race?Enter a color:")
colors = ["red","orange","yellow","green","blue","purple"]
is_race_on = False
all_turtles = [t1,t2,t3,t4,t5,t6]

print(user_bet)

if user_bet:
    is_race_on= True




# for t1
t1.fillcolor("yellow")
t1.penup()
t1.goto(x=-230,y=-100)

# for t2
t2.fillcolor("red")
t2.penup()
t2.goto(x=-230,y=-60)

t3.fillcolor("orange")
t3.penup()
t3.goto(x=-230,y=-20)

t4.fillcolor("green")
t4.penup()
t4.goto(x=-230,y=20)

t5.fillcolor("blue")
t5.penup()
t5.goto(x=-230,y=60)

t6.fillcolor("purple")
t6.penup()
t6.goto(x=-230,y=100)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on=False
            winning_color = turtle.fillcolor()
            if winning_color == user_bet:
                print(f"You have won the {winning_color} turtle is winner..!")
            else:
                print(f"You have lost the {winning_color} turtle is winner..!")

        random_distance=random.randint(0,10)
        turtle.forward(random_distance)
























screen.exitonclick()