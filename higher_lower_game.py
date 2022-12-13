import random
import os
from art import *
from game_data import data

# Function to clear the screen
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to begin the game
def play_game():
    game_over = False
    score = 0
    # Randomly selecting first account from the game data and removing it so it doesn't repeat
    account_a = data.pop(random.randint(0, len(data)-1)) # Am using the pop() function in order to avoid the two random selection being the same. The pop() function removes that item from the list after it is selected
    # While loop to allow more comparison
    while not game_over:
        # Randomly selecting second account from the game data and removing it so it doesn't repeat
        account_b = data.pop(random.randint(0, len(data)-1))

        print(logo)

        # Printing current score
        if score > 0:
            print(f"You're right! current score is {score} ")

        # first comparison
        print(f"Compare A: {account_a['name']}, a/an {account_a['description']}, from {account_a['country']} ")
        print(vs)
        print(f"Compare B: {account_b['name']}, a/an {account_b['description']}, from {account_b['country']} ")

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
    # Play again option
    play_again =input("Do you want to play again? Type 'y' for yes or 'n' for no: ").lower()
    if play_again == "y":
        cls()
        play_game()
play_game()
