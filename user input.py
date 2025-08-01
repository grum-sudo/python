
item = input ("what item would you like to buy?: ")
price = float(input("what is the price of the item?:"))
quantity = int(input ("many of the item would you like to buy?:"))
total = price * quantity
print(f"you have bought {quantity} x {item}/s")
print (f"your total is ₺{total}")