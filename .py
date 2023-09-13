print("Welcome to the Simple Shopping Cart!")
cart = []
for i in range(3):
    item = input("enter item: ")
    cart.append(item)
for items in cart:
    print(items)
print(len(cart))
remove = input("Enter the index of the item to remove ")
cart.remove(remove)
print(cart)
print(len(cart))
total_price = 0
for item in cart:
    price = float(input(f"Enter the price for '{item}': "))
    total_price += price

print(f"Total price for items in the cart: {total_price}")