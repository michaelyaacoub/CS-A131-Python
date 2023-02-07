# # ##credit_num = input("Enter a credit card number: ")
# # ##
# # ##if len(credit_num) == 19 and credit_num[4] == '-' and credit_num[9] == '-' and credit_num[14] == '-':
# # ##    print("Card Number:", credit_num)
# # ##elif len(credit_num) == 16 :
# # ##    print("Card Number:", credit_num)
# # ##else :
# # ##    print("invalid input")
# #
# #
# # """ Given a string, return a new string where the first and last chars have been exchanged. """
# #
# #
# # def string(str):
# #     if len(str) <= 1:
# #         return str
# #
# #     middle = str[1:len(str) - 1]
# #     # last + mid + first
# #     return str[len(str) - 1] + middle + str[0]
# #
# #
# # print(string("Michael"))
# # print(string("Jackson"))
# #
# # print()
# # """
# # Given a string, we'll say that the front is the first 3 chars of the string.
# # If the string length is less than 3, the front is whatever is there.
# # Return a new string which is 3 copies of the front.
# # """
# #
# #
# # def front_three(str):
# #     if len(str) < 3:
# #         return str + str + str
# #     front_3 = str[0:3]
# #     return front_3 + front_3 + front_3
# #
# #
# # print(front_three("Michael"))
# # print(front_three("Jackson"))
# #
# # print()
# # """
# # Given a string and a non-negative int n, return a larger
# # string that is n copies of the original string.
# # """
# #
# #
# # def string_times(str, n):
# #     return str * n
# #
# #
# # print(string_times("Hi", 2))
# # print(string_times("Hi", 3))
# # print(string_times("Hi", 5))
# #
# # print()
# # """
# # Given a string, return a new string made of every other char
# # starting with the first, so "Hello" yields "Hlo".
# # """
# #
# #
# # def string_bits(str):
# #     result = ""
# #     for i in range(len(str)):
# #         if i % 2 == 0:
# #             result = result + str[i]
# #     return result
# #
# #
# # print(string_bits("Rica"))
# # print(string_bits("Egypt"))
# # print(string_bits("Heeololeo"))
# #
# # print()
# # """
# # Given an array of ints, return True if
# # one of the first 4 elements in the array is a 9.
# # The array length may be less than 4.
# # """
# # # def array_front9(nums):
# # #   end = len(nums)
# # #   if end > 4 :
# # #     end = 4
# # #
# # #   for i in range(end) :
# # #     if nums[i] == 9 :
# # #       return True
# # #   return False
# # #
# # # print(array_front9([1, 2, 9, 3, 4]))
# # # print(array_front9([1, 2, 3, 4, 5]))
# # #
# # #
# # # def boxString(contents):
# # #    n = len(contents)
# # #    print("-" * (n + 2))
# # #    print("!" + contents + "!")
# # #    print("-" * (n + 2))
# # #
# # # print(boxString("HiBug"))
#
#
# """
# Name: Michael Yaacoub
# Date: 03/16/23
# Assiginment: Programming Exam 4 - RESUBMISION
# --------------------------------
# Write a four (4) functions in alphabetical order,
# to be complete a function must include a descriptive
# docstring (PEP8 and David Kay's Design Recipe).
# The functions must be named:
# """
#
#
# # def count_types(upper_lower):
# #     """Takes in a string and returns a string"""
# #     upper_case_letter = 0
# #     lower_case_letter = 0
# #     for i in range(len(upper_lower)):
# #        if upper_lower.isupper() is True:
# #             lower_case_letter += 1
# #        if lower_lower.lower() is False:
# #             upper_case_letter += 1
#
# # print(f"There are {upper_case_letter} upper case letters, {lower_case_letter} lower case letters.")
#
# # assert count_types("AAA") == 3
# # assert count_types("aaaa") == 4
#
#
# def count_types(upper_lower):
#     """Takes in a string and returns a string"""
#     result = ""
#     upper_case_letter = 0
#     lower_case_letter = 0
#
#     for i in range(len(upper_lower)):
#         if upper_lower[
#             i].isupper():  # err: Didn't point at the index when checking for isupper() and used wrong operator.
#             upper_case_letter += 1
#         elif upper_lower[
#             i].islower():  # err: Didn't point at the index when checking for islower() and used wrong operator.
#             lower_case_letter += 1
#     result = "There are " + str(upper_case_letter) + " upper case letters, " + str(
#         lower_case_letter) + " lower case letters."  # err: Didn't store outcome in a var.
#
#     return result  # err: return statement didn't exist which function didn't have anything to return and to test.
#
#
# assert count_types(
#     "NEAAWfannncyP@$$word") == "There are 6 upper case letters, 11 lower case letters."  # reformatted result and added expected output
# assert count_types(
#     "Hello CS Studnetss") == "There are 4 upper case letters, 12 lower case letters."  # reformatted resutl and added expected output
#
#
# def greeting():
#     """Displays the consle"""
#     print("Hello World!")
#
#
# # def grid(integer):
# #     """Takes in an int and displays the consle gird"""
# #     print("-" * integer)
# #     print("| " + " |")
# #     print("-" * integer)
#
# # assert grid(4) == print("----" * integer)
#
#
# def grid(integer):
#     """Takes in an int and displays the consle gird"""
#     count = 0
#     while count < integer:
#         print('-' + "---" * integer)  # print roof separated
#         print('| ' + '| ' * integer)  # print the inside with proper spacing
#         print('-' + "---" * integer)  # print the bottom as the roof
#
#         count += 1  # increment, no assert needed since the function don't return a value
#
#
# # def password_change(string):
# #     """ Take in a string param and return it formated per changes"""
# #     word = 0
# #     result = ""
# #     for i in range(len(string)):
# #        if string[i] == "a" or if string[i] == "A"
# #    return result
#
# # assert password_change("aA") == "@"
# # assert password_change("iI") == "!"
#
#
# def password_change(string):
#     """ Take in a string param and return it formated per changes"""
#     result = ""
#     for i in range(len(string)):
#         if string[i] == 'A' or string[i] == 'a':
#             result = result + '@'  # return the correct output
#         elif string[i] == 'I' or string[i] == 'i':  # check for 'I' and 'i'
#             result = result + '!'  # return the correct output
#         elif string[i] == 'S' or string[i] == 's':  # check for 'S' and 's'
#             result = result + '$'  # return the correct output
#         else:
#             result = result + string[i]  # wrote an else statement as final result
#
#     return result  # proper indentation
#
#
# assert password_change("a") == "@"  # proper indentation and expected output
# assert password_change("I") == "!"  # proper indentation and expected output
#
#
# title = "Python for Everyone"
# newTitle = title.replace("e", "*")
# print(newTitle)
#

x = [5, 3, 7, 9, 1]
y = x[: 2]
print(y)
