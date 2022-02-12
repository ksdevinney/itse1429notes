# Program 3A3
# Katie Devinney
# Determines if a number is even or odd

for numbers in range(5):
    inputNumber = int(input("Enter a number: "))
    if inputNumber % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")