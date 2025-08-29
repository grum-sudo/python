foods =  []# i dont really understand ts like why [] and not {} or ()
prices = []
total = 0

while True:
    food = input("enter what you want buy: (q quit)")
    if food.lower() == "q":
        break
    else:
        price = float(input("enter the price: "))
        foods.append(food)
        prices.append(price)

print("---- YOUR CART ----")

for food in foods:
    print (food)

for price in prices:
    total += price

print(f"you total is ${total}")#the python tut said to add empty print but i dont wanna and it doesnt even matter