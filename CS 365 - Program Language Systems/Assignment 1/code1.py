import functools
import random
import statistics

# Ruben Nunez
# CS 365 - Program Language Systems
# Assignment 1

def prettyPrint(aList):
    # Prints out the numbers in the array in eight lines of 10 evenly spaced numbers
    print("\n".join([" ".join([f"{aList[i + j]:2d}" for j in range(10)]) for i in range(0,len(aList),10)]))

def main ():
    randomNumberList = [random.randint(1,85) for x in range(80)]
    pp = pprint.PrettyPrinter(width=40, compact= True)
    print(" Unsorted Number List")
    prettyPrint(randomNumberList)

    print("\n Sorted Number List")
    randomNumberList.sort()
    prettyPrint(randomNumberList)

    print(f"\nThe smallest number is: {randomNumberList[0]}")
    print(f"The largest number is: {randomNumberList[len(randomNumberList) - 1]}")

    sumOfRandomList = functools.reduce(lambda a, b: a + b, randomNumberList)
    print(f"The sum of the numbers is: {sumOfRandomList}")

    productOfRandomList = functools.reduce(lambda a, b: a * b, randomNumberList)
    print(f"\nThe product of the numbers is: {productOfRandomList}")

    print(f"\nThe mean of the numbers is: {statistics.mean(data = randomNumberList)}")
    print(f"The median of the numbers is: {statistics.median(data = randomNumberList)}")
    print(f"The mode of the numbers is: {statistics.mode(data = randomNumberList)}")
    print(f"The Standard Deviation of the numbers is: {statistics.stdev(data = randomNumberList)}")
    return 0

if (__name__ == "__main__"):
    main()