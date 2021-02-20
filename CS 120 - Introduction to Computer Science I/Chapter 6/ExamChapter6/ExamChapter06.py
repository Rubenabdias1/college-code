"""
Name:                   Ruben Nunez
Class and section:      CS 120 01
Assignment:             Performance Exam Chapter 06
Program Description:    This program displays a menu of items. Then asks the
                        user for the amount of each menu item it wishes to
                        order, then calculates and displays the cost of every
                        item and the total cost of its order.
                        
"""
PRICE_PER_PIZZA = 1.75
PRICE_PER_FRIE = 2.00
PRICE_PER_DRINK = 1.25

print(" -         Menu        - ")
print("%-19s%5s" % ("Pizza Slices", "$%0.2f" % PRICE_PER_PIZZA))
print("%-19s%5s" % ("Fries", "$%0.2f" % PRICE_PER_FRIE))
print("%-19s%5s" % ("Soft Drinks", "$%0.2f" % PRICE_PER_DRINK))
print("")

def readPizza():
    quantity = int(input("How many pizza slices would you like?: "))
    return quantity

def readFries():
    quantity = int(input("How many fries would you like?: "))
    return quantity

def readSoftDrinks():
    quantity = int(input("How many soft drinks would you like?: "))
    return quantity

def calculateCost(item, prize):
    return item * prize

def totalCost(price1, price2, price3):
    return price1 + price2 + price3

def main():
    order = {}
    order["Pizza Slices"] = [readPizza()]
    order["Fries"] = [readFries()]
    order["Soft Drinks"] = [readSoftDrinks()]
    
    pricePizza = calculateCost(order["Pizza Slices"][0], PRICE_PER_PIZZA)
    priceFries = calculateCost(order["Fries"][0], PRICE_PER_FRIE)
    priceDrinks = calculateCost(order["Soft Drinks"][0], PRICE_PER_DRINK)
    total = totalCost(pricePizza, priceFries, priceDrinks)

    order["Pizza Slices"].append(pricePizza)
    order["Fries"].append(priceFries)
    order["Soft Drinks"].append(priceDrinks)

    print("\n%-14s%8s%15s" % ("ITEM","QUANTITY","PRICE"))
    for item in order:
        order[item][1] = "$%0.2f" % order[item][1]
        print("%-14s%8d%15s" % (item, order[item][0], order[item][1]))
    print("%-22s%15s" % ("TOTAL", "$%0.2f" % total))
            
if __name__ == "__main__":
    main()
