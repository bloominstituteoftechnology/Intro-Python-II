import turtle
import random
myPen = turtle.Turtle()
myPen.shape("turtle")
myPen.speed(10)

window = turtle.Screen()
window.bgcolor("#00B2C0")


def corner(turtle):
    for x in range(0, 6):
        turtle.left(15)
        turtle.forward(2)


def cornered_box(turtle, x1, y1, x2, y2, letter):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.color("black")
    turtle.fillcolor("black")
    turtle.begin_fill()
    for x in range(0, 4):
        turtle.forward(40)
        corner(turtle)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x2, y2)
    turtle.color("white")
    turtle.write(letter, None, None, "28pt bold")


cornered_box(myPen, -40, 20, -35, 35, "C")
cornered_box(myPen, 25, 20, 30, 35, "O")
cornered_box(myPen, -40, -45, -35, -30, "D")
cornered_box(myPen, 25, -45, 30, -30, "E")

myPen.color("white")
myPen.goto(-115, -92)
myPen.write("Anyone Can Learn", None, None, "24pt bold")
myPen.goto(-115, -127)
myPen.write("Anyone Can Teach", None, None, "24pt bold")
myPen.left(90)


myPen.goto(10, 105)

for x in range(0, 100):
    myPen.color("#%06x" % random.randint(0, 2**24 - 1))
myPen.color("white")
