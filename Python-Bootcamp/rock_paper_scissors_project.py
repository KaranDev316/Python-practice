import random
user_choice = input("Enter your choice(Rock/Paper/Scissor): ")

choices = ["rock","paper","scissors"]

computer_choice = random.choice(choices)

print(computer_choice)