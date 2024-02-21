from art import logo_lower_higher
import random
from lower_higher_gamedata import data
print(logo_lower_higher)

def lower_higher_game():
    contenderA = random.choice(data)
    contenderB = random.choice(data)
    print(f"which has higher instagram followers: {contenderA['name']} or {contenderB['name']}")
    choice = input("just type h for higher or l for lower\n")

    if contenderA['follower_count'] > contenderB['follower_count'] and choice == "h":
        print("Correct!")
        lower_higher_game() #recursion
    elif contenderA['follower_count'] > contenderB['follower_count'] and choice == "l":
        print("Wrong!")
        new_choice = input("type y to play again or type n to quit\n")
        if new_choice == "y":
            lower_higher_game() #recursion

    elif contenderA['follower_count'] < contenderB['follower_count'] and choice == "h":
        print("Wrong!\nwould you like to play again?")
        new_choice = input("type y to play again or type n to quit\n")
        if new_choice == "y":
            lower_higher_game() #recursion
    elif contenderA['follower_count'] < contenderB['follower_count'] and choice == "l":
        print("Correct!")
        lower_higher_game() #recursion
    else:
        print("wrong entry")
        new_choice = input("type y to play again or type n to quit\n")
        if new_choice == "y":
            lower_higher_game() #recursion
        lower_higher_game()
lower_higher_game()
