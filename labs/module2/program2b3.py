# Program 2B3
# Katie Devinney
# Takes in 5 test grades and calculates the average grade

testOne = float(input("Enter test grade 1: "))
testTwo = float(input("Enter test grade 2: "))
testThree = float(input("Enter test grade 3: "))
testFour = float(input("Enter test grade 4: "))
testFive = float(input("Enter test grade 5: "))

sum = testOne + testTwo + testThree + testFour + testFive
average = str(sum / 5)

print("The average is " + average)