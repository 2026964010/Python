price=int(input("Enter the price of the item: "))
if price > 20000:
    shipping_cost=0
    print("The item is affordable.")
else:
    shipping_cost=3000
    print("The item is not affordable.")
print("Shipping cost=", shipping_cost)

