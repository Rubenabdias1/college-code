import random
import time
def bubbleSort(alist):
    compare = 0
    swap = 0
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            compare += 1
            if alist[i] > alist[i + 1]:
                swap += 1
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp
        passnum -= 1
    return compare, swap

def printList(alist):
    count = 0
    for x in range(len(alist)):
        
        if count % 10 == 0:
            print()
        print("%4d" % alist[x], end = " ")
        count += 1

def createList(num):
    lyst = []
    for x in range(num):
        lyst.append(x)
    random.shuffle(lyst)
    return lyst

def main():
    count = 100
    while count <= 10000:
        lyst = createList(count)
        start = time.time()
        compare, swap = bubbleSort(lyst)
        end = time.time()
        totalTime = end - start
        print("Count =", count)
        print("Comparisons:", compare)
        print("Swaps:", swap)
        print("Time:", totalTime)
        count = count * 10

main()
    
