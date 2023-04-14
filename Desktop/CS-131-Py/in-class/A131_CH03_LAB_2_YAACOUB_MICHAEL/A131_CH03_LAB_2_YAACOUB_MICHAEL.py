""" ---------------------------------------
Name: Michael Yaacoub
Group Ch.03 - Lab 2
Date: 02/24/2023
--------------------------------------- """

"""
Write a program that creates a menu with up to five(5) items: 
- Ask the user for the name of each dish and the price
- Give the user an option to either ask again or quit
- After the user quits, format the output to display the dish name on the left and the price on the right
"""

dish = input("Please enter a dish or (enter q to quit): ")
if dish == 'q' :
    quit
    print("quited")
elif dish != 'q' :
    price = float(input("Please enter dish price: "))
    dish_1 = input("Please enter a dish or (enter q to quit): ")
    if dish_1 == 'q' :
        quit
        print("Dish: %-18s Price: $%5.2f" % (dish, price))
    elif dish_1 != 'q' :
        price_1 = float(input("Please enter dish price: "))
        dish_2 = input("Please enter a dish or (enter q to quit): ")
        if dish_2 == 'q' :
            quit
            print("Dish: %-18s Price: $%5.2f" % (dish, price))
            print("Dish: %-18s Price: $%5.2f" % (dish_1, price_1))
        elif dish_2 != 'q' :
            price_2 = float(input("Please enter dish price: "))
            dish_3 = input("Please enter a dish or (enter q to quit): ")
            if dish_3 == 'q' :
                quit
                print("Dish: %-18s Price: $%5.2f" % (dish, price))
                print("Dish: %-18s Price: $%5.2f" % (dish_1, price_1))
                print("Dish: %-18s Price: $%5.2f" % (dish_2, price_2))
            elif dish_3 != 'q' :
                price_3 = float(input("Please enter dish price: "))
                dish_4 = input("Please enter a dish or (enter q to quit): ")
                if dish_4 == 'q' :
                    quit
                    print("Dish: %-18s Price: $%5.2f" % (dish, price))
                    print("Dish: %-18s Price: $%5.2f" % (dish_1, price_1))
                    print("Dish: %-18s Price: $%5.2f" % (dish_2, price_2))
                    print("Dish: %-18s Price: $%5.2f" % (dish_3, price_3))
                elif dish_4 != 'q' :
                    price_4 = float(input("Please enter dish price: "))
                    print("Dish: %-18s Price: $%5.2f" % (dish, price))
                    print("Dish: %-18s Price: $%5.2f" % (dish_1, price_1))
                    print("Dish: %-18s Price: $%5.2f" % (dish_2, price_2))
                    print("Dish: %-18s Price: $%5.2f" % (dish_3, price_3))
                    print("Dish: %-18s Price: $%5.2f" % (dish_4, price_4))
