from turtle import Turtle, Screen
MOVE_DISTANCE = 10
TURN_ANGLE = 10

timmy_the_turtle = Turtle()
timmy_the_turtle.speed("fastest")
screen = Screen()
screen.title("Etch-a-Sketch Simulator")

def move_forwards():
    # timmy_the_turtle.forward(10)
    timmy_the_turtle.forward(MOVE_DISTANCE)

def move_backwards():
    # timmy_the_turtle.backward(10)
    timmy_the_turtle.backward(MOVE_DISTANCE)

def turn_left():
    # new_heading = timmy_the_turtle.heading() + 10
    new_heading = timmy_the_turtle.heading() + TURN_ANGLE
    timmy_the_turtle.setheading(new_heading)

def turn_right():
    # new_heading = timmy_the_turtle.heading() - 10
    new_heading = timmy_the_turtle.heading() - TURN_ANGLE
    timmy_the_turtle.setheading(new_heading)

def clear():
    timmy_the_turtle.clear()
    timmy_the_turtle.penup()
    timmy_the_turtle.home()
    timmy_the_turtle.pendown()


# Keyboard Controls
# W -> Forward
# S -> Backward
# A -> Turn Left
# D -> Turn Right
# C -> Clear Canvas

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

screen.exitonclick()
