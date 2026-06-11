import random
user_choice = input("Enter your choice(Rock/Paper/Scissors): ").lower()

choices = ["rock","paper","scissors"]

computer_choice = random.choice(choices)
if user_choice == "rock" or user_choice == "paper" or user_choice == "scissors":
    if user_choice == computer_choice:
        print("Draw")
    elif user_choice == "rock" and computer_choice == "scissors":
        print("YOU WON")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("YOU WON")
    elif user_choice == "paper" and computer_choice == "rock":
        print("YOU WON")
    else:
        print("YOU LOSE!")
else:
    print("Please enter Rock or Paper or Scissors")