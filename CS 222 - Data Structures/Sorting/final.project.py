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
    comparisons = 0     # TODO
    swaps = 0           # TODO
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position -= 1
        alist[position] = currentvalue
    return comparisons, swaps

def shellSort(alist):
    comparisons = 0 # TODO
    swaps = 0       # TODO
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for startPosition in range(sublistCount):
            gapInsertionSort(alist, startPosition, sublistCount)
        sublistCount = sublistCount // 2
    return comparisons, swaps

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        position = i
        while position >= gap and \
              alist[position - gap] > currentValue:
            alist[position] = alist[position - gap]
            position = position - gap
        alist[position] = currentValue

def createList(lenght):
    lyst = list() # || []
    for i in range(lenght):
        lyst.append(random.randrange(1,10,1))
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
    print("Sorted:", lyst)
    print("\tNumber of comparisons:", comparisons)
    print("\tNumber of swaps:", swaps)
    print("\tDuration:", totalTime)
    print()

def benchmark(count):
    print(" ==> Sorting", count, "items\n")
    lyst = createList(count)
    selectionLyst = copyList(lyst)
    insertionLyst = copyList(lyst)
    shellLyst = copyList(lyst)
    print("Sorting: ", lyst)
    benchmarkSort(selectionSort, selectionLyst, "Selection Sort:")
    benchmarkSort(insertionSort, insertionLyst, "Insertion Sort:")
    benchmarkSort(shellSort, shellLyst, "Shell Sort:")



def main():
    benchmark(10)
    benchmark(100)
    benchmark(1000)
    benchmark(10000)
    return 0

if __name__ == "__main__":
    main()