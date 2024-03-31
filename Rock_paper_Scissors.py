import random

# List of choices
list = ["rock", "Paper", "Scissors"]

# Computer makes a random choice
computer_choice = random.choice(list).lower()

# User enters their choice
user_choice = input("Enter your choice: Rock, Paper, or Scissors: ").lower()

# Check if the user entered a valid choice
if user_choice not in list:
    print("Invalid input!")
else:
    # Compare the choices
    if (computer_choice == "rock" and user_choice == "scissors") or \
       (computer_choice == "scissors" and user_choice == "paper") or \
       (computer_choice == "paper" and user_choice == "rock"):
        print("Computer wins!")
    elif (computer_choice == user_choice):
        print("Draw!")
    else:
        print("User wins!")