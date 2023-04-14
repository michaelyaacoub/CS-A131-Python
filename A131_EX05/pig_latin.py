"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 05 Exercise - Part C
Date: 03/13/2023
---------------------------------------
Write a program that asks the user to enter a string and then prints the string in pig latin.
For all words in the string longer than two (2) characters, for each word,
remove the first character and add it to the end and then add "ay".
"""


def pig_latin(word):
    """Outputs a string in a pig latin format."""
    if len(word) > 2:
        return word[1:] + word[0] + "ay"
    else :
        return word

string = input("Enter a string: ")
words = string.split()
result = ""

for word in words :
    result += pig_latin(word) + " "
    
print(result)
