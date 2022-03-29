"""
Program 6A2
Katie Devinney
Reads numbers from a file, then sums the digits of each number
"""

def addDigits(x):
    length = len(x)
    sum = 0

    for i in range(length):
        current = x[i] # get the current number
        current = int(current) # convert to int for adding
        sum += current

    return sum

def main():
    file = open("lab6A2.txt", 'r')

    numbers = file.read()
    numbers = numbers.split()

    for i in range(len(numbers)):
        print("The number is %s" % numbers[i]) # print the number
        theSum = addDigits(numbers[i]) # call the function, as a variable to print in next step
        print("The sum of its digits is %d" % theSum)

if __name__ == "__main__":
    main()