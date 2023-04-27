"""
-------------------------------
Name: Michael Yaacoub
Date: Apr/24/23
Assignemnt: EX08 - Part B
-------------------------------
Write a program that counts how many times each word appears in a text file using a dictionary. 
The program should ask the user for the filename, open the file, add each unique word to the dictionary 
as the key where the value of each is the count. Then, 
loop through the dictionary and display to the screen the words (and their counts) that appear more than 1000 times.
"""


def read_file(filename):
    """ Reads a file and returns a list of all words in the file."""
    with open(filename, 'r') as file:
        words = file.read().split()
    return words

def count_words(words):
    """ Counts the number of times each word appears in a list and returns a dictionary mapping each word to its count. """
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

def print_word_counts(word_counts, base):
    """ Prints out the words and their counts from a dictionary, but only if the count is greater than or equal to the given threshold. """
    for word, count in word_counts.items():
        if count >= base:
            print(word, count)

filename = input("Enter the filename: ")
words = read_file(filename)
word_counts = count_words(words)
print_word_counts(word_counts, 1000)

