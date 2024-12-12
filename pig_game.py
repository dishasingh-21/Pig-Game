#Firstly, we need to figure out a way to roll the dice. We are gonna use a random no. generator which will generate numbers between 1-6.
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll

'''
value = roll()
print(value)             #This block of code can be used to observe, actually, rolling of the dice.
'''

#Asking the number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():  #isdigit() will tell us if it is a valid whole number or not.
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4.")
    
    else:
        print("Invalid, try again.")

# print(players)
max_score = 50
player_scores = [0 for _ in range(players)]  #This list will contain individual scores.

# print(player_scores)

#PLAYER TURNS
while max(player_scores) < max_score:

    for player_index in range(players):
        print(f"\nPlayer {player_index + 1}'s turn has just started.\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a {value}. ")
    
            print(f"Your score is: {current_score}")
        player_scores[player_index] += current_score
        print(f"Your total score is: {player_scores[player_index]}")
winning_score = max(player_scores)
winner = player_scores.index(winning_score)
print(f"GAME OVER!\nPlayer {winner + 1} is the winner.")






