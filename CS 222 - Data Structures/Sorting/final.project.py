"""
Name:                   Your Name
Class and Section:	    CS 222 01
Assignment:		        Final Project
Due Date:		        Monday, May 10, 2021 
Date Turned in:         Monday, May 10, 2021 
Program Description:	This program will run benchmarks on three sorting algorithms: Selection Sort,
                        Insertion Sort, and Shell Sort. It will run them with three different sizes 
                        of lists: 100, 1,000 and 10,000 numbers. The benchmarks will print the amount
                        of time that it took for the algorithms to sort the lists, the number of
                        comparisons made and the number of swaps done.

"""
import random
import time

def selectionSort(alist):
    comparisons = 0
    swaps = 0
    for fillslot in range(len(alist) - 1, 0 , -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            comparisons += 1
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        swaps += 1
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return comparisons, swaps

def insertionSort(alist):
    comparisons = 0     
    swaps = 0           
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 :
            comparisons += 1                            # got the condition out of the while loop to count the comparisons
            if (alist[position - 1] > currentvalue):    # since it will not count the comparison when position is < 0                                   
                swaps += 1
                alist[position] = alist[position - 1]
                position -= 1
            else:
                break
        swaps += 1 
        alist[position] = currentvalue
    return comparisons, swaps

def shellSort(alist):
    comparisons = 0 
    swaps = 0       
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
           comparisonsMade, swapsMade =  gapInsertionSort(alist, startPosition, sublistCount)
           comparisons += comparisonsMade
           swaps += swapsMade 
        sublistCount = sublistCount // 2
    return comparisons, swaps

def gapInsertionSort(alist, start, gap):
    comparisons = 0
    swaps = 0
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position >= gap:
            comparisons += 1
            if(alist[position - gap] > currentValue):
                swaps += 1
                alist[position] = alist[position - gap]
                position = position - gap
            else:
                break
        swaps += 1
        alist[position] = currentValue
    return comparisons, swaps

def createList(lenght):
    lyst = list() # || []
    for i in range(lenght):
        lyst.append(random.randrange(1,1000,1))
    random.shuffle(lyst) # Making sure
    return lyst

def copyList(lyst):
    return [ x for x in lyst ] # list comprehension (ch 1)


def benchmarkSort(sortingAlgorythm, lyst, label):
    print(label)
    start = time.time()
    comparisons, swaps = sortingAlgorythm(lyst)
    end = time.time()
    totalTime = end - start
    # print("Sorted:", lyst) # Uncomment this out to output the sorted list
    print("\tNumber of comparisons:", comparisons)
    print("\tNumber of swaps:", swaps)
    print("\tDuration:", totalTime)
    print()

def benchmark(count):
    print("=====> Sorting", count, "items <=====\n")
    lyst = createList(count)
    selectionLyst = copyList(lyst)
    insertionLyst = copyList(lyst)
    shellLyst = copyList(lyst)
    # print("Sorting: ", lyst, "\n") # Uncomment this out to output the list to be sorted
    benchmarkSort(selectionSort, selectionLyst, "Selection Sort:")
    benchmarkSort(insertionSort, insertionLyst, "Insertion Sort:")
    benchmarkSort(shellSort, shellLyst, "Shell Sort:")



def main():
    benchmark(100)
    benchmark(1000)
    benchmark(10000)
    return 0

if __name__ == "__main__":
    main()