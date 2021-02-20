PRICE = 99.0

quantity = int(input("Quantity of packages purchased: "))
if quantity < 10:
    discount = 0
elif quantity <= 19:
    discount = 0.1
elif quantity <= 49:
    discount = 0.2
elif quantity <= 99:
    discount = 0.3
else:
    discount = 0.4

total = quantity * PRICE
discountAmount = discount * total
salesPrice = total - discountAmount

if discount > 0:
    print("Discount amount:", discountAmount, "(", str(int(discount * 100)) + "% )")
print("Sales Price:", salesPrice)
