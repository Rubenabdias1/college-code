from llstack import LLStack
""" 
Name:			        Your Name
Class and Section:	    CS 222 02
Assignment:		        Chapter 3B Program
Due Date:		        Friday, April 23, 2021
Date Turned in:         Monday, April 21, 2021
Program Description:	This program tests the stack class that implements 
                        a linked list.
"""
def main():
    pile = LLStack()                                           # stack.__init__()
    print("Is the pile of numbers empty?", pile.isEmpty())     # stack.isEmpty()
    pile.push(1)                                               # stack.push()
    pile.push(2)
    pile.push(3)
    print("Added three numbers: ", pile)                       # stack.__str__()
    print("Popping next number: ", pile.pop())                 # stack.pop()
    pile.push(4)
    pile.push(5)
    print("Added two more numbers: ", pile)
    print("Peeking:", pile.peek())                             # stack.peek()
    print("Is the pile of numbers empty?", pile.isEmpty())
    print("The pile has", pile.size(), "items")                 # stack.size()
    pile.pop()
    pile.pop()
    pile.pop()
    pile.pop()
    print("Popping 4 times. Is the pile of numbers empty?", pile.isEmpty())
    

    return 0

if __name__=="__main__":
    main()