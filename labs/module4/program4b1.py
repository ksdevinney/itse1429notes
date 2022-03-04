# Program 4B1
# Katie Devinney
# Reads integers from a file, uses file input for calculation

file = open("labs/module4/Lab4B1.txt", 'r') # open file

oddSum = 0 # variable for sum

for line in file: # read each line of the file
    numberList = line.split() # split along spaces
    for eachEntry in numberList:
        number = int(eachEntry) # convert each string to a number
        if number % 2 != 0: # only add the odd numbers
            # print(number)
            oddSum += number
print("The total is", oddSum)