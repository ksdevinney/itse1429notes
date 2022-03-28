"""
Program 6A1
Katie Devinney
calculates the area of a shape after determining which formula to use
"""


import math

# calculate the area of a square
def square(length):
    area = length * length
    print("A square of side length %d will have an area of %d" % (length, area))
    return area

# calculate the area of a hexagon
def hexagon(length):
    square = length * length
    area = (3 * math.sqrt(3) * square) / 2
    print("A hexagon of side length %d will have an area of %d" % (length, area))
    return area

# calculate the area of an octagon
def octagon(length):
    square = length * length
    area = (1 + math.sqrt(2)) * (2 * square)
    print("An octagon of side length %d will have an area of %d" % (length, area))
    return area

def main():
    file = open("labs/module6/lab6A1.txt", 'r')

    shapes = []

    for line in file:
        shapes = line.split()

        sides = int(shapes[0])

        length = int(shapes[1])
        if sides == 4:
            square(length)
        elif sides == 6:
            hexagon(length)
        elif sides == 8:
            octagon(length)

if __name__ == "__main__":
    main()