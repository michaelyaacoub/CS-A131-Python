"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 07 Exercises - Part B
Date: 04/10/2023
---------------------------------------
Write a program that asks the user for a number between 10 and 20,
then initializes a list with the user given number of random integers,
and then displays to the console four lines of output, with the following data:
• Every element at an even index.
• Every even element.
• All elements in reverse order.
• Only the first and last element
Step 1: Ask the user for a number 10 - 20
Step 2: Generate random rolls for a 10 sided-die for the user given number
Step 3: Store the results of the rolls in a list (global variable)
Step 4: Filter and sort the list of rolls to display the information needed
Make sure you are using functions!
"""


from random import randint

rolls = []  # Global variable


def get_input():
    """ Prompt the user to enter a number between 10 - 20. """
    numbers = int(input("Choose a number 10 - 20: "))
    while True:
        if 10 <= numbers <= 20:
            return numbers
        numbers = int(input("Invalid! Choose a number 10 - 20: "))


def roll_dice(roll_dice):
    """ Generates a list of random rolls of a 10 sided dice. """
    for i in range(roll_dice):
        rolls.append(randint(1, 10))
    return rolls


def even_index():
    """ Returns every element at an even index."""
    result = ""
    for i in range(0, len(rolls), 2):
        if i != 0:
            result += ", "
        result += str(rolls[i])
        rolls.sort()
    return result


def even_element():
    """ Returns every even element. """
    result = []
    for i in range(len(rolls)):
        if rolls[i] % 2 == 0:
            result.append(rolls[i])
    return result


def rolls_reversed():
    """ Returns all elements of rolls reversed. """
    result = []
    for i in range(len(rolls) - 1, -1, -1):
        result.append(rolls[i])
    return result


def first_last():
    """ Returns first element and last element of the list"""
    first_element = rolls[0]
    last_element = rolls[-1]
    return str(first_element) + " " + str(last_element)


if __name__ == '__main__':
    num_rolls = get_input()
    dice_rolled = roll_dice(num_rolls)
    even_index_elements = even_index()
    even_element_in_rolls = even_element()
    reversed_elements = rolls_reversed()
    first_and_last = first_last()
    print("Elements at even index:", even_index_elements)
    print("The even elements are:", even_element_in_rolls)
    print("In reverse order:", reversed_elements)
    print("First and last:", first_and_last)
   

