# Program 4B3
# Katie Devinney
# reads strings from a file and prints them in a different order

file = open("labs/module4/Lab4B3.txt", 'r')

for line in file:
    cleanLine = line.strip()
    name = cleanLine.split(",")
    lastName = name[0]
    # print(lastName)
    firstName = name[1]
    # print(firstName)
    initial = name[2]
    # print(initial)
    print(firstName +  initial + " " + lastName)

# print(name)