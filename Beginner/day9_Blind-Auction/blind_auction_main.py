from replit import clear
from art import logo


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of: ${highest_bid}")


print(logo)

bids = {}

biding_finished = False

while not biding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other biders? Type 'yes' or 'no'. \n").lower()

    if should_continue == "no":
        biding_finished = True
        find_highest_bidder(bids)

    elif should_continue == "yes":
        clear()








