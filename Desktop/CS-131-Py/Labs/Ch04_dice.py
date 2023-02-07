"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch.04 - Dice Lab
Date: 03/02/2023
---------------------------------------
This program simulates tosses of a pair of dice.
"""

from random import randint

for i in range(10) :
    d1 = randint(1, 6)
    d2 = randint(2, 8)

    print("Dice Roll: ", d1, d2)
