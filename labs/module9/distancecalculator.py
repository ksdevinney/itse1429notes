# distancecalculator
# Katie Devinney
# a class for storing information about coordinate points

import math

class DistanceCalculator(object):

    def __init__(self, x1, y1, x2, y2):
        self.firstX = x1
        self.firstY = y1
        self.secondX = x2
        self.secondY = y2
        
        self.pointDistance = 0

    def getDistance(self):
        self.pointDistance = math.sqrt((self.secondX - self.firstX) ** 2 + (self.secondY - self.firstY) ** 2)

    def __str__(self):
        return "Point 1: (" + str(self.firstX) + ", " + str(self.firstY) + ") \nSecond point: (" + str(self.secondX) + ", " + str(self.secondY) + ")\nDistance between point 1 and point 2: " + str(self.pointDistance) 