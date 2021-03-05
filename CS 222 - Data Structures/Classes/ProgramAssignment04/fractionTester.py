""" 
Name:			        Ruben Nunez
Class and Section:	    CS 222 01
Assignment:		        Program Assignment 03
Due Date:		        Monday, March 8, 2021
Date Turned in:         Friday, March 5, 2021
Program Description:	This program tests the Fraction class with arithmetic and 
                        relational operators. The fraction class takes two arguments,
                        a numerator and a denominator. Since both must be instances of
                        integers, the program will test if the constructor raises an
                        error whenever the value provided is not an integer.
 """

import fraction

def main ():
    print("Fraction Class Tester\n")

    try:
        frac1 = fraction.Fraction(6.5, 9)
        print("Success!", frac1) #If it prints success then the error was not raised
    except ValueError as error:
        print(error)
    try:
        frac1 = fraction.Fraction(6, 9.5)
        print("Success!", frac1)
    except ValueError as error:
        print(error)

    print()

    halfFraction = fraction.Fraction(1, 2)
    frac1 = fraction.Fraction(6, 9)
    frac2 = fraction.Fraction(12, 15)

    print("Addition:")
    sumOfHalves = halfFraction + halfFraction
    print(halfFraction, "+", halfFraction, "=", sumOfHalves) 
    
    print("\nSustraction:")
    sustractionOfHalves = halfFraction - halfFraction
    print(halfFraction, "-", halfFraction, "=", sustractionOfHalves )
    print(frac1, "-", frac2, "=", frac1-frac2 )


    print("\nMultiplication:")
    print(frac1, "x", frac2, "=", frac1 * frac2 )

    print("\nDivision:")
    print(frac2, "/", frac1, "=", frac2 / frac1 )
    
    print("\nEqual:")
    print(frac1, "==", frac1, "?", frac1 == frac1)
    print(frac1, "==", frac2, "?", frac1 == frac2)

    print("\nNot Equal:")
    print(frac1, "!=", frac1, "?", frac1 != frac1)
    print(frac1, "!=", frac2, "?", frac1 != frac2)

    print("\nGreater than:")
    print(frac1, ">", frac1, "?", frac1 > frac1)
    print(frac1, ">", frac2, "?", frac1 > frac2)
    print(frac2, ">", frac1, "?", frac2 > frac1)

    print("\nGreater than or equal to:")
    print(frac1, ">=", frac1, "?", frac1 >= frac1)
    print(frac1, ">=", frac2, "?", frac1 >= frac2)
    print(frac2, ">=", frac1, "?", frac2 >= frac1)

    print("\nLess than:")
    print(frac1, "<", frac1, "?", frac1 < frac1)
    print(frac1, "<", frac2, "?", frac1 < frac2)
    print(frac2, "<", frac1, "?", frac2 < frac1)
    
    print("\nLess than or equal to:")
    print(frac1, "<=", frac1, "?", frac1 <= frac1)
    print(frac1, "<=", frac2, "?", frac1 <= frac2)
    print(frac2, "<=", frac1, "?", frac2 <= frac1)



if __name__ == '__main__':
    main()
    