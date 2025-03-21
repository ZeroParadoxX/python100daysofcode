#display art
from art import  logo,vs
from game_data import data
import random


def format_data(account):
    """a Formate the account data into primitive format."""
    account_name = account['name']
    account_descr = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_descr}, from {account_country} "

def check_answer(user_guess,a_follower,b_follower):
    if a_follower > b_follower:
        return user_guess == "a"
    else:
        return user_guess == 'b'

print(logo)
score = 0
# Generate a random acoount from the game data
account_b = random.choice(data)
game_should_continue = True

# ASk user for a gues
while game_should_continue:

    # making account at position b become the next account at position a
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")


    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    print('\n'*20)
    print(logo)
    # check if user is correct

    # - get follower count of each account
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    # -use if statement to check if user is correct
    if is_correct:
        score += 1
        print(f"You're right! current score- {score}")
    else:
        print(f"sorry, that's wrong current score- {score}")
        game_should_continue = False
    # give user feedback on their guess

# score keeping

# make the game repeatable

