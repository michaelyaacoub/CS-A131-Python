"""
-----------------------------------
Name: Michael Yaacoub
Date: Apr/15/23
Assignment: EX07 - Part A
-----------------------------------
Write a program that asks the user for a file name 
and prints the number of characters, words, and lines in that file.
"""

def get_file():
    """ Ask user for file name and return the opened file object """
    filename = input("Enter file name: ")
    with open(filename, "r") as infile:
        return infile.read()


def count_lines(file):
    """ Counts the lines in a file. """
    my_line = len(file.split('\n'))
    return my_line

def count_words(file):
    """ Counts the words in a file. """
    my_words = len(file.split())
    return my_words

def count_characters(file):
    """ Counts the characters in a file. """
    my_char = len(file)
    return my_char

if __name__ == '__main__':
    file  = get_file()
    lines = count_lines(file)
    words = count_words(file)
    chars = count_characters(file)

    print(f"The file contains '{chars}' characters, '{words}' words and '{lines}' lines")
