"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 04 Exercises - Part A
Date: 03/05/2023
---------------------------------------
Write a program that asks the user for floating-point values
until they enter 0 to quit, then print
"""

float_input = float(input("Enter a number (0 to quit): "))
total_count = 0.0
count = 0
largest = float_input
smallest = float_input

while float_input != 0 :
    float_input = float(input("Enter a number (0 to quit): "))
    if float_input == 0 :
      break
    
    count += 1
    total_count += float_input
    avarage = total_count / count
    
    if float_input > largest :
        largest = float_input
    elif float_input < smallest :
        smallest = float_input

    range_value = largest - smallest
    
print("The largest value is: ", largest)
print("The smallest value is: ", smallest)
print("The average of the values is: ", avarage)
print("The range of the values is: ", range_value)
