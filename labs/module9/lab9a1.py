# Lab 9A1
# Katie Devinney
# Uses DistanceCalculator class to calculate distance between two points

from distancecalculator import DistanceCalculator

def main():
    x1 = float(input("Enter the first x value: "))
    y1 = float(input("Enter the first y value: "))
    x2 = float(input("Enter the second x value: "))
    y2 = float(input("Enter the second y value: "))

    point1 = DistanceCalculator(x1, y1, x2, y2)

    point1.getDistance()

    print(point1.__str__())

if __name__ == "__main__":
    main()