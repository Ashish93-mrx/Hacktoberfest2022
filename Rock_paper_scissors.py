#simple python game called rock,paper and scissors

import random

user_won = 0
computer_won = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock or Paper or Scissors or Q to quit the game: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    #here  rock= 0, paper= 1, scissors= 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won this time!")
        user_won += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_won += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_won += 1

    else:
        print("You lost!")
        computer_won += 1

print("You won", user_won, "times.")
print("The computer won", computer_won, "times.")
print("okay have a great day!")
