# Program 3C
# Katie Devinney
# Calculates the diameter, circumference, and area of a circle based on user input radius

from math import pi

radius = float(input("Enter the length of the radius:"))
diameter = round(radius * 2, 2)
circumference = round(diameter * pi, 2)
area = round(pi * radius ** 2, 2)

print("Diameter: ", diameter, "\nCircumference: ", circumference, "\nArea: ", area)