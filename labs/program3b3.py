# Program 3b3
# Katie Devinney
# rolls two dice 5 times and finds the largest sum of the rolls

import random

maxSum = 0

for rolls in range(1, 6):
    dieOne = random.randint(1, 6)
    dieTwo = random.randint(1, 6)
    sum = dieTwo + dieOne # sum for each round
    print("Dice roll: " + str(dieOne) + " " + str(dieTwo))
    if maxSum < sum: # if this sum is larger than current max...
        maxSum = sum # set new sum
    # print(maxSum) # test

print("The largest sum was " + str(maxSum))