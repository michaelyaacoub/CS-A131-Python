"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 05 Exercise - Part A
Date: 03/13/2023
---------------------------------------
Write a function count_words that returns a count of all words in the string string.
Words are separated by spaces.
"""


def count_words(string):
    """ Count words based on how many spaces in a sentence. """
    letter_space = 0
    for i in range(len(string)):
        if string[i] == ' ':
            letter_space += 1
    return letter_space


print(count_words("Mary had a little lamb"))
