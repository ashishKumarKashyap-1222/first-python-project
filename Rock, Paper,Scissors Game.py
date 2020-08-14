import random """this will import random function which provides random value"""

a = ["rock", "paper", "scissors"]
computer_won = 0
user_won = 0
while True:
    user_choice = input("please enter your choice,choose any one from the following Rock, Paper or scissors: ")
    computer_choice = random.choice(a)
    if user_choice == "rock" and computer_choice == "rock":
        print("try again")
    elif user_choice == "rock" and computer_choice == "paper":
        print("opps! computer won this chance")
        computer_won += 1
    elif user_choice == "rock" and computer_choice == "scissors":
        print("congratulation! you won this chance")
        user_won+=1
    elif user_choice == "paper" and computer_choice == "paper":
        print("try again")
    elif user_choice == "paper" and computer_choice == "scissors":
        print("opps! computer won this chance")
        computer_won += 1
    elif user_choice == "paper" and computer_choice == "rock":
        print("congratulation! you won this chance")
        user_won += 1
    elif user_choice == "scissors" and computer_choice == "scissors":
        print("try again")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("opps! computer won this chance")
        computer_won += 1
    elif user_choice == "scissors" and computer_choice == "rock":
        print("congratulation! you won this chance")
        user_won += 1
    else:
        print("invalid input")
    print("total no of games user won:", user_won)
    print("total no of game computer won:", computer_won)
