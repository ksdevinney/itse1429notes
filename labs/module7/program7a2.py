# Katie Devinney
# Program 7A2
# Puts the turtle to work setting pins at the bowling alley

from turtle import Turtle

def main():
    buster = Turtle()

    row = 4
    indent = 0

    startX = 0
    startY = 0

    while row > 0:
        for pin in range(row):
            buster.dot(20)
            buster.up()
            buster.forward(50)
        row -= 1
        indent += 1
        buster.up()
        buster.goto(startX + 25 * indent , startY - indent * 50)

    


if __name__ == "__main__":
    main()