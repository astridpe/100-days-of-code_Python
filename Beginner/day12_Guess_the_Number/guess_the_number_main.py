# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
from random import randint

print(logo)

# Global variables:
LEVEL_EASY_TURNS = 10
LEVEL_HARD_TURNS = 5


# Velger vansklighetsgrad:
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return LEVEL_EASY_TURNS
    else:
        return LEVEL_HARD_TURNS


def guess_number(random_number, user_guess, attempts):
    if user_guess == random_number:
        print(f"You got it! The answer was {random_number}.")
    elif user_guess < random_number:
        print("Too low.")
        return attempts - 1
    else:
        print("Too high.")
        return attempts - 1


def game():
    # Printer velkomstmelding:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    # Finner et nummer som skal gjettes mellom 1 og 100:
    random_number = randint(1, 100)

    attempts = set_difficulty()

    user_guess = 0
    while user_guess != random_number:

        print(f"You have {attempts} attempts remaining to guess the number.")
        user_guess = int(input("Make a guess: "))
        attempts = guess_number(random_number, user_guess, attempts)

        if attempts == 0:
            print(f"You've run out of guesses, you lose. The number was: {random_number}")
            return
        elif user_guess != random_number:
            print("Guess again")


game()