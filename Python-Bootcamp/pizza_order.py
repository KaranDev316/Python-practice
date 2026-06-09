print("Welcome to the pizza order")
pizza_size = input("what size of pizza do you want? (small/medium/large): ")
price = 0
is_small = False
if pizza_size.lower() == "small":
    print("Price of small pizza is 100")
    price = 100
    is_small = True
elif pizza_size.lower() == "medium":
    print("Price of medium pizza is 200")
    price = 200

else:
    print("Price of large pizza is 300")
    price = 300


pepperoni = input("what pepperoni do you want (yes/no)?: ")
if pepperoni.lower() == "yes":
    if is_small:
        price = price + 30
    else:
        price = price + 50
cheese = input("Do you want extra cheese (yes/no)?: ")
if cheese.lower() == "yes":
    price = price + 20
print(f"Total price is {price}")
