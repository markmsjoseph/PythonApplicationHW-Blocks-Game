#Mark Joseph (mmj301)
import math
import random
import turtle

def monte_pi(darts):

    t = turtle.Turtle()
    wn = turtle.Screen()

    # set the dimensions of the window
    wn.setup(500, 500)

    # constrain the coordinate system so that it represents a 1 x 1 plane
    wn.setworldcoordinates(0, 0, 1, 1)

    # turn animation off
    wn.tracer(0)

    t.up()

    # 1. create a variable to keep track of how many points fall within the
    #    quarter circle

    inCircle = 0
    for i in range(darts):

        x = random.random()
        y = random.random()
        d = math.sqrt(x**2 + y**2)

        t.goto(x,y)
        if d <= 1:
            inCircle = inCircle + 1
            t.color("blue")
        else :
            t.color("red")

        t.dot()

        pi = inCircle/darts*4

        print(pi)



    # 2. generate points (the parameter, called darts, represents the number
    #    of points to be generated)
    #    a. determine which ones fall within the quarter circle
    #    b. plot the points using a turtle function called dot
    #    c. use the turtle function color, to color the points within the
    #       the circle blue... and outside of the color red:
    #       t.color('blue')
    #       t.dot()


    # 3. use the formula in the book for calculating an approximation for pi

    # only close the window when it is clicked
    wn.exitonclick()

monte_pi(2000)
