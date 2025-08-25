import random

randomNumber = random.randint(1,100) 
while True:
    try:
        guessing = int(input("Guess the number between 1 and 100 :  "))
        if guessing == randomNumber:
            print("Congratulation! You guessed the number")
            break
        elif guessing > randomNumber:
            print("To High!")
        else:
            print("To Low!")
    except ValueError:
        print("please enter a valid number")
    
   
        