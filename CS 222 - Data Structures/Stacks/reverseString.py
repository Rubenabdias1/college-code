""" 
    Write a function named reverseString that accepts a Stack object and a string.  
    The function should use the Stack to return the string in reverse.  
    For example, if you passed “This is a test” to the function, it should return “tset a si sihT”.
"""
import stack

def reverseString(stack, string):
    for character in string:
        stack.push(character)
    
    reversedString = ""

    while not stack.isEmpty():
        reversedString += stack.pop()

    return reversedString

def main():
    letters = stack.Stack()
    reversedString = reverseString(letters,'This is a test')
    print(reversedString)

if __name__ == "__main__":
    main()