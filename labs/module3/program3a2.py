# Program 3A2
# Katie Devinney
# Calculates the sum of all numbers before an input number, and averages them

selectedNumber = int(input("Enter a number: "))
sum = 0
inBetween = 0

if selectedNumber == 0: # get a nonzero number
    electedNumber = int(input("Enter a number: "))

for count in range(1, selectedNumber + 1):
    sum += count
    inBetween += 1

average = sum / selectedNumber

print("sum: %-6d" % sum + "numbers between: %-6d" % inBetween + "average: %-6.2f" % average)