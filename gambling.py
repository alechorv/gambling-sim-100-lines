# Package imports (TIP: "from" only imports selected functions/items)
from os import system
from time import sleep
from random import random
from math import floor, ceil

loading_set = ('|', '/', '-', '\\') # Characters for the loading animation

system('cls') # Clears the console/terminal

print("==================================")
print("|| WELCOME TO THE GAMBLING ROOM ||")
print("==================================\n\n\n") # TIP: "\n" creates a new empty line

print("What's in your wallet?")
wallet = float(input("> $")) # Using 'float' for decimal values

system('cls')

# If the player types "0" into the wallet
if int(wallet) == 0:
    print("\nYou came to the Gambling Room... with no money?\n")
    print("You're banned. Get out.")
else:
    # The games start here if the player has >$0 to start

    print("========================")
    print("|| IT'S GAMBLING TIME ||") # Start message
    print("========================\n\n\n")

    while 1: # Gambling loop (TIP: "while 1:" = "while True:")
        # If the player has lost all their money
        if int(wallet) == 0:
            print("Alright, time to go home bud.\n")
            break

        print(f"YOUR WALLET: ${wallet}\n\n\n") # TIP: Putting 'f' allows devs to insert variables within the string using curly brackets

        print("Enter BET & MULTIPLIER: (enter '0' to cash out)")
        bet = float(input("> $")) # Bet amount
        if int(bet) == 0:
            system('cls')
            break
        while bet > wallet: # Make sure the player has enough money
            print("With what money, dumbass?")
            bet = float(input("> $")) # Bet amount
        multi = float(input("> x")) # Multiplier
        payout = bet * multi

        chance = round(100 / (multi + 1), 2) # Probabilty formula: 1x = 50%, 2x = 33.33%, 3x = 25%...

        print(f"\nODDS: {chance}%")

        # Loading animation that slows down as it plays
        load_speed = 0.01 # Seconds to wait between animation frames
        for _ in range(7): # Repeat 7 times, the "_" is because we don't need a variable to track the loop
            for l in loading_set: # 'l' changes to the next frame character in the 'loading_set' list every cycle
                print(f"\r{l} ", end="") # Prints the loading character, '\r' resets it every frame so it doesn't duplicate, and 'end=""' stops it from automatically going to the next line
                sleep(load_speed) # Waits however many seconds 'load_speed' is set to
                load_speed += 0.01 # Slows down the animation by making it wait slighly longer between future frames

        system('cls')

        if random() * 100 < chance: # 'random.random' chooses a decimal number between 0 and 1, multiply it by 100 and you get a random percentage to compare with our chance percentage
            wallet += payout # Add the payout to the player's wallet

            win_msg = f">>>   YOU WON ${payout}   <<<"
            msg_len = len(win_msg) # Get's how many characters are in the win message, because it depends on how much money the player has won

            win_pattern = ">"*ceil(msg_len/2) + "<"*floor(msg_len/2) # Creates a ">>><<<" pattern string that's same length as the win message (aka 'win_msg')
            print(win_pattern)
            print(win_msg)
            print(win_pattern)
            print("\n\n")

            # If the player puts "0" for the multiplier or the bet
            if int(multi) == 0:
                print("Wow, really got us with that one.")
            elif int(bet) == 0:
                print("Bro hit the big jackpot.")
        else:
            wallet -= bet # Subtract the player's bet from their wallet

            # If the player bet $0 and lost, if not then just say the normal lose message
            if int(bet) == 0:
                print(f"\nYou Lost... uhm... $0?\n")
            else:
                print(f"\nYou Lost ${bet}...\n")

        input("Press enter to play again... ") # Pressing 'Enter' just reads an empty input, and then continues with the code, running back through the loop!
        system('cls')

        print("===============================")
        print("|| LET'S RUN THAT SHIT BACK! ||") # New starting message since the user is replaying
        print("===============================\n\n\n")

# Runs after the loop has broken (Cashout, No money, etc...)
print("\nThanks for playing!")
print(f"FINAL CASHOUT: {wallet}\n")

