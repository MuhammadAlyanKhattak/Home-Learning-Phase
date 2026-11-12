# Programming Exercise: Number of characters
# University of Helsinki Python MOOC
#
# Task:
# The function len can be used to find out the length of a string, among other things.
# The function returns the number of characters in a string.
#
# Please write a program which asks the user for a word and then prints out
# the number of characters, if there was more than one typed in.
#
# Examples of expected behaviour:
#
# Sample output 1:
# Please type in a word: hey
# There are 3 letters in the word hey
# Thank you!
#
# Sample output 2:
# Please type in a word: banana
# There are 6 letters in the word banana
# Thank you!
#
# Sample output 3:
# Please type in a word: b
# Thank you!

# Write your solution here

word = input("Please type in a word:")
lengthword = len(word)
if lengthword <= 1:
    print("Thank you!")
else:
    print(f"There are {lengthword} letters in the word {word}")
    print("Thank you!")
