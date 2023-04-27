"""
-------------------------------
Name: Michael Yaacoub
Date: Apr/24/23
Assignemnt: EX08 - Part C
-------------------------------
Write a program that reads in a text file, converts all words to lowercase, 
and prints out all words in the file that contain a letter chosen by the user. 
Build a dictionary whose keys are the lowercase letters, 
and whose values are sets of words containing the given letter.
"""

def build_letter_dict(filename):
    """ Build a dictionary whose keys are lowercase letters and whose values are sets of words containing the given letter. """
    letter_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                word = word.lower()
                letters = set(word)
                for letter in letters:
                    letter_dict.setdefault(letter, set()).add(word)

    return letter_dict


def filename_from_user():
    """ Get the filename from the user. """
    filename = input("Enter the name of the file to open: ")
    letter_dict = build_letter_dict(filename)
    letter = input("Enter letter to see included words: ")
    letter = letter.lower()
    if letter in letter_dict:
        print("Words containing '{}':".format(letter))
        for word in letter_dict[letter]:
            print(word)
    else:
        print("No words containing the letter '{}' in the file.".format(letter))


if __name__ == '__main__':
    filename_from_user()

