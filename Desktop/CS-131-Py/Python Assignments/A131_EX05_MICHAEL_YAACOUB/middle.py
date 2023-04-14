"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 05 Exercise - Part B
Date: 03/13/2023
---------------------------------------
Write a function named middle that takes a string as an input and
returns a string containing the middle
character of the input if the length of input string is odd,
or the two middle characters if the length is even.
"""


def middle(string):
    """ find middle char if str is odd or middle two chars if str is even. """
    if len(string) % 2 == 0:
        return string[(len(string) // 2) - 1: (len(string) // 2) + 1]
    else:
        return string[(len(string) // 2)]


print(middle("fiddle"))
print(middle("cat"))
