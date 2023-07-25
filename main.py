from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

print("Welcome to the secret auction program.")

finished_bidding = False
# def auction_winner():

highest_bid = 0

while finished_bidding == False:

    bidders = {}
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    other = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    bidders[name] = bid

    if bid > highest_bid:
        highest_bid = bid
        highest_bidder = name

    if other == 'yes':
        clear()
    elif other == 'no':
        finished_bidding = True
        clear()
        print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")

# auction_winner()