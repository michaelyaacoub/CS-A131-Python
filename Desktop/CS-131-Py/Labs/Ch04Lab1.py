"""
---------------------------------------
Name: Michael Yaacoub
Assignment: CH.04 Lab 01
Date: 02/28/2023
---------------------------------------

Enter all the scores to be averaged.
Enter a negative number after you are done.
"""

grades_total = 0
count = 0

grade = int(input("Enter a positive number to get ave / else enter a sentinel num to quit: "))

while grade >= 0:
    count += 1
    grades_total = grades_total + grade
    if grade <= -1 :
        break
    grade = int(input())

print("Average is: ", grades_total / count)
