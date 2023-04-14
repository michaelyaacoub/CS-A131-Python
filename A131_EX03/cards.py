"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 03 Exercises - Part A
Date: 02/28/2023
---------------------------------------
Write a program that takes user input describing a poker playing card in the following shorthand notation:
first character is the card value, the second character is the card suit.
"""

card_value = input("Enter the first character value of your card: ").upper()


if len(card_value) > 2 :
    first_position = card_value[1]
else :
    first_position = card_value[0]

second_position = card_value[-1]
if first_position == 'A' :
    first_position = 'Ace'
elif first_position == 'J' :
    first_position = 'Jack'
elif first_position == 'Q':
    first_position = 'Queen'
elif first_position == 'K' :
    first_position = 'King'
elif first_position == '0' :
    first_position = '10'

if second_position == 'D' :
    second_position = 'Dimonds'
elif second_position == 'S' :
    second_position = 'Spades'
elif second_position == 'C' :
    second_position = 'Clubs'
elif second_position == 'H' :
    second_position = 'Hearts'

print(first_position + " of " + second_position)
