"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 07 Exercises - Part A
Date: 04/10/2023
---------------------------------------
Write the following functions and provide a program to test them.
def firstDigit(n) (returning the first digit of the argument)
def lastDigit(n) (returning the last digit of the argument)
def digits(n) (returning the number of digits in the argument)

For example: firstDigit(1729) is 1, lastDigit(1729) is 9, and digits(1729) is 4.
"""


def digits(n):
    """ Returns the number of digits in the argument. """
    return len(str(n))


def first_digit(n):
    """ Returns the first digit passed. """
    n_str = str(n)
    return n_str[0]


def last_digit(n):
    """ Returns the last digit passed. """
    n_str = str(n)
    return n_str[- 1]


# Testing functions with the 1729
assert digits(1729) == 4
print("The number of digits in 1729: ", digits(1729))
assert first_digit(1729) == "1"
print("The first int in 1729 is: ", first_digit(1729))
assert last_digit(1729) == "9"
print("The last int in 1729 is: ", last_digit(1729))
