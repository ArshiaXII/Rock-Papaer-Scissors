import random
import time

# Define the options
options = ["rock", "paper", "scissors"]

# Define the countdown function
def countdown(n):
    for i in range(n, 0, -1):
        print(i)
        time.sleep(1)
    print("GO!")

# Define the game function
def game():
    # Get player's choice
    print("Choose your option: rock, paper, or scissors?")
    player_choice = input().lower()

    # Make sure player's choice is valid
    while player_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        player_choice = input().lower()

    # Get computer's choice
    computer_choice = random.choice(options)

    # Print the choices
    print(f"\nYou chose {player_choice}.")
    print(f"The computer chose {computer_choice}.\n")

    # Determine the winner
    if player_choice == computer_choice:
        print("It's a tie!")
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("The computer wins!")

# Define the main function
def main():
    # Countdown from 3 seconds
    countdown(3)

    # Start the game
    game()

if __name__ == "__main__":
    main()
