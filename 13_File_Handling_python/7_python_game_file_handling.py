from random import choice
from datetime import datetime
import os
import csv

choices = ["stone", "paper", "scissors"]
rules = {"stone":"scissors","scissors": "paper", "paper": "stone"}
summary = {
    "time":"",
    "total": 0,
    "wins":0,
    "losses":0,
    "draws":0,
    "choices":[]
}

def determine_winner(user, computer):
    if user == computer:
        return "Draw"
    return "User Win" if rules[user] == computer else "Computer Win"

def get_user_choice():
    while True:
        user = input("Enter Stone, Paper, or Scissors: ").strip().lower()
        if user in choices:
            return user
        print("Invalid choice. Try again.")

def game():
    user = get_user_choice()
    computer = choice(choices)
    result = determine_winner(user, computer)
    print(f"You: {user.capitalize()} | Computer: {computer.capitalize()} -> {result}")
    return result, user

def update_stats(result, user):
    """ This function takes result from game and update stats inside summary dictionary based on result """

    summary["total"] += 1
    summary['choices'].append(user)
    summary["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if result == "User Win":
        summary["wins"] += 1
    elif result == "Computer Win":
        summary["losses"] += 1
    else:
        summary["draws"] += 1

def print_summary():
    # Step 3: Show game summary
    print("\n===== GAME SUMMARY ==========")
    print(f"Total Games   : {summary['total']}")
    print(f"Wins          : {summary['wins']}")
    print(f"Losses        : {summary['losses']}")
    print(f"Draws         : {summary['draws']}")
    print(f"Choices       : {summary['choices']}")
    print("================================")

def update_file():
    FILE_NAME = "results.csv"
    FIELD_NAMES = ["time","total", "wins","losses","draws","choices"]
    file_exists = os.path.isfile(FILE_NAME)

    with open(FILE_NAME, 'a', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELD_NAMES)
        if not file_exists:
            writer.writeheader()
        writer.writerow(summary)

if __name__ == "__main__":
    while True:
        result, user = game()
        update_stats(result, user)
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print_summary()
            update_file()
            break