#Number Guessing Game Objectives:

# Include an ASCII art logo.

from art import logo_number_guessing
import random

print(logo_number_guessing)


# Allow the player to submit a guess for a number between 1 and 100.
def number_guessing_game():
    turns = 5
    while turns > 0:
        guess = int(input("Guess a number between 1 and 10\n"))
        print(guess)

        # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.

        i = random.randint(1, 5)
        #print (i)
        if guess > i:
            print("Too high")
        elif guess < i:
            print("Too low")
            # If they got the answer correct, show the actual answer to the player.
        elif guess == i:
            print(f"You got it! The answer was {i}")

            # Track the number of turns remaining.
        turns -= 1
        print(turns)
        # If they run out of turns, provide feedback to the player.
        if turns == 0:
            print("You've run out of guesses, you lose.")
        # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).


print("Exiting")
number_guessing_game()
