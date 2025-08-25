import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
emojis = {ROCK : "🪨",PAPER :"📄",SCISSORS : "✂️"}
choices = tuple(emojis.keys())

def user_input():
    while True:
        userInput = input("Rock, Paper, or scissor (r/p/s) : ").lower()
        if userInput in choices:
            return userInput
        else:
            print("invalid choice")
            
def display_choices(userInput,randombot):
    print(f"your choice {emojis[userInput]}")
    print(f"bot choice {emojis[randombot]}")
    
def rules_game(userInput,randombot):
    if userInput == randombot:
        print("Tie")
    elif ((userInput == ROCK and randombot == SCISSORS) or
        (userInput == PAPER and randombot == ROCK) or
        (userInput == SCISSORS and randombot == PAPER)):
        print("you win!")
    else:
        print("you lose!")

def play_game():
    while True:
        userInput = user_input()
        randombot = random.choice(choices)
        display_choices(userInput,randombot)
        rules_game(userInput,randombot)
          
        isDone = input("Continue (y/n) : ").lower()
        if isDone == 'n':
            break

play_game()