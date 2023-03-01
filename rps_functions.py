import random


# user picks RPS and convert to number
def get_user_input():
    answer = input("Choose Rock, Paper or Scissors by entering r, p or s:")

    if answer == "r":
        user_num = 0
        print("You picked Rock")
    elif answer == "p":
        user_num = 1
        print("You picked Paper")
    elif answer == "s":
        user_num = 2
        print("You picked Scissors")

    return user_num


#Computer picks random num and RPS
def computer_choice ():
    com_num = random.randint(0,2)

    if com_num == 0:
        print("Computer picked Rock")
    elif com_num == 1:
        print("Computer picked Paper")
    elif com_num == 2:
        print("Computer picked Scissors")

    return com_num


# Function for Winner
def winner():
    if user_input == computer:
        print("Draw")
    else:
        user_win = False
        if user_input == 0 and computer == 2:
            user_win = True
        if user_input == 1 and computer == 0:
            user_win = True
        if user_input == 2 and computer == 1:
            user_win = True

        if user_win == True:
            print("You win")
        else:
            print("Computer Wins")



playing = True
#start while loop
while playing is True:
    user_input = get_user_input()

    computer = computer_choice()

    winner()

    #stop while loop
    quit = input("Press enter to continue or q to quit: ")
    if quit == "q":
        playing = False
        print("Goodbye")