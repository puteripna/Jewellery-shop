"""
Program   : LxGraphics.py
Author    : Nur Izzaty binti Yaacob
Date      : 27 April 2024

Displays a welcome loading screen with visuals after logging in.
"""


import turtle
import time

wn = turtle.Screen()
wn.title("WELCOME!")
wn.bgcolor("#f5ece5")
wn.setup(width=1.0, height=1.0)  # Maximise screen size

pen = turtle.Turtle()
pen.pensize(2)
pen.hideturtle()
pen.speed(0)


# FUNCTION TO DRAW LETTER L
def L():
    def body():
        pen.up()
        pen.goto(-95, -190)
        pen.down()

        pen.pencolor("#45523e")
        pen.fillcolor("#45523e")
        pen.begin_fill()
        for i in range(2):
            pen.forward(95)
            pen.left(90)
            pen.forward(150 * 2 + 40)
            pen.left(90)
        pen.end_fill()

    def corners():
        # bottom left
        pen.pencolor("#45523e")
        pen.fillcolor("#45523e")
        pen.begin_fill()
        pen.seth(90)
        pen.forward(35)
        pen.circle(35, -90)
        pen.seth(0)
        pen.forward(35)
        pen.end_fill()

        # bottom right
        pen.up()
        pen.goto(0, -190)
        pen.down()
        pen.fillcolor("#45523e")
        pen.begin_fill()
        pen.seth(90)
        pen.forward(35)
        pen.seth(270)
        pen.circle(35, 90)
        pen.seth(180)
        pen.forward(35)
        pen.end_fill()

        # upper left
        pen.up()
        pen.goto(-95, 150)
        pen.down()
        pen.fillcolor("#45523e")
        pen.begin_fill()
        pen.seth(270)
        pen.forward(35)
        pen.seth(90)
        pen.circle(35, 90)
        pen.seth(0)
        pen.forward(35)
        pen.end_fill()

        # upper right
        pen.up()
        pen.goto(0, 150)
        pen.down()
        pen.fillcolor("#45523e")
        pen.begin_fill()
        pen.seth(270)
        pen.forward(35)
        pen.seth(270)
        pen.circle(35, -90)
        pen.seth(180)
        pen.forward(35)
        pen.end_fill()

        pen.up()
        pen.goto(180, -190)
        pen.down()
        pen.fillcolor("#45523e")
        pen.begin_fill()
        pen.seth(90)
        pen.forward(120)
        pen.circle(120, -90)
        pen.seth(0)
        pen.forward(120)
        pen.end_fill()

    body()
    corners()


# FUNCTION TO DRAW LETTER X
def X():
    pen.pencolor("#EBA428")
    pen.up()
    pen.goto(20, -55)
    pen.down()

    # BODY OF X
    pen.fillcolor("#EBA428")
    pen.begin_fill()
    pen.seth(270)
    pen.circle(7, -78)
    pen.seth(18.8)
    pen.forward(158)
    pen.seth(0)
    pen.circle(7, 85)
    pen.seth(90)
    pen.forward(48)
    pen.circle(7, -85)
    pen.seth(180 + 18.8)
    pen.forward(158)
    pen.seth(180)
    pen.circle(7, 78)
    pen.seth(270)
    pen.forward(48)
    pen.end_fill()

    # CORNERS OF X
    pen.up()
    pen.goto(180, -50)
    pen.down()

    pen.fillcolor("#EBA428")
    pen.begin_fill()
    pen.seth(90)
    pen.forward(35)
    pen.circle(20, -160)
    pen.seth(-37)
    pen.forward(48)
    pen.end_fill()

    pen.up()
    pen.goto(20, 55)
    pen.down()

    pen.fillcolor("#EBA428")
    pen.begin_fill()
    pen.seth(270)
    pen.forward(35)
    pen.seth(270)
    pen.circle(20, -160)
    pen.seth(180 - 37)
    pen.forward(48)
    pen.end_fill()


# FUNCTION TO DRAW HOOK SHAPE
def hook():
    pen.speed(0)
    pen.pencolor("#45523e")
    pen.up()
    pen.goto(100, 70)
    pen.down()

    # Circles
    pen.fillcolor("#45523e")
    pen.begin_fill()
    pen.seth(0)
    pen.circle(10, 180)
    pen.seth(0)
    pen.circle(13, 360)
    pen.seth(180)
    pen.circle(10, 180)
    pen.end_fill()

    # Hook
    pen.pensize(5)
    pen.left(90)
    pen.forward(55)
    pen.left(-90)
    pen.circle(10, 270)


# FUNCTION TO DRAW STAR
def star(x, y, r, linecolor, fcolor):
    heading = 270
    pen.pensize(3)
    pen.speed(0)

    pen.up()
    pen.goto(x, y)
    pen.down()

    pen.seth(0)
    pen.pencolor(linecolor)
    pen.fillcolor(fcolor)
    pen.begin_fill()
    for i in range(4):
        pen.circle(r, 90)
        pen.setheading(heading)
        heading -= 90
    pen.end_fill()


def draw_star():
    time.sleep(0.2)

    star(-650, -20, 100, "#45523e", "#45523e")

    time.sleep(0.5)

    star(-420, -20, 75, "#45523e", "white")

    time.sleep(0.4)

    star(-240, -20, 50, "#45523e", "#45523e")

    time.sleep(0.3)

    star(230, -20, 40, "#45523e", "white")

    time.sleep(0.2)

    star(350, -20, 30, "#45523e", "#45523e")

    time.sleep(0.2)

    star(450, -20, 20, "#45523e", "white")

    time.sleep(0.1)

    star(530, -20, 10, "#45523e", "#45523e")


# FUNCTION TO WRITE TEXTS
def texts():
    pen.up()
    pen.goto(-160, 220)
    pen.down()
    font1 = ("Times", 50, "bold")
    pen.write("WELCOME TO", font=font1)

    pen.up()
    pen.goto(-210, -310)
    pen.down()
    font2 = ("Times", 50, "bold")
    pen.write("BYLUXE JEWELRY", font=font2)


def mainn():
    L()
    X()
    hook()
    draw_star()
    texts()
    time.sleep(2)
    wn.bye()  # Shut graphics window

mainn()
