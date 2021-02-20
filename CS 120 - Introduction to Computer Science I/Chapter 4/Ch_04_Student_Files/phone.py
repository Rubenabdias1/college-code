alphaPhoneNumber = input("Enter the telephone number in " \
                         "the format XXX-XXX-XXXX: ")
numPhoneNumber = ''

for ch in alphaPhoneNumber:
    if ch.isalpha():
        ch = ch.upper()
        if ch == 'A' or ch == 'B' or ch == 'C':
            ch = '2'
        elif ch == 'D' or ch == 'E' or ch == 'F':
            ch = '3'
        elif ch == 'G' or ch == 'H' or ch == 'I':
            ch = '4'
        elif ch == 'J' or ch == 'K' or ch == 'L':
            ch = '5'
        elif ch == 'M' or ch == 'N' or ch == 'O':
            ch = '6'
        elif ch == 'P' or ch == 'Q' or ch == 'R' or ch == 'S':
            ch = '7'
        elif ch == 'T' or ch == 'U' or ch == 'V':
            ch = '8'
        elif ch == 'W' or ch == 'X' or ch == 'Y' or ch == 'Z':
            ch = '9'
    numPhoneNumber += ch
print("The phone number is", numPhoneNumber)
