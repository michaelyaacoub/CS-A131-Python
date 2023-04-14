''' Programming Exam 4 Functions
 amTsaasan, Spring 2023
'''

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
    for i in range(len(upper_lower)):
        if upper_lower.isupper() is True:
            lower_case_letter += 1
        if lower_lower.lower() is False:
            upper_case_letter += 1
            
print(f"There are {upper_case_letter} upper case letters, {lower_case_letter} lower case letters.")

assert count_types("AAA") == 3
assert count_types("aaaa") == 4


def greeting():
    """Displays the consle"""
    print("Hello World!")



def grid(integer):
    """Takes in an int and displays the consle gird"""
    print("-" * integer)
    print("| " + " |")
    print("-" * integer)
    
assert grid(4) == print("----" * integer)


def password_change(string):
    """ Take in a string param and return it formated per changes"""
    word = 0
    result = ""
    for i in range(len(string)):
       if string[i] == "a" or if string[i] == "A"
   return result
   
assert password_change("aA") == "@"
assert password_change("iI") == "!"
