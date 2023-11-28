"""A number-guessing game."""

# Put your code here
# print("hi")

# greet player
# get player name 
# choose random number between 1 and 100
# repeat forever 
    # get guess
    # if guess is incorrect:
        # give hint
        # increase number of guesses
    # else:
        # congratulate player 

import random

def random_number_game():
    random_number = random.randint(1,100)
    guess = None
    number_of_guesses = 0
    # might need to set up low and high parameters later 
    # too_low = 0
    # too_high = 100

    print("Hello, what is your name?")
    name = input("type in your name: ")
    print(f"{name}, im thinking of a number between 1 and 100.")
    print("Try to guess my number")
    guess = int(input("Your guess? "))
    while guess != random_number: 
        if guess < random_number:
            print("Your guess is too low, try again.")
            number_of_guesses = number_of_guesses + 1
            guess = int(input("Your guess? "))
        elif guess > random_number:
            print("Your guesss is too high, try again.")
            number_of_guesses = number_of_guesses + 1
            guess = int(input("Your guess? "))
    if guess == random_number:
        number_of_guesses = number_of_guesses + 1
        print(f"Well done, {name}! You found my number in {number_of_guesses} tries!")
random_number_game()
            
            
