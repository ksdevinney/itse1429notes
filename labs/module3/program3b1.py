# Program 3B1
# Katie Devinney
# uses a loop to add even integers until sentinel value is entered

sum = 0

while True:
    numberEntered = int(input("Enter a number or enter 9999 to quit: "))
    if numberEntered % 2 == 0: # only add even numbers
        sum += numberEntered # keep track of sum
    elif numberEntered == 9999:
        break

print("The sum of even numbers entered is: " + str(sum))