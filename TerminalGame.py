import random

print("=============================================")
print(" Welcome to Life of an International Student ")
print("=============================================")
print("")
print("---------------------------------------------")
print(" HOW TO PLAY ")
print("---------------------------------------------")
print(" You will play as an international student in")
print(" AUSTRALIA ")
print(" and your objective is to ")
print(" save enough money to pay your fees ($2000) ")
print("You have 3 attributes: Money, Happiness and Time")
print("Survive random events, make strategic decisions")
print(" to keep a good balance between attributes. ")
print("---------------------------------------------")
print(" GOOD LUCK ")
print("---------------------------------------------")
print("")

ready1 = input("ENTER Y to continue: ")

if ready1.lower() == "y":
    print("")
    print("Choose your Character:")
    print("")
    print("1) Jayesh from Nepal")
    print("2) Somchai from Thailand")
    print("3) Alejandro from Colombia")
    print("4) Create your own Character")
    print("")
    player = int(input("Choose by entering a number [1-4]: "))

    if player == 1:
        print("---------------------------------")
        print("You have picked Jayesh from Nepal!")
        print("---------------------------------")
    elif player == 2:
        print("---------------------------------------")
        print("You have picked Somchai from Thailand!")
        print("---------------------------------------")
    elif player == 3:
        print("---------------------------------------")
        print("You have picked Alejandro from Colombia!")
        print("---------------------------------------")
    elif player == 4:
        customname = input("Enter your Character's Name: ")
        customaddress = input("Where is your Character from?: ")
        print("--------------------------------------------------")
        print(f"You have picked {customname} from {customaddress}!")
        print("--------------------------------------------------")
    else:
        print("GAME OVER")
        exit()
else:
    print("GAME OVER")
    exit()

ready2 = input("Enter Y to continue: ")
print("")

# Global variables
time = 60
money = 1000
happiness = 50

# Function to update and display the current status
def update_balance(time_change, money_change, happiness_change):
    global time, money, happiness
    time += time_change
    money += money_change
    happiness += happiness_change
    print("---------------------------")
    print("Updated Status:")
    print(f"Time = {time}")
    print(f"Money = ${money}")
    print(f"Happiness = {happiness}")
    print("---------------------------")

# Function to trigger lotto
def lotto():
    global money
    print("You stumble across a Lotto shop,")
    print("play the lotto? [-$5 Money]")
    print("")
    play = input("Enter Y to play and N to skip: ").lower()

    if play == "y":
        update_balance(0, -5, 0)  # Deduct $5 for playing
        outcome = random.randint(1, 15)
        winnings = 0
        if outcome <= 6:
            winnings = 0
        elif outcome <= 11:
            winnings = 20
        elif outcome <= 14:
            winnings = 100
        elif outcome == 15:
            winnings = 500
        print(f"Congratulations! You won ${winnings}.")
        update_balance(0, winnings, 0)
    else:
        print("You skipped the lotto.")

# Function to trigger random events
def random_event():
    event = random.randint(1, 10)
    if event in (1, 2):
        print("You find $50 on the street.")
        update_balance(0, +50, 0)
    elif event in (3, 4):
        print("Rent is due: -$200")
        update_balance(0, -200, 0)
    elif event in (5, 6):
        print("You helped a tourist: +10 Happiness")
        update_balance(0, 0, +10)
    elif event in (7, 8):
        print("Your phone screen cracks: -15 Happiness")
        update_balance(0, 0, -15)
    elif event == 9:
        print("You get stuck in traffic: -10 Time")
        update_balance(-10, 0, 0)
    elif event == 10:
        print("Your parents send you money: +$100")
        update_balance(0, +100, 0)

# Function to check if the game is over
def check_game_over():
    global time, money, happiness
    if time <= 0 or money <= 0 or happiness <= 0:
        print("\nGAME OVER! One of your attributes reached zero.")
        exit()

# Function to continue the game
def continue_game():
    cont = input("Enter Y to continue: ")
    if cont.lower() == 'y':
        print("")
    else:
        print("GAME OVER!")
        exit()

    except ValueError:
    print("Invalid input. Please enter 1 or 2.")

if round5 == 1:
    update_balance(-15, -300, +20)
elif round5 == 2:
    update_balance(-15, +300, -20)

check_game_over()
continue_game()

# Trigger Random Event
random_event()
check_game_over()
continue_game()

# Round 6
print("Round 6:")
print("Your car breaks down, and you need it fixed.")
print("1) Get it fixed immediately: -10 hours, -$500, +5 Happiness")
print("2) Delay repairs: -5 Happiness")

while True:
    try:
        round6 = int(input("What do you want to do? [1-2]:"))
        if round6 in [1, 2]:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

if round6 == 1:
    update_balance(-10, -500, +5)
elif round6 == 2:
    update_balance(0, 0, -5)

check_game_over()
continue_game()

# Trigger Lotto
lotto()
check_game_over()
continue_game()

# Round 7
print("Round 7:")
print("You have an upcoming exam.")
print("1) Study hard: -20 hours, -$50, +10 Happiness")
print("2) Wing it: -10 Happiness")

while True:
    try:
        round7 = int(input("What do you want to do? [1-2]:"))
        if round7 in [1, 2]:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

if round7 == 1:
    update_balance(-20, -50, +10)
elif round7 == 2:
    update_balance(0, 0, -10)

check_game_over()
continue_game()

# Trigger Random Event
random_event()
check_game_over()
continue_game()

# Round 8 - Final Round
print("Round 8 (Final Round):")
print("It's time to pay your student fees.")
print("1) Pay $2000 in fees: -$2000")
print("2) Delay payment: -10 Happiness")

while True:
    try:
        round8 = int(input("What do you want to do? [1-2]:"))
        if round8 in [1, 2]:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

if round8 == 1:
    if money >= 2000:
        update_balance(0, -2000, 0)
        print("Congratulations! You've successfully paid your fees!")
        print("You WIN the game!")
        exit()
    else:
        print("You don't have enough money to pay the fees!")
        print("GAME OVER!")
        exit()
elif round8 == 2:
    update_balance(0, 0, -10)

check_game_over()

# Final Outcome
print("The game has ended. Here is your final status:")
print(f"Time = {time}")
print(f"Money = ${money}")
print(f"Happiness = {happiness}")

if money >= 2000:
    print("Congratulations! You've successfully managed your life and paid your fees. YOU WIN!")
else:
    print("Unfortunately, you couldn't save enough money. GAME OVER!")
