# Program 6A1
# Katie Deviney
# 

import math

# calculate the area of a square
def square(length):
    area = length * length
    return area

# calculate the area of a hexagon
def hexagon(length):
    square = length * length
    area = (3 * math.sqrt(3) * square) / 2
    return area

# calculate the area of an octagon
def octagon(length):
    square = length * length
    area = (1 + math.sqrt(2)) * (2 * square)
    return area

def main():
    file = open("labs/module6/lab6A1.txt", 'r')

    shapes = []

    for line in file:
        shapes[line] = int(line.split())
        print(shapes)