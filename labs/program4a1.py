# Program 4A1
# Katie Devinney
# checks to see if two words have the same first and last letter

wordOne = input("Enter a word: ")
wordTwo = input("Enter a word: ")

if wordOne[0] == wordTwo[0]: #check first letter
    print("These words have the same first letter.")
if wordOne[-1] == wordTwo[-1]: # check last letter
    print("These words have the same last letter. ")
if wordTwo in wordOne: # word 2 inside of word 1
    print(wordTwo + " is inside of " + wordOne + ".")