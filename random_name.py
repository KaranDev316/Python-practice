import random

names = (input("Enter everybody's name separated by a comma: ")).split(",")
random_name = random.choice(names)
print(f"{random_name} will pay the bill")


