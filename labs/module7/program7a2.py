# Katie Devinney
# Program 7A2
# Puts the turtle to work setting pins at the bowling alley

from turtle import Turtle

def main():
    buster = Turtle()

    setPins(buster, 4)

    # get out of the way!
    buster.up()
    buster.goto(300, 300)

# draw the dots
def setPins(t, row):
    startX = 0
    startY = 0
    indent = 0

    # iterate over each row
    while row > 0:
        # set pins in the row
        for pin in range(row):
            t.dot(20)
            t.up()
            t.forward(50)
        
        # each row is shorter than the last
        row -= 1
       
        # each row gets closer to the middle
        indent += 1
        t.up()
        
        # move to the next row
        t.goto(startX + 25 * indent , startY - indent * 50)

if __name__ == "__main__":
    main()