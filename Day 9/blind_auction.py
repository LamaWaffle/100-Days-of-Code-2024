
import os
clear = lambda: os.system('cls')

def new_bidder(name, bid_amount):
    new_bidder = {}
    new_bidder["Name"] = name
    new_bidder["Amount"] = bid_amount
    bids.append(new_bidder)

bids = []

print("Welcome to the Secret Auction! \n")

looping = True
while looping:

    name = input("What is your name? ")
    price = input("What is your bid? $")
    new_bidder(name, price)

    anyone_else = input("Are there any other bidders? 'yes' or 'no'? ")
    if anyone_else == "no":
        looping = False
        
        bidders_bet = 
        print(bidders_bet)

    
    
    else:
        clear()
        print("Continuing program until all users have inputted their bids..")
        continue
