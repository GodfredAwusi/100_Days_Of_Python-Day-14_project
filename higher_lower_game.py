import random
import os
from art import *
from game_data import data

# Function to clear the screen
def cls():
    """This clears the console and it's cross-platform"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to play the game
def play_game():
    game_over = False
    score = 0

    # Randomly selecting first two accounts for comparison and also removing them so they don't repeat
    account_a = data.pop(random.randint(0, len(data)-1))
    account_b = data.pop(random.randint(0, len(data)-1))

    while not game_over:
        print(logo)
        # Printing current score if the user has actually scored a point or more
        if score > 0:
            print(f"You're right! current score is {score} ")

        # Printing the first comparison
        print(f"Compare A: {account_a['name']}, a/an {account_a['description']}, from {account_a['country']} ")
        print(vs)
        print(f"Compare B: {account_b['name']}, a/an {account_b['description']}, from {account_b['country']} ")
        # User's answer input
        choice = input("Who has the more followers! Type 'A' or 'B': ").lower()

        # Checking the answer
        if choice == "a" and account_a["follower_count"] > account_b["follower_count"]:
            cls()
            score += 1
        elif choice == "b" and account_b["follower_count"] > account_a["follower_count"]:
            cls()
            score += 1
        else:
            game_over = True
            cls()
            print(logo)
            print(f"Sorry, that's wrong. Final score is {score} ")

        # Making account_b the next account_a
        account_a = account_b
        # The next account_b
        account_b = data.pop(random.randint(0, len(data)-1))
    # Play again option
    play_again =input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
    if play_again == "y":
        cls()
        play_game()
play_game()
