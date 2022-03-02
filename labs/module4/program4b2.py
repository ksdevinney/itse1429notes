# Program 4b2
# Katie Devinney
# reads an input file

file = open("labs/module4/Lab4B2.txt", 'r')
combinedString = ""

for line in file:
    stringList = line.split() # create 2 strings from file
    for count in range(len(stringList[0])):
        combinedString += stringList[0][count] # add one letter from first string
        combinedString += stringList[1][count] # add one letter from second string
print("The new string is " + combinedString)