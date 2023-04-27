"""
-----------------------------
Name: Michael Yaacoub
Date: Apr/16/23
Assignment: EX07 - Part C
-----------------------------
Write a program that asks the user to input a set of floating-point values. 
When the user enters a value that is not a number, 
give the user a second chance to enter the value. After two chances, 
quit reading input. 
Add all correctly specified values and print 
the sum when the user is done entering data. 
Use exception handling to detect improper inputs.
"""

def read_float():
    """ Checks for user input validation validation after two prompts then sums input. """
    while True:
        try:
            return float(input("Enter a number, or another non-number to quit: "))
        except ValueError:
            return None


def get_sum():
    """ Asks user for input and checks for input err. """
    total = 0.0
    num_tries = 0
    while num_tries < 2:
        value = read_float()
        if value is None:
            num_tries += 1
            if num_tries >= 2:
                break
        else:
            total += value
            num_tries = 0
    print("The total is", total)


if __name__ == "__main__":
    get_sum()


