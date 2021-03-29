import stock;
""" 
Name:			        Ruben Nunez
Class and Section:	    CS 222 01
Assignment:		        Extra Credit Chapter 01
Due Date:		        Friday, March 19, 2021
Date Turned in:         Friday, March 19, 2021
Program Description:    This program asks the user for a company's stock name,
                        symbol, previous closing price and current price. Then,
                        it prints out the company's stock info. Finally, it changes
                        the stock's previous closing price and sets the new price to
                        0.0028, and prints out the modifications.

"""
def main():
    name = input("Enter the stock's name: ")
    symbol = input("Enter the stock's symbol: ")
    previousClosingPrice = float(float(input("Enter the stock's previous closing price: ")))
    currentPrice = float(input("Enter the stock's price: "))
    vgid = stock.Stock(symbol, name, previousClosingPrice, currentPrice)
    
    print(vgid)
    vgid.setPreviousClosingPrice(vgid.getCurrentPrice())
    vgid.setCurrentPrice(0.0028)
    print()
    print(vgid)

if __name__ == "__main__":
    main();