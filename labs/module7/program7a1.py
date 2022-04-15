# Program 7A1
# Katie Devinney
# Creates art using a turtle

from turtle import Turtle

def main():
    snap = Turtle()
    # draw ground
    ground(snap)

    # make the house
    snap.up()
    snap.goto(-200, -200)
    snap.down()
    square(snap, 300)

    # give it a roof
    # # pen color?/fill?    
    snap.up()
    snap.setheading(90)
    snap.forward(300)
    snap.right(90)
    snap.down()
    triangle(snap, 300)
    
    # window 1
    snap.up()
    snap.goto(-150, 25)
    snap.down()
    square(snap, 50)

    # window 2
    snap.up()
    snap.goto(0, 25)
    snap.down()
    square(snap, 50)

    # sun
    # pen color/fill
    snap.up()
    snap.goto(200, 100)
    snap.down()
    drawSun(snap, 8, 50)

    # door
    # pen color/fill
    snap.up()
    snap.goto(-75, -200)
    snap.down()
    rectangle(snap, 100, 50)

def ground(t):
    t.up()
    t.goto(-400, -200)
    t.down()
    t.forward(700)

def square(t, length):
    for count in range(4):
        t.forward(length)
        t.left(90)

def triangle(t, length):
    for count in range(3):
        t.forward(length)
        t.left(120)

def drawSun(t, n, length):
    for count in range(n):
        triangle(t, length)
        t.left(360 / n)

def rectangle(t, length, width):
    t.setheading(0)
    t.forward(width)
    t.left(90)
    t.forward(length)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(length)

if __name__ == "__main__":
    main()