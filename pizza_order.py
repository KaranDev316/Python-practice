print("Welcome to the pizza order")
pizza_size = input("what size of pizza do you want?: ")
price = 0
if pizza_size.lower() == "small":
    print("Price of small pizza is 100")
    price = 100
elif pizza_size.lower() == "medium":
    print("Price of medium pizza is 200")
    price = 200
else:
    print("Price of large pizza is 300")
    price = 300

pepperoni = input("what pepperoni do you want?: ")