import random

choices = ('r','p','s')
computer_score = 0
player_score = 0

def get_players_choice():

    global choices
    symbol = input("Choose either rock(r), paper(p), or scissors(s). ").lower()

    if symbol not in choices: 
        print("You did not enter a valid option. ")
        return get_players_choice()
    else: 
        return symbol
    
def computer():
    return random.choice(choices)

def game():
    global computer_score, player_score
    pChoice = get_players_choice()
    cChoice = computer()
    random_response = "The world was almost destroyed when the {pChoice}'s collided".format(pChoice = pChoice)

    print("The computer has chosen", cChoice)
    print("You have chosen", pChoice)

    if pChoice == cChoice:
        print("It's a tie! " + random_response + " No one gets a point. ")
    elif (pChoice == 'r' and cChoice == 's') or (pChoice == 's' and cChoice == 'p') or (pChoice == 'p' and cChoice == 'r'):
        print("You won!")
        player_score += 1
    else: 
        print("You have been dominated by a computer!")
        computer_score += 1
    print()

print("Welcome to your doom! I mean, Rock, Paper, Scissors!!!")
while True:
    for i in range(5):
        game()
    print("Good job! \nYour score is:", player_score, "\nMy score is:", computer_score)
    print()
    again = int(input("Press 1 to continue\nPress 2 to reset and continue\nPress 3 to exit "))    
    if again==1:
        continue
    elif again==2:
        player_score=0
        computer_score=0
        continue
    else:
        break

print("Peace out!")