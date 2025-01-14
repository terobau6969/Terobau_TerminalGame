import random


print("=============================================")
print(" Welcome to Life of an International Student ")
print("=============================================")
print("")
print("---------------------------------------------")
print("                 HOW TO PLAY                 ")
print("---------------------------------------------")
print(" You will play as an international student in")
print("                 AUSTRALIA                   ")
print("          and your objective is to           ")
print(" save enough money to pay your fees ($2000) ")
print("You have 3 attributes: Money, Happiness and Time")
print("Survive random events, make strategic decisions")
print("  to keep a good balance between attributes. ")
print("---------------------------------------------")
print("                  GOOD LUCK                  ")
print("---------------------------------------------")
print("")

ready1 = input("ENTER Y to continue:")
if ready1.lower() == "y":
    print("")
    print("Choose your Character:")
    print("")
    print("1) Jayesh from Nepal")
    print("2) Somchai from Thailand")
    print("3) Alejandro from Colombia")
    print("4) Create your own Character")
    print("")

    player = int(input("Choose by entering a number [1-4]:"))

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
        customname = input("Enter your Character's Name:")
        customaddress = input("Where is your Character from?:")
        print("--------------------------------------------------")
        print(f"You have picked {customname} from {customaddress}!")
        print("--------------------------------------------------")
else:
    print("GAME OVER")
    exit
    
ready2 = input("Enter Y to continue:")
print("")

# Global variables
time = 70
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

#function to trigger lotto
def lotto():
    global money
    print("You stumble across a Lotto shop,")
    print("play the lotto? [-$5 Money]")
    print("")
    play = input("Enter Y to play and N to skip:").lower()

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

#function to continue
def continue_game():
   cont = input("Enter Y to continue:")
   if cont.lower() == 'y':
       print("")
   else:
       print("GAME OVER!")
       exit


#Main events of the game
if ready2.lower() == "y":
    print("--------------------------")
    print ("Starting Balance:")
    print (f"Time: {time}")
    print (f"Money: ${money}")
    print (f"Happiness: {happiness}")
    print("--------------------------")

    print("")

    print("----------------------------------------------")
    print("Winning Conditions:")
    print("Pay $2000 student fees by the end of the game.")
    print("THERE ARE A TOTAL OF 8 ROUNDS")
    print("----------------------------------------------")

    print("")

    print("------------------------------------")
    print("Losing conditions:")
    print("Dont be Broke i.e. Money = 0)")
    print("Dont run out of time i.e. Time = 0")
    print("Dont be depressed i.e. Happiness = 0")
    print("------------------------------------")

    print("")
else:
    print("GAME OVER")
    exit
    
gamestart = input("ENTER Y to continue:")
print("")
if gamestart.lower() != "y":
    print ("GAME OVER")
    exit

else:
    print("Lets Begin!")
    print("")

#Round 1
print ("Round 1:")
print("You get invited to dinner with friends,")
print("but you have a shift at work:")
print("1) Call in sick : -5 Time, -$50 Money, +10 Happiness")
print("2) Go to work: -5 Time, +$100 Money, -10 Happiness")
print("")
while True:
    try:
        round1 = int(input("What do you want to do? [1-2]:"))
        if round1 in [1, 2]:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

if round1 == 1:
    update_balance(-5, -50, +10)
elif round1 == 2:
    update_balance(-5, +100, -10)

    
check_game_over()

continue_game()

#Trigger a random event
random_event()
check_game_over()

continue_game()

#Round 2
print("Round 2:")
print("Your friend asks for help moving apartments.")
print("1) Help them: -10 Time, +15 Happiness")
print("2) Say you're too busy: +5 hours, -10 Happiness")

while True:
    try:
        round2 = int(input("What do you want to do? [1-2]:"))
        if round2 in [1, 2]:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

if round2 == 1:
    update_balance(-10, 0, +15)
    
elif round2 == 2:
    update_balance(+5, 0, -10)
    

check_game_over()
continue_game()

#Trogger Lotto
lotto()
check_game_over()

continue_game()

#Round 3
print("Round 3:")
print(" Your friends plan a 3-night trip to Sydney:")
print("but you have a shift at work:")
print("1) Call in sick and join them: -15 hours, -$300, +20 Happiness")
print("2) Cancel with friends and work: -15 hours, +$300, -20 Happiness")
while True:
    try:
        round3 = int(input("What do you want to do? [1-2]:"))
        if round3 in [1, 2]:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

if round3 == 1:
    update_balance(-15, -300, +20)
elif round3 == 2:
    update_balance(-15, +350, -20)

check_game_over()
continue_game()

#Trigger Random Event
random_event()
check_game_over()
continue_game()

#Round 4
print("Round 4:")
print("You meet someone on Tinder")
print("1) Ask her out: -5 hours, -$30, +10 Happiness")
print("2) Delete Tinder and Lock in: -10 Happiness")
while True:
    try:
        round4 = int(input("What do you want to do? [1-2]:"))
        if round4 in [1, 2]:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

if round4 == 1:
    update_balance(-5, -30, +10)
elif round4 == 2:
    update_balance(0, 0, -10)

check_game_over()
continue_game()

#Trigger Lotto
lotto()
check_game_over()
continue_game()

#Round 5
print("Round 5:")
print("Your friends organise a movie night:")
print("but you have a shift at work:")
print("1)Call sick at work and join: -15, -$300, +20 Happiness")
print("2)Make excuse and work instead: -15, +$300, -20 Happiness")
while True:
    try:
        round5 = int(input("What do you want to do? [1-2]:"))
        if round5 in [1, 2]:
            break
        else:
            print("Invalid choice. Please select 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter 1 or 2.")

if round5 == 1:
    update_balance(-15, -300, +20)
elif round5 == 2:
    update_balance(-15, +400, -20)
    
check_game_over()
continue_game()

#Check work status
if round1 == 1 and round5 ==1:
    print("You called in sick too much and got fired from your work")
    print("GAME OVER!")
    exit
elif round1 == 1 and round3 ==1:
    print("You called in sick too much and got fired from your work")
    print("GAME OVER!")
    exit
elif round3==1 and round5==1:
    print("You called in sick too much and got fired from your work")
    print("GAME OVER!")
    exit 
else:
    print("")
   
#Trigger Random Event
random_event()
check_game_over()
continue_game()

#Round 6
if round4 == 1:
    #Round 6 if not single
    print("Round 6:")
    print("Your Partner's Birthday is coming up:")
    print("1)Buy a gift: -$50, +10 Happiness")
    print("2)Ignore them: -20 Happiness (There is a change they will leave you)")
    while True:
        try:
            round6a = int(input("What do you want to do? [1-2]:"))
            if round6a in [1, 2]:
                break
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

        
        if round6a == 1:
            update_balance(0, -50, +10)
        elif round6a == 2:
            update_balance(0, 0, -20)

        check_game_over()
    continue_game()

else:
    #Round 6 if single
    print("Round 6:")
    print("You want to start going to the gym:")
    print("1)Sign up for Membership: -10 Hours, -$50, +20 Happiness")
    print("2)Scratch the idea and stay unhealthy: -5 Happiness")
    while True:
        try:
            round6b = int(input("What do you want to do? [1-2]:"))
            if round6b in [1, 2]:
                break
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    round6a = 0
    if round6b == 1:
        update_balance(-10, -50, +20)
    elif round6b == 2:
        update_balance(0, 0, -5)


    check_game_over()
    continue_game()


#Trigger Lotto
lotto()
check_game_over()
continue_game()


#Round 7
if round4 == 1:
    #Round 7 if not single
    print("Round 7:")
    print("Your relationship anniversary is coming up:")
    print("1)Surprise your partner: -$50, +10 Happiness")
    print("2)Ignore it: -20 Happiness (There is a change they will leave you)")
    while True:
        try:
            round7a = int(input("What do you want to do? [1-2]:"))
            if round7a in [1, 2]:
                break
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    if round7a == 1:
        update_balance(0, -50, +10)
    elif round7a == 2:
        update_balance(0, 0, -20)
 

    check_game_over()
    continue_game()

    
else:
    #Round 7 if single
    print("Round 7:")
    print("You pick up painting as a hobby:")
    print("1)Buy supplies: -5 hours, -$40, +15 Happiness")
    print("2)Scratch the idea: -5 Happiness")
    while True:
        try:
            round7b = int(input("What do you want to do? [1-2]:"))
            if round7b in [1, 2]:
                break
            else:
                print("Invalid choice. Please select 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    round7a= 0
    if round7b == 1:
        update_balance(-5, -40, +15)
    elif round7b == 2:
        update_balance(0, 0, -5)
    else:
        print("GAME OVER: Wrong Input")
        exit

    check_game_over()
    continue_game()


#Check Relationshop Status  
if round7a == 2 and round6a == 2:
    print("GAME OVER: Your Partner left you for being ignorant")
    update_balance(0, 0 , -100)

else:
    print("")
    
#Round 8
print("Round 8:")
print("Its Christmas!! You are invited to dinner with Family and Friends.")
print("but you get holiday bonus at work if you attend:")
print("1)Buy gifts and attend dinner: -10, -$100 +25 Happiness")
print("2)Work and miss out on Christmas: -10, +$600, -30 Happiness")
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
    update_balance(-10, -100, +25)
elif round8 == 2:
    update_balance(-10, +500, -30)
    
check_game_over()
continue_game()


#Check winning conditions
if money >= 2000:
    print(f"You have ${money}, Congratulations you WIN!!!")
else:
    print(f"You have ${money}, not enought to pay the fees :(")
    print("At least you survived, but you still are a loser!")

exit











    