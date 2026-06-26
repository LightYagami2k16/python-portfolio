# Number Guessing Game
# Practice: while loops, random module, if/else

import random

def play_game():
    secret_number = random.randint(1, 100)
    guesses = 0

    print("\n=== Number Guessing Game ===")
    print("I'm thinking of a number between 1 and 100.")
    print("You have unlimited guesses. Good luck!\n")

    while True:
        # Get a guess from the player
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a whole number.")
            continue

        guesses += 1

        # Check the guess
        if guess < 1 or guess > 100:
            print("Please guess a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"\n🎉 Correct! You got it in {guesses} guess{'es' if guesses != 1 else ''}!")
            break

# Main program — keeps asking to play again
print("Welcome to the Number Guessing Game!")

while True:
    play_game()
    again = input("\nPlay again? (yes/no): ").strip().lower()
    if again not in ["yes", "y"]:
        print("Thanks for playing!")
        break
