# To do:
# 1. 1 Import Logo and print it
from art import logo

# 1. 2 Import the game_data and make it a global variable
from game_data import data

# 1. 3 Import the random-library and clear from repplit
import random
from replit import clear

print(logo)

CANDIDATE_DICTIONARY = data


# 2. Make a function that picks a random candidate from the game-data
def pick_candidate(candidate_dictionary):
    candidate = random.choice(candidate_dictionary)
    return candidate


# 3. make a function that prints the candidates name, description and country
def print_candidate(candidate):
    name = candidate["name"]
    description = candidate["description"]
    country = candidate["country"]
    return f"{name}, {description}, from {country}."


def compare_candidates(candidateA, candidateB, user_choice):
    followersA = int(candidateA["follower_count"])
    followersB = int(candidateB["follower_count"])

    if user_choice == "a":
        if followersA > followersB:
            return True
        else:
            return False
    else:
        if followersB > followersA:
            return True
        else:
            return False


def game():
    # For at man skal kunne holde på B-kandidaten fra forrige runde til å sammenligne i neste runde, lagrer man denne
    # variabelen utenfor while-loopen:
    candidateB = pick_candidate(CANDIDATE_DICTIONARY)
    score = 0
    continue_game = True

    while continue_game:
        # 3. 1 Call the pick_candidate function and print the first candidate with "Compare A:"
        candidateA = candidateB
        print_A = print_candidate(candidateA)
        print(f"Compare A: {print_A}")

        # 4. Import vs and print it
        from art import vs
        print(vs)

        # 5. Call the pick_candidate function and print the second candidate with "Against B:". Sjekker i tillegg om
        # de to alternativene er like.
        candidateB = pick_candidate(CANDIDATE_DICTIONARY)
        if candidateA == candidateB:
            candidateB = pick_candidate(CANDIDATE_DICTIONARY)
        print_B = print_candidate(candidateB)
        print(f"Against B: {print_B}")

        # 6. Make a function that ask the user who they think have the most followers. This function should compare
        # the two candidates against the users choice and return true or false depending on the right or wrong answer.
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        result = compare_candidates(candidateA, candidateB, user_choice)

        # 6. 1 Clear the screen between rounds
        clear()
        print(logo)

        # 7. If the user guesses right, they will gain 1 point and the game continue. If they guess wrong the game
        # should stop and the users score will be printed.
        if result:
            score += 1
            print(f"You're right! Current score: {score}")

        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False


game()
