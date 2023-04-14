"""
---------------------------------------
Name: Michael Yaacoub - Nik Vonessen
Group Assignment: Lab 3.3
Date: 02/14/2023
---------------------------------------
"""


# ------Inputs------
dish_1 = input("What'd would like for your first dish?: ")
dish_price_1 = float(input('Price for first dish? '))


dish_2 = input("How about your second dish?: ")
dish_price_2 = float(input('Price for second dish? '))


dish_3 = input("Great, would you like to add a third?: ")
dish_price_3 = float(input('Price for third dish? '))


dish_4 = input("You got to add a fourth! : ")
dish_price_4 = float(input('Price for fourth dish? '))


dish_5 = input("Anything Else for a fifth?: ")
dish_price_5 = float(input('Price for last dish? '))

# ------Outputs------
print("Dish: %-18s Price: $%5.2f" % (dish_1, dish_price_1))

print("Dish: %-18s Price: $%5.2f" % (dish_2, dish_price_2))

print("Dish: %-18s Price: $%5.2f" % (dish_3, dish_price_3))

print("Dish: %-18s Price: $%5.2f" % (dish_4, dish_price_4))

print("Dish: %-18s Price: $%5.2f" % (dish_5, dish_price_5))

