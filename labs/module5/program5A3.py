# Program 5A3
# Katie Devinney
# Reads a list from file and determines if the numbers are going up or down

inFile = open("labs/module5/Lab5A34.txt", 'r')

line = inFile.read()
numbers = line.split()
length = len(numbers)

for index in range(length):
    numbers[index] = int(numbers[index]) # convert strings to ints
print(numbers)

descending = False
ascending = False

for index in range(length - 1):
    if numbers[index] > numbers[index - 1]:
        ascending = True
        descending = False
    elif numbers[index] < numbers[index - 1]:
        descending = True
        ascending = False
    else:
        print("equal")

if ascending and not descending:
    print("The list is going up.")
elif descending and not ascending:
    print("The list is going down.")
elif not descending and not ascending:
    print("The list is not going up or down.")