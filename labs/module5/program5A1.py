# Program 5A1
# Katie Devinney
# reads and manipulates numbers in a list

inFile = open("labs/module5/Lab5A1.txt", 'r')

numberLine = inFile.readline()
numberLine = numberLine.split() # creates a list from input file

for index in range(len(numberLine)):
    numberLine[index] = int(numberLine[index]) # converts values to integers
print("The numbers are:\n", numberLine)

sumList = 0
for position in range(0, 5):
    sumList += numberLine[position] # adds the first 5 numbers
print("The sum of the first 5 numbers is ", sumList)

listLength = len(numberLine) # for range on next 2

numberCount = 0
inputNumber = int(input("Enter a number between 0-10: "))
for numbers in range(listLength):
    if numberLine[numbers] == inputNumber:
        numberCount += 1 # increments each time number is found
print("Your number is in this list", numberCount, "time(s).")

newList = []
removeNumber = int(input("Enter another number between 0-10: "))
for integer in range(listLength):
    if numberLine[integer] != removeNumber:
        current = numberLine[integer] # variable for numbers to add to new list
        newList.append(current)
print("Here, I removed all the", removeNumber, "for you:\n", newList)

