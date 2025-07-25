import os
os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'

from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
screen = Screen()

def move_forwards():
    timmy_the_turtle.forward(10)

def move_backwards():
    timmy_the_turtle.backward(10)

def turn_left():
    new_heading = timmy_the_turtle.heading() + 10
    timmy_the_turtle.setheading(new_heading)

def turn_right():
    new_heading = timmy_the_turtle.heading() - 10
    timmy_the_turtle.setheading(new_heading)

def clear():
    timmy_the_turtle.clear()
    timmy_the_turtle.penup()
    timmy_the_turtle.home()
    timmy_the_turtle.pendown()


screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
