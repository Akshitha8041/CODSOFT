import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    win_conditions = {
        "rock": "scissors",
        "paper": "rock",
        "scissors": "paper"
    }

    if user_choice == computer_choice:
        return "It's a tie!"
    elif computer_choice == win_conditions[user_choice]:
        return "You win!"
    else:
        return "Computer wins"

