import os
from Art import logo, vs
import random
from game_data import data


def format_account(account):
    """Format the account data into printable format"""
    account_name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{account_name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    """Take the user guess and follower counts and returns if they got it right"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Display art
print(logo)
score = 0
game_should_continue = True
# Making account at position B become the next account at position 
account_b = random.choice(data)

# Make the game repeatable
while game_should_continue:
    # Generate a random account from the game data.
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_account(account_a)}.")
    print(vs)
    print(f"Compare B: {format_account(account_b)}. ")

    # Ask user for a guess.
    guess = input("Who has more followers? 'A' or 'B' : ").lower()

    # Check if user is correct
    # Get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    # Use if statement to check if user is correct
    # Clear the screen between rounds
    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)
 
    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1
        print(f"you're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score {score}")
