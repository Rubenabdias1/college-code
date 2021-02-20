"""
Name:                   Ruben Nunez
Class and section:      CS 120 01
Assignment:             Program Assignment 02, Chapter 02
Program Description:    This program asks the user for the price of the food then
                        calculates the total amount of a meal purchased at a
                        restaurant.
"""

TIP_PERCENTAGE = 18
SALES_TAX = 7

mealPrice = int(input("Enter the price of the meal in dolars: "))
tip = mealPrice * TIP_PERCENTAGE / 100
tax = mealPrice * SALES_TAX / 100
total = mealPrice + tax + tip
print("\nSubtotal: $" + str(mealPrice))
print("Tax:      $" + str(tax))
print("Tip:      $" + str(tip))
print("Total:    $" + str(total))
