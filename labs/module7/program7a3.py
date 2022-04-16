# Program 7A3
# Katie Devinney
# turtle draws a pattern

from turtle import Turtle

def main():
    startX = 0
    startY = 0

    skippy = Turtle()

    # position the turtle and make a row
    skippy.goto(startX, startY)
    line(skippy)
    # adjust where the next row will start 
    startX -= 50
    startY += 50

    # position the turtle and make a row
    skippy.goto(startX, startY)
    line(skippy)
    startX -= 50
    startY += 50

    # position the turtle and make a row
    skippy.goto(startX, startY)
    line(skippy)
    startX -= 50
    startY += 50

    # position the turtle and make a row
    skippy.goto(startX, startY)
    line(skippy)
    startX -= 50
    startY += 50


def line(t):

    t.up()

    # loop to draw 4 dots in each row
    for dot in range(4):
        t.dot(20)
        t.setheading(0)
        t.forward(50)
        t.setheading(90)
        t.forward(50)


if __name__ == "__main__":
    main()