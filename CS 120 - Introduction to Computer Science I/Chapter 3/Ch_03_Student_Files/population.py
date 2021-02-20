population = int(input("Starting pupulation: "))
increase = float(input("Growth increase: "))
decrease = float(input("Decrease rate: "))
numDays = int(input("Number of days to run: "))

days = 1
averageIncrease = increase / 100.0
averageDecrease = decrease / 100.0
print("%-8s%-22s" % ("Day", "Aproximate Population"))
"""
for day in range(1, numDays + 1):
    print("%-8d%10.5f" % (day, population))
    population *= (1 + averageIncrease)
    population *= (1 - averageDecrease)
"""
while population > 1 and days < numDays:
    print("%-8d%10.5f" % (days, population))
    population *= (1 + averageIncrease)
    population *= (1 - averageDecrease)
    days += 1;
    
