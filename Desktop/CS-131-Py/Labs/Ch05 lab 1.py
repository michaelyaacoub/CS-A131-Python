"""
---------------------------------------
Name: Michael Yaacoub - Nalan Pandian
Group Assignment: Ch05 Lab 1.1
Date: 03/07/2023
---------------------------------------
"""

def two_numbers(val_1,val_2):
    '''A function that takes in two number input parameters and returns the higher number'''
    if val_1 > val_2 :
        return val_1
    elif val_2 > val_1 :
        return val_2
   
assert two_numbers(12,42) == 42
print(two_numbers(3,25))  
   
   
def greeting():
    ''' function that takes in NO input parameters and prints a greeting'''
    print ("Good morning")
   
greeting()

def string_out(name):
    '''A function that takes in a string input and prints to the console "Happy Birthday'''
    print("Happy Birthday", name)
   
string_out("Nalan")
   
def three_num(a,b,c):
    '''A function that takes in three number input parameters and returns True if the first two can be added together to equal the last one, and False in any other case'''
    if a + b == c :
        return True
    else: return False

assert three_num(20,20,40) == True
print(three_num(18,18,26))
