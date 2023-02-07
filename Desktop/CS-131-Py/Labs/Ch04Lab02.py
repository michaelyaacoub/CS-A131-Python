"""
---------------------------------------
Name: Michael Yaacoub
Assignment: Ch.04 - Lab 2
Date: 02/28/2023
---------------------------------------
Write a program that creates a menu with up to five(5) items:
- Using a loop
- Ask the user for the name of each dish and the price
- Give the user an option to either ask again or quit
- After the user quits, format the output to display the dish name on the left and the price on the right
"""

item_menu = 0
menu = ""
dish = ""
price = 0.0
while menu != 'q' :
    dish = input("Please enter a dish or (enter q to quit): ")
    item_menu += 1
    if dish == 'q' :
        break
        print(menu)
    price = float(input("Please enter dish price: "))
    menu += ("Dish: %-18s Price: $%5.2f\n" % (dish, price))
print("********Items Ordered:********")
print(menu)    
