"""
Name:                   Ruben Nunez
Class and section:      CS 120 01
Assignment:             Program Assignment 04, Chapter 04
Program Description:    This program asks the user if they want to encrypt or
                        decrypt a message. Then, using the Ceasar Cypher, the
                        program encrypts the plaintext into an encrypted set of
                        characters. Or decrypts the input with the key that the
                        user provided.
"""

keepGoing = "no"
while keepGoing != "yes":
    
    action = ""
    while True:
        action = input("\nWould you like to encrypt or decrypt? (Enter the action): ")
        if action != "encrypt" and action != "decrypt":
            print("Invalid action\n")
        else:
            break

    text = input("Enter the text to " + action + ": ")
    key  = int(input("Enter the encryption key: "))

    result = ""
    charDifference = ord("~") - ord(" ") + 1
    if action == "encrypt":
        for char in text:
            cypher = ord(char) + key
            while cypher > 126:     #In case the key is greater than 94
               cypher -= charDifference
            result += chr(cypher)
    elif action == "decrypt":
        for char in text:
            cypher = ord(char) - key
            while cypher < 32:      #In case the key is less than 33
                cypher += charDifference
            result += chr(cypher)

    print("The " + action + "ed value is", result)

    keepGoing = input("Would you like to exit the program? (Enter yes to quit): ")
