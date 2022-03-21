# Program 5B2
# Katie Devinney
# determines if the user inputs an acceptable variable name

file = open("labs/module5/Lab5B2.txt", 'r')

words = file.read()
words = words.split() # read file for individual words

reservedWords = tuple(words) # tuple for reserved words

print("You are not allowed to use these words:\n", reservedWords)

variable = input("Enter a variable name: ")
acceptable = True # assumes variable passes all tests

if variable[0].isalpha() == False: # must start with a letter
    print("Variable names must start with a letter.")
    acceptable = False

for character in range(len(variable)): # no special characters
    if variable[character].isalpha() == False and variable[character].isnumeric() == False and not variable[character] == '_':
        print("Variable names can only contain letters, numbers, and _.")
        acceptable = False

if variable in reservedWords: # not a reserved word
    print("Variable cannot use words from the list of reserved words.")
    acceptable = False

if acceptable: # acceptable should still be True if passed all tests
    print("Your variable name is valid!")
else:
    print("Your variable name is not valid.")