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
    """A number-guessing game."""
    
    random_number = random.randint(1,100)
    guess = None
    number_of_guesses = 0
    # might need to set up low and high parameters later 
    # too_low = 0
    # too_high = 100

    print("Welcome to Mellody's Random Number Game!")
    print("Hello, what is your name?")
    name = input("type in your name: ")
    print(f"{name}, im thinking of a number between 1 and 100.")
    print("Try to guess my number")

# 8.3 handling exceptions 
# https://docs.python.org/3/tutorial/errors.html

# ensuring the user inputs an integer and 
    while True:
        try:
            guess = int(input("Your guess? "))
            break
        except ValueError:
            print("That is not a valid number, please enter a number.")
        
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
            
            
