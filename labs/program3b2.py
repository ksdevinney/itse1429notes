# Program 3b2
# Katie Devinney
# Gets input and checks if that input meets certain criteria

firstNum = int(input("Enter a number: "))
secondNum = int(input("Enter a number that is smaller than the previous number: "))

while secondNum >= firstNum: # get numbers in correct order
    firstNum = int(input("Try again! Enter a number: "))
    secondNum = int(input("Enter a number that is smaller than the previous number: "))

numberSum = firstNum + secondNum # to check condition
numberDiff = firstNum - secondNum # to check condition

if firstNum % 10 == 0 or secondNum % 10 == 0 or numberSum % 10 == 0 or numberDiff % 10 == 0: # any of these can be true
    print("We have 10s!")
else: # if none of those are true...
    print("No 10s here...")