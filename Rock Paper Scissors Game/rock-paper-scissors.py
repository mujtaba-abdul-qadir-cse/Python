import random

def rockPaperScissors():


    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print()
    print("Please enter your choice:")
    print()

    playersChoice = int(input())

    computersChoice = random.randint(1, 3)

    if playersChoice == computersChoice:
        print("\nIT'S A DRAW!")
        explanation(playersChoice, computersChoice)

    elif playersChoice == 1 and computersChoice == 2:
            print("\nYOU LOSE!!")
            explanation(playersChoice, computersChoice)

    elif playersChoice == 1 and computersChoice == 3:
            print("\nYOU WIN!!")
            explanation(playersChoice, computersChoice)

    elif playersChoice == 2 and computersChoice == 1:
            print("\nYOU WIN!!")
            explanation(playersChoice, computersChoice)

    elif playersChoice == 2 and computersChoice == 3:
            print("\nYOU LOSE!!")
            explanation(playersChoice, computersChoice)

    elif playersChoice == 3 and computersChoice == 1:
            print("\nYOU LOSE!!")
            explanation(playersChoice, computersChoice)

    elif playersChoice == 3 and computersChoice == 2:
            print("\nYOU WIN!!")
            explanation(playersChoice, computersChoice)


    print()
    print("Press enter to return to menu")

    input()


    rockPaperScissors()

def explanation(a, b):
    options = ["Rock", "Paper", "Scissors"]

    print()
    print("You chose: " + options[a - 1])
    print()
    print("Computer chose: " + options[b - 1])


rockPaperScissors()
