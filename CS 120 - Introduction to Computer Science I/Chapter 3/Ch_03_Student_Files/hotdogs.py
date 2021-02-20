HD_PER_PACK = 10
BUN_PER_PACK = 8

leftoversHD = 0
leftoversBun = 0

numPeople = int(input("Enter the number of people attending: "))
hdPerPerson = int(input("Enter the number of hot dogs per person: "))

hotdogsNeeded = numPeople * hdPerPerson

hdPackages = hotdogsNeeded // HD_PER_PACK
extraHD = hotdogsNeeded % HD_PER_PACK

if extraHD > 0 :
    hdPackages += 1
    leftoversHD = HD_PER_PACK - extraHD

print("Number of hot dog packages:", hdPackages)
print("Number of hot dogs left over:", leftoversHD)

bunPackages = hotdogsNeeded // BUN_PER_PACK
extraBun = hotdogsNeeded % BUN_PER_PACK

if extraBun > 0 :
    bunPackages += 1
    leftoversBun = BUN_PER_PACK - extraBun

print("Number of hot dog packages:", bunPackages)
print("Number of hot dogs left over:", leftoversHD)


