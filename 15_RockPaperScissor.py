import random

exit = False
usr_pnts = 0
comp_pnts = 0

# def usrWin():
#     print("You Won!!")
#     usr_pnts += 1

# def compWin():
#     print("Computer Won!!")
#     comp_pnts += 1

def tie():
    print("It's a tie!!!.")


while exit == False:
    options = ["rock", "papper", "scissors"]
    usr_inpt = input("Choose, rock, paper, scissors or exit:")
    comp_inpt = random.choice(options)

    if usr_inpt == "exit":
        print("Game ended")
        print(usr_pnts, comp_pnts)
        exit = True

    if usr_inpt == "rock":
        if comp_inpt == "rock":
            print("Your input is Rock.")
            print("Computer input is Rock.")
            tie()
        elif comp_inpt == "paper":
            print("Your input is Rock.")
            print("Computer input is paper.")
            print("Computer Won!!")
            comp_pnts += 1
        elif comp_inpt == "scissor":
            print("Your input is Rock.")
            print("Computer input is scissor.")
            print("You Won!!")
            usr_pnts += 1
    elif usr_inpt == "paper":
        if comp_inpt == "rock":
            print("Your input is paper.")
            print("Computer input is Rock.")
            print("Computer Won!!")
            comp_pnts += 1
        elif comp_inpt == "paper":
            print("Your input is paper.")
            print("Computer input is paper.")
            tie()          
        elif comp_inpt == "scissor":
            print("Your input is paper.")
            print("Computer input is scissor.")
            print("Computer Won!!")
            comp_pnts += 1
    elif usr_inpt == "scissor":
        if comp_inpt == "rock":
            print("Your input is scissor.")
            print("Computer input is Rock.")
            print("Computer Won!!")
            comp_pnts += 1
        elif comp_inpt == "paper":
            print("Your input is scissor.")
            print("Computer input is paper.")
            print("You Won!!")
            usr_pnts += 1
        elif comp_inpt == "scissor":
            print("Your input is scissor.")
            print("Computer input is scissor.")
            tie()
    elif usr_inpt != "rock" or usr_inpt != "paper" or usr_inpt != "scissor":
        print("Invalid Input!!!")