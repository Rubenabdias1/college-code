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
    if action == "encrypt":
        for char in text:
            cypher = ord(char)  - 96
            cypher = (cypher + key) % 26
            result += chr(cypher + 96 )
    elif action == "decrypt":
        for char in text:
            cypher = ord(char) - 96
            cypher = (cypher - key) % 26
            result += chr(cypher + 96)

    print("The " + action + "ed value is", result)

    keepGoing = input("Would you like to exit the program? (Enter yes to quit): ")
