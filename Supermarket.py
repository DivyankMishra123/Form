#Creating shopping cart
print("-----Welcome to Divyank SuperMarket----")

foods=[]
prices=[]
total=0
while True:
    food=input("Write down your order please(press 'q' for quit):")
    if food == "q":
        break
    else:
        price=float(input("The price of " + food + " is: $"))
        foods.append(food)
        prices.append(price)

#Add to cart
print("---YOUR CART---")
for food in foods:
    print(food)
for price in prices:
    total+=price
print(f"Your total bill is ${total}")