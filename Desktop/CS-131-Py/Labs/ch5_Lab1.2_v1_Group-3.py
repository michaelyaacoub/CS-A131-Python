""" Nalan Pandian and Michael Yaacoub Ch5 Lab 1.2"""
from random import randint


def guessing_game():
    response = "You have the right answer!"
    correct_answer = randint(1, 10)  # 10
    guess = int(input("Guess a number: "))  # 5
    while guess != correct_answer:
        if guess < correct_answer:
            print("Too low.")
            guess = int(input("Guess a number: "))
        if guess > correct_answer:
            print("Too high.")
            guess = int(input("Guess a number: "))

    print(response)


guessing_game()
