# Program 5B2
# Katie Devinney
# determines if the user inputs an acceptable variable name

file = open("labs/module5/Lab5B2.txt", 'r')

words = file.read()
words = words.split()

reservedWords = tuple(words)

print("You are not allowed to use these words:\n", reservedWords)

variable = input("Enter a variable name: ")
acceptable = True

if variable[0].isalpha() == False:
    print("Variable names must start with a letter.")
    acceptable = False

for character in range(len(variable)):
    if variable[character].isalpha() == False and variable[character].isnumeric() == False and not variable[character] == '_':
        print("Variable names can only contain letters, numbers, and _.")
        acceptable = False

if variable in reservedWords:
    print("Variable cannot use words from the list of reserved words.")
    acceptable = False

if acceptable:
    print("Your variable name is valid!")
else:
    print("Your variable name is not valid.")