"""
-------------------------------
Name: Michael Yaacoub
Date: Apr/24/23
Assginment: EX08 - Part A
-------------------------------
Write a program that reads in two text files and prints out, 
in sorted order, all words that are common to both of them.
"""

def read_file(filename):
    """ Reads a file and returns a list of all words in the file. """
    with open(filename, 'r') as file:
        words = file.read().split()
    return words

# Read in the two files
file1 = read_file("menu.txt")
file2 = read_file("menu1.txt")

# Find the common words
common_words = sorted(list(set(file1) & set(file2)))

# Print out the common words
print("The words that are common to both files. ")
for word in common_words:
    print(word)

