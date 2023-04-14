"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 06 Exercises - Part B
Date: 03/22/2023
---------------------------------------
Write a function def same_set(a, b) that returns True if two lists have the same elements
in some order, ignoring duplicates. For example, the two lists
1 4 9 16 9 7 4 9 11
and
11 11 7 9 16 4 1
"""

def same_set(list1, list2):
    if contained(list1, list2) and contained(list2, list1):
        print("the same!!")
    else:
        print("not the same")

def contained(list1, list2):
    for element in list1:
        if element not in list2:
            return False

    return True

def result():
    assert same_set([1, 4, 9, 16, 9, 7, 4, 9, 11, 11], [11, 11, 7, 9, 16, 4, 1]) == True
    assert same_set([1, 4, 9, 16, 9, 7, 4, 9, 11, 11], [11, 11, 7, 9, 16, 4, 12345]) == False

if __name__ == "__result__":
    result()
