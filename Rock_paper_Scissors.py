import random
list=["rock","Paper","Scissors"]
computer_choice=random.choice(list)
user_choice=int(input("Enter your choice: 0 for Rock, 1 for Paper, 2 for Scissors: "))
if(computer_choice>user_choice or computer_choice==0 and user_choice==2):
    print("Computer wins!")
elif(computer_choice==user_choice):
    print("Draw!")
elif(computer_choice<user_choice or computer_choice==2 and user_choice==0):
    print("User wins!")
else:
    print("Invalid input!")