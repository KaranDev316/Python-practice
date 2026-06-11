import random
user_choice = input("Enter your choice(Rock/Paper/Scissors): ")

choices = ["rock","paper","scissors"]

computer_choice = random.choice(choices)
if user_choice.lower() == "rock" or user_choice.lower() == "paper" or user_choice.lower() == "scissors":
    if user_choice.lower() == computer_choice:
        print("Draw")
    elif user_choice.lower() == "rock" and computer_choice == "scissors":
        print("You won")
    elif user_choice.lower() == "scissors" and computer_choice == "paper":
        print("You won")
    elif user_choice.lower() == "paper" and computer_choice == "rock":
        print("you won")
    else:
        print("YOU LOSE!")
else:
    print("Please enter Rock or Paper or Scissors")