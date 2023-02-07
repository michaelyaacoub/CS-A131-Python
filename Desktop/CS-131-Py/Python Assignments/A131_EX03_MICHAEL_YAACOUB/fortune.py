"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch 03 Exercises - Part B
Date: 02/28/2023
---------------------------------------
Write a fortune telling program either based on the lunar calendar (12-year cycle) or the solar (12-month cycle).
"""


month = int(input("Month: "))
day = int(input("Day: "))

if month > 12 or day > 31 :
    print("Your input is invaild.")
    quit

elif month == 12 and day > 21 and day < 32 or month == 1 and day > 0 and day < 20 :
    print("The Capricornian's animal is the Mountian Sea-Goat and the fortune for today: Keep your eyes open for opportunities!")

elif month == 1 and day > 19 and day < 31 or month == 2 and day > 0 and day < 19 :
    print("The Aquarian's animal is the Water-Bearer and the fortune for today: Keep pushing towards your goals.")

elif month == 2 and day > 18 and day < 30 or month == 3 and day > 0 and day < 21 :
    print("The Piscean's animal is the Fish and the fortune for today: Use it wisely to tackle your tasks.")

elif month == 3 and day > 20 and day < 32 or month == 4 and day > 0 and day < 20 :
    print("The Arien's animal is the Ram and the fortune for today: Take some time to relax and recharge.")

elif month == 4 and day > 19 and day < 31 or month == 5 and day > 0 and day < 20 :
    print("The Taurean's animal is the Bull and the fortune for today: Take risks and be bold.")
    
elif month == 5 and day > 20 and day < 32 or month == 6 and day > 0 and day < 21 :
    print("The Geminian's animal is Snake and fortune for today: The Twins are tired and you would be wise to have an extra cup of coffee.")

elif month == 6 and day > 20 and day < 32 or month == 7 and day > 0 and day < 24 :
    print("The Cancerian's animal is Horse and the fortune for today: Stay focused and don't lose sight of your goals.")


elif month == 7 and day > 22 and day < 31 or month == 8 and day > 0 and day < 23 :
    print("The Leo's animal is the Lion and the fortune for today: Spread kindness and positivity wherever you go.")

elif month == 8 and day > 22 and day < 32 or month == 9 and day > 0 and day < 23 :
    print("The Virgin's animal is the Maiden and the fortune for today: Embrace your inner child and have fun!")

elif month == 9 and day > 23 and day < 31 or month == 10 and day > 0 and day < 23 :
    print("The Libran's animal is the Scales and the fortune for today: Use your skills to tackle your to-do list.")

elif month == 10 and day > 22 and day < 32 or month == 11 and day > 0 and day < 23 :
    print("The Scorpio's animal is Scropion and the fortune for today: Lean on your support system when you need it")

elif month == 11 and day > 22 and day < 31 or month == 12 and day > 0 and day < 22 :
    print("The Sagittarian's animal is the Archer and the fortune for today: Put in the effort and you will be rewarded.")


