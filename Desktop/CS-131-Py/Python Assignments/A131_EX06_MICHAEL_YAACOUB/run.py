"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 06 Exercises - Part A
Date: 03/22/2023
---------------------------------------
A run is a sequence of adjacent repeated values. Write a program with as many functions
and _helper functions as needed to generate a sequence of 20
random die tosses (one 6-sided die), store them in a list, and print the die values,
marking the runs by including them in parentheses, like this:

1 2 (5 5) 3 1 2 4 3 (2 2 2 2) 3 6 (5 5) 6 3 1
"""

from random import randint

def roll_dies():
    values_list = []

    for i in range(20):
        values = randint(1, 6)
        values_list.append(values)

    in_run = False
    for i in range(20 - 1):
        if in_run:
            if values_list[i] != values_list[i - 1]:
                print(")", end="")
                in_run = False
        if not in_run:
            if values_list[i] == values_list[i + 1]:
                print("(", end=" ")
                in_run = True
        print(values_list[i], end=" ")
    if in_run:
        print(")")

roll_dies()
