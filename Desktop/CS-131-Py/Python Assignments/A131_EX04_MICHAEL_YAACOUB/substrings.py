"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 04 Exercise - Part B
Date: 02/28/2023
---------------------------------------
Write a program that asks the user for a word, then prints all substrings, sorted by length.
"""

## string [starting index : ending index : step value]


word = input("Enter a word: ")

for i in word :
    print(i)
    
for j in range(len(word) -1) :
    if len(word) > 1 :
        print(word[j : j + 2])
print(word)
