STATE_RATE = 0.03
COUNTY_RATE = 0.02

propertyValue = float(input("Enter the property value: "))
stateTax = propertyValue * STATE_RATE
countyTax = propertyValue * COUNTY_RATE
totalTax = stateTax + countyTax

print("Property Tax: $" + str(totalTax))
