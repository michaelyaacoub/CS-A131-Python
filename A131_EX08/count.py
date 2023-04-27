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
    with open(filename, 'r') as file:
        return file.read().split()

def unique_words():
    get_file = input("Enter the name of a file: ")

    content_file = read_file(get_file)

    unique_dict = {}

    for word in content_file:
        if word in unique_dict:
            unique_dict[word] += 1
        else:
            unique_dict[word] = 1
            
    return unique_dict

unique_dict = unique_words()

for word, count in unique_dict.items():
        if count > 1000:
            print(word, ':', count)
    
