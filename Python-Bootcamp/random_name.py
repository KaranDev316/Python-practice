import random

names = (input("Enter everybody's name separated by a comma: ")).split(",")

random_int = random.randint(0, len(names)-1)

random_name = names[random_int]
print(f"{random_name} will pay the bill")


