#Create a minigame of rock,paper,scissors
#Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock
#The game will be played against the computer
#The user will input their choice and notified if they enter an invalid option
#The computer will randomly select a choice
#The winner will be displayed on the screen whether the user won, lost or tied
#The user will be able to play again or exit the game
#The user will be able to see their score
#Game should be able to handle invalid inputs and putting inputs into lowercase if needed

import random

def game():
    user_score = 0
    computer_score = 0
    while True:
        print("Welcome to Rock, Paper, Scissors! ")
        
        user_choice = input("Enter your choice (rock, paper, scissors): ")
        user_choice = user_choice.lower()
        
        #Computer choice
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        
        #Check for valid inputs
        if user_choice not in choices:
            print("Invalid input, please try again")
            continue
        
        print(f"\nYou chose {user_choice}, the computer chose {computer_choice}.\n")
        
        #Determine winner
        if user_choice == computer_choice:
            print(f"Both players selected {user_choice}. It's a tie!")
        elif user_choice == "rock":
            if computer_choice == "scissors":
                print("Rock smashes scissors! You win!")
                user_score += 1
            else:
                print("Paper covers rock! You lose.")
                computer_score += 1
        elif user_choice == "paper":
            if computer_choice == "rock":
                print("Paper covers rock! You win!")
                user_score += 1
            else:
                print("Scissors cuts paper! You lose.")
                computer_score += 1
        elif user_choice == "scissors":
            if computer_choice == "paper":
                print("Scissors cuts paper! You win!")
                user_score += 1
            else:
                print("Rock smashes scissors! You lose.")
                computer_score += 1
        
        print(f"\nYou have {user_score} points, the computer has {computer_score} points.\n")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Thanks for playing!")
            break

game()