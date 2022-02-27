# Program 4A2
# Katie Devinney
# Creates a string based on the first letter of each word in a sentence

sentence = input("Enter a sentence: ")

seperatedSentence = sentence.split()
firstLetters = '' # for the first letters

for words in range(0, len(seperatedSentence)): # loop through the words
    firstLetters += seperatedSentence[words][0] # add first letter to the string

print(firstLetters)