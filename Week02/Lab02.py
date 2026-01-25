import random

choices = ["Rock", "Paper", "Scissors"]

# Minimum 2 users
playerchoice = input(
    "Enter a number between the following list:1=Rock, 2=Paper, 3=Scissors:  "
)

playerchoice = int(playerchoice)


# Input check

if playerchoice < 1 or playerchoice > 3:
    print("Error: You should choose a number between 1 and 3!")
else:
    # Develop the game logic through if/elif/else
    computerChoice = random.randint(1, 3)

    print(playerchoice)
    print(computerChoice)
    
    if playerchoice == computerChoice:
        print("It's a tie!")
    elif playerchoice == 1 and computerChoice == 3:
        print("Rock beats Scissors-Player win")
    elif playerchoice == 2 and computerChoice == 1:
        print("Paper beats Rock-Player win")
    elif playerchoice == 3 and computerChoice == 2:
        print("Scissors beats Paper-Player win")
    else:
        print("Computer Win!")