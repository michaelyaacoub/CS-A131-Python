''' Programming Exam 5
 Chapter 6, Lists
 amT, Spring 2023
 '''
"""
Name: Michael Yaacoub
Assignment: PE05
Date: 03/23/2023
"""

def create_empty(positive_int, values):
   """ Returns a list which length of the int with the value in each element """
   result = []
   for i in range(values):
      result = values[i] * positive_int
      
   return result
   
assert create_empty(3, "Max") == ['Max', 'Max', 'Max']
assert create_empty(4, "22") == [22, 22, 22, 22]


def exam_drop_lowest(grade, int_value):
   """ Takes a list and a positive value, drops the lowest and returns the avarage of values"""
   largest = grade[0]
   smallest = grade[0]
   avarage = 0
   for i in range(int_value):
      if i > int_value[i]:
         largest = int_value[i]
      elif i < int_value[i]:
         smallest = int_value[i]
         
      return avarage
   pass

assert exam_drop_lowest([0, 40, 30, 40, 50], 2) == 43.33
assert exam_drop_lowest([20, 40, 30, 40, 50], 0) == 36.0


def npc_action(int_1, int_2, int_3):
   """ Takes in 3 ints and evaluates if action is taken, returns a boolean"""
   pass

assert npc_action(1,4,5) == True
assert npc_action(3,6,0) == False



def order_lists(list_1, list_2):
   """ Takes in two lists, returns a new list with elements in order"""
   length_1 = len(list_1)
   length_2 = len(list_2)
   result = []
   pass

assert order_lists([3,2,1],[6,4,5]) == [1, 2, 3, 4, 5, 6]
assert order_lists(['z', 'b', 'a'], ['c', 'n', 'h']) == ['a', 'b', 'c', 'h', 'n', 'z']


from random import randint



