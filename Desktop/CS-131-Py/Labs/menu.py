"""
---------------------------------
Name: Michael Yaacoub
Assiginment: Ch 06 LAB 2 Menu Revisited
Date: 03/16/23
---------------------------------
Write a menu program that prompts the user for the name of the restaurant,
and as many dishes (with prices) as they want...
and saves them in a list (or two ?), then displays the finished menu to the screen.

you must use at least one list
you must use at least one function
"""

def menu():
    """ Displays selected menu items and their prices"""
    resturant_name = input("Where are you dinnig? ")
    dish = []
    price = []
    item_menu = 0
    menu = ""
    menu_receipt = ""
    while menu != 'q':
        dish.append(input("Please enter a dish: "))
        price.append(float(input("Please enter dish price: ")))
        menu_receipt += ("Dish: %-18s Price: $%5.2f\n" % (dish[item_menu], price[item_menu]))
        item_menu += 1
        menu = input("if you want to quit, enter q : ")
    print("---------------------" + resturant_name + "---------------------")
    print(menu_receipt)
menu()