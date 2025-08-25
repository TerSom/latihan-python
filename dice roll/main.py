import math
import random

while True:
    userInput = input("Roll the dice? (y/n) : ").lower()
    if userInput == "y":
        die1 = random.randint(1,10)
        die2 = random.randint(1,10)
        print(f"({die1}, {die2})")
    elif userInput == "n":
        print("Thanks for playing")
        break
    else:
        print("invalid choice!")
    