"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 07 Exercises - Part C
Date: 04/10/2023
---------------------------------------
Write a program that takes in a string and a list of small words,
then prints to the screen the string with all the small words
from the list removed from the string.
"""


def get_input():
    """ Gets a string input and a list input. """
    input_string = input("Enter string: ")
    input_list = input("Enter list: ")
    user_list = input_list.strip('[]').split(", ")
    small_words = [word.strip().lower() for word in user_list]  # append elements lowered without whitespaces.
    return input_string, small_words


def remove_small_words(string, small_words):
    """ Returns the string with all the small words from the list removed. """
    words = string.split()  # split string into individual words
    result = []
    for word in words:
        if word.lower() not in small_words:  # check if word is small
            result.append(word)
    return " ".join(result)  # join remaining words back into a string


if __name__ == '__main__':
    input_string, small_words = get_input()
    updated_text = remove_small_words(input_string, small_words)
    print("Updated text: ")
    print(updated_text)
