"""
Name:                   Ruben Nunez
Class and section:      CS 120 01
Assignment:             Program Assignment 06
Due Date:               Wednesday, April 8, 2020
Date Turned in:         Sunday, April 5, 2020
Program Description:    This program asks the user for multiple sales amounts
                        then calculates and displays the total amount of state
                        sales tax, county sales tax and the total amount of sale
                        taxes from those inputs.
"""

STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.025

print(" -  Sales Tax Calculator  - ")

def read():
    amount = 0
    sale = "loopInitiator"
    while sale != 0:
        sale = int(input("Enter a sale amount ( enter 0 to quit ): "))
        amount += sale
    return amount

def stateTaxCalc(sale): return sale * STATE_TAX_RATE

def countyTaxCalc(sale): return sale * COUNTY_TAX_RATE

def totalTaxCalc(sale):
    return stateTaxCalc(sale) + countyTaxCalc(sale)

def calculate(salesAmount):
    
    # Returns a dictionary that contains the state sales tax, county sales
    # tax and the total amount of sales tax from the sale amount.
    
    totalSalesTax = {"stateTax":0, "countyTax":0, "totalTax":0}
    
    totalSalesTax["stateTax"] = stateTaxCalc(salesAmount) 
    totalSalesTax["countyTax"] = countyTaxCalc(salesAmount)
    totalSalesTax["totalTax"] = totalTaxCalc(salesAmount)
    
    return totalSalesTax

def printTaxTable(salesTax):
    
    print("\nCounty Sales Tax | State Sales Tax |  Total Sales Tax")
    
    stateTax = "$%.2f" % salesTax["stateTax"]
    countyTax = "$%.2f" % salesTax["countyTax"]
    totalTax = "$%.2f" % salesTax["totalTax"]

    print("%16s" % stateTax + " |%16s" % countyTax + " |%17s" % totalTax)


def main():
    totalSales = read()
    totalSalesTaxes = calculate(totalSales)
    printTaxTable(totalSalesTaxes)
            
if __name__ == "__main__":
    main()
