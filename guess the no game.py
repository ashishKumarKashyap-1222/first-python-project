import random
a = random.randint(0, 100)
no_of_chances = 10
total_correct_answers = 0
while True:
    while no_of_chances > 0:
        input_no = int(input("please enter your no: "))
        if input_no == a:
            print("congratulation! You have guessed the correct no")
            total_correct_answers=total_correct_answers+1
            print("total no pf correct ans",total_correct_answers)
            play_again = int(input("do you want to play again \n pres 1 for yes\n 2 for no"))
            if play_again == 1:
                continue
            elif play_again == 2:
                break
            break
        else:
            if input_no < a:
                print("your given input is less than the no. Try again!")
                no_of_chances = no_of_chances - 1
            elif input_no > a:
                print("your given input is grater than the no. try again!")
                no_of_chances = no_of_chances - 1
            print(no_of_chances, "no of guesses you took")
            print(10 - no_of_chances, "no of guesses left")
        if no_of_chances == 0:
            print("you have exceed the limit of guessing the no \n GAME OVER!")
print("thank you for playing this game. have a great day.")




