# Chapter 7: Simple Graphics and Image Processing

## Simple Graphics

Turtle graphics- simple tools for drawing pictures
Uses a coordinate system (x, y) with origin at center of the window

Turtle state:
Heading: value in degrees- turns the turtle counterclockwise (initially set at 0, facing east)
Color: what color the turtle's pen is (initially black)
Width: width of the line drawn
Down: either true or false, controls if the turtle's pen is up (not drawing) or down (drawing)

State: set of values of its attributes of any given moment

Turtle class has many different methods- 7.1b

Turtle configuration file (turtle.cfg) is a text file that contains the initial turtle attributes

Book examples use:
width = 300
height = 200
using_IDLE = True
colormode = 255

You have to create an instance of The Turtle before using it, using a constructor

> from turtle import Turtle
> t = turtle()

mutator methods: change the internal state

accessor methods: return the value of an attribute

Can change the turtle's pen color using .pencolor() method, with either a color word as an argument or RGB values

## Image Processing

Analog information includes a continuous range of values

images are sampled? into pixels

Raw image file: all sampled information, best looking but largest file size
Compression schemes, like analyizing adjacent pixels for the same color and saving a location instead of the color

Lossless: no information is lost

Lossy: some information is lost (still looks fine when image is decompressed)

Gif compression scheme: 1. algorithm analyzes image for up to 256 of the most prevalent colors, 2. each sample in the grid is replaced with th ekey of the closest color

For images, (0, 0) is at the upper left corner, (width - 1, height - 1) at the bottom right

*images* module contains image processing algorithms
Uses the Image class, images must be .gif

Many image processing algorithms use nested loops- the outer loop iterates over one coordinate, the inner loop iterates over the other

Pixel RGB values are stored in a tuple. You can manipulate pixels by getting the values of the tuple and assign new values to a new tuple, then reset the pixel to the new tuple

7.2i: converting to black and white (spoiler: replace each pixel with black or white, depending on what's closer to the color)

7.2j: converting to grayscale (multiply each color value by a luminance weight factor, then add them together and set the sum as each value in RGB)