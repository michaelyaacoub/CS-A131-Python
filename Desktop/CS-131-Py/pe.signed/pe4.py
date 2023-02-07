"""
Name: Michael Yaacoub
Date: 03/16/23
Assiginment: Programming Exam 4
--------------------------------
Write a four (4) functions in alphabetical order,
to be complete a function must include a descriptive
docstring (PEP8 and David Kay's Design Recipe).
The functions must be named:
"""


def count_types(upper_lower):
    """Takes in a string and returns a string"""
    upper_case_letter = 0
    lower_case_letter = 0
    result = ""
    for i in range(len(upper_lower)):
        if upper_lower[i].isupper():
            lower_case_letter += 1
        if upper_lower[i].islower():
            upper_case_letter += 1
    result = "There are " + str(lower_case_letter) + " upper case letters, " + str(
        upper_case_letter) + " lower case letters."
    return result


assert count_types("NEAAWfannncyP@$$word") == "There are 6 upper case letters, 11 lower case letters."
assert count_types("Hello CS Studnetss") == "There are 4 upper case letters, 12 lower case letters."


def greeting():
    """Displays the consle"""
    print("Hello World!")


def grid(integer):
    """Takes in an int and displays the consle gird"""
    count = 0
    while count < integer:
        print('-' + "---" * integer)
        print('| ' + '| ' * integer)
        print('-' + "---" * integer)

        count += 1


def password_change(string):
    """ Take in a string param and return it formated per changes"""
    result = ""
    for i in range(len(string)):
        if string[i] == 'a' or string[i] == 'A':
            result = result + '@'
        elif string[i] == 'i' or string[i] == 'I':
            result = result + '!'
        elif string[i] == 's' or string[i] == 'S':
            result = result + '$'
        else:
            result = result + string[i]
    return result

assert password_change("NAAAWpassword4thiswebsite") == "N@@@Wp@$$word4th!$web$!te"
assert password_change("Hellosss") == "Hello$$$"