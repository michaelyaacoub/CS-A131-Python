# --------------------------------------
# Name: Michael Yaacoub
# Date: 03/09/2023
# Ch.05 Lab 1.2 Guessing Game
# --------------------------------------
"""
Writes a program that assigns a random int to a variable. 
Asks the user to guess the number.
Give hints if the user guesses too high or too low.
Using a function
"""
from random import randint

#correct_answer = randint(1,10) # 10
#guess = int(input("Guess a number: "))  # 5
def guessing_game(guess, correct_answer):
    response = "You have the right answer!"

    while guess != correct_answer : 
        if guess < correct_answer :
            print("Too low.")
            guess = int(input("Guess a number: "))
        if guess > correct_answer :
            print("Too high.") 
            guess = int(input("Guess a number: "))
    
    print(response) 

#guessing_game(4, 7)