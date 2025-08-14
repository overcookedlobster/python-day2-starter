# Sub-Task 2: Guessing Game
import random

print("I'm thinking of a number between 1 and 100.")
secret_number = random.randint(1, 100) # You can change this to a fixed number for easier testing, e.g., 42

# TODO: Create a while loop that continues as long as the user hasn't guessed the number.
# Inside the loop:
# 1. Prompt the user for their guess and convert it to an integer.
# 2. Use an if/elif/else statement to compare the guess to the secret_number.
# 3. Print "Too low!", "Too high!", or "You got it!" accordingly.
# 4. If the guess is correct, break out of the loop.

while True:
    guess = int(input("What's your guess? "))
    # TODO: Add comparison logic here
    if True: # This is a placeholder
        print("You got it!")
        break

