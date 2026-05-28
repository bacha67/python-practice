import random

# player choice
choice = input("Choose (r/p/s): ").lower()

# validation
if choice not in ("r", "p", "s"):
    print("Invalid choice")

else:

    # computer choice
    computer = random.computer = random.choice(["r", "p", "s"])
    print("Computer chose:", computer)

    # tie
    if choice == computer:
        print("It's a tie!")

    # player wins
    elif (
        (choice == "r" and computer == "s") or
        (choice == "p" and computer == "r") or
        (choice == "s" and computer == "p")
    ):
        print("You win!")

    # computer wins
    else:
        print("Computer wins!")