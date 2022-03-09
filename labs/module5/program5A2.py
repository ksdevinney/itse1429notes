# Program 5A2
# Katie Devinney
# 

import random

randomList = []
oddCount = 0
oddList = []
evenCount = 0
evenList = []

for index in range(15):
    randomList.append(random.randint(1, 20)) # create list of 15 random ints
print("Here is a list of random numbers:", randomList)

for index in range(len(randomList)):
    if randomList[index] % 2 != 0:
        oddCount += 1 # count odd numbers
        oddList.append(randomList[index]) # create list of odd numbers
    else:
        evenCount += 1 #count even numbers
        evenList.append(randomList[index]) # create list of even numbers
print("There are", oddCount, "odd numbers in the list.")
print("Here are the odd numbers from the list:\n", oddList)
print("There are", evenCount, "even numbers in the list.")
print("Here are the even numbers from the list:\n",evenList)