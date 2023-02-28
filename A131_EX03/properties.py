"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 03 Exercises - Part C
Date: 02/28/2023
---------------------------------------
Write a program that reads in a string and prints whether it
- contains only letters
- contains only uppercase letters
- contains only lowercase letters
- contains only digits
- contains only letters and digits
- starts with an uppercase letter
- ends with a period
"""

properties_string = input("Enter a string: ")

if properties_string.isalpha() :
    print('The string contains only letters')

elif properties_string.isupper() :
    print('All letters in string are upper case letters')

elif properties_string.islower() :

    print('All letters in string are lower case letters')

elif properties_string.isdigit() :
    print('The string contains only digits')

elif properties_string.isalnum() :

    print('The string contains only letters and/or digits')

elif properties_string[0].isupper() :
    print('The string starts with an upper case character')

elif properties_string.endswith('.'):
    print('The string ends with a period')
