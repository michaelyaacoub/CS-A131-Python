"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 04 Exercise - Part C
Date: 03/05/2023
---------------------------------------
Write a program that asks the user to enter a string and then prints the number of vowels in the word. For this exercise,
assume that a e i o u y are vowels.
"""

string = input("Enter a string: ")

vowel = 0
for i in range(len(string)):
    if (
        string[i] == "a"
        or string[i] == "e"
        or string[i] == "i"
        or string[i] == "o"
        or string[i] == "u"
        or string[i] == "y"
    ):
        vowel += 1
    
print("The number of vowels is ", vowel)
