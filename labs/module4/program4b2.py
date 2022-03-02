# Program 4b2
# Katie Devinney
# reads an input file

import string


file = open("labs/module4/Lab4B2.txt", 'r')
combinedString = ""

for line in file:
    stringList = line.split()
    # -_-
    for word in stringList:
        combinedString += "1a"
print(combinedString)