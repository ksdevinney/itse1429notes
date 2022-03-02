# Program 2B
# Katie Devinney
# Calculates average speed based on user input for distance and time

distance = float(input("Enter the distance in miles: "))
time = float(input("Enter the time in hours: "))
speed = distance / time

print("Distance covered: ", distance, " miles\nTravel Time: ", time, " hours\nAverage Traveling Speed: ", round(speed, 3), " miles per hour")