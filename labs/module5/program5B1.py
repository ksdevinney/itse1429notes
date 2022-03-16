# Program 5B1
# Katie Devinney
# Fills a dictionary from file, searches for a name, age, and finds the highest age

people = {}

file = open("labs/module5/Lab5B1.txt", 'r')

person = []

for line in file: # fill the dictionary
    person = line.split()
    people[person[0]] = int(person[1])

print("Here is a list of people:\n", people) # print the list

name = input("Enter a name to search: ")

if people.get(name): # search for name
    print("That name is on the list.")
else:
    print("That name does not appear on the list.")

count = 0 
max = 0 # to hold the highest age
age = int(input("Enter an age: "))

for info in people.values():
    if info == age: # count how many times the requested age appears
        count += 1
    if info > max: # find the highest age
        max = info

print("That age appears", count, "times.")
print("The higest age is:", max)