# 🎲 Number Guessing Game

The computer picks a secret random number between 1 and 100. You try to guess it!

## What it does

- Picks a random number between 1 and 100
- Tells you if your guess is too high or too low
- Counts how many guesses you take
- Lets you play again when you finish

## How to run it

```bash
python guessing_game.py
```

## Example

```
=== Number Guessing Game ===
I'm thinking of a number between 1 and 100.
You have unlimited guesses. Good luck!

Enter your guess: 50
Too high! Try a lower number.

Enter your guess: 25
Too low! Try a higher number.

Enter your guess: 37
Too high! Try a lower number.

Enter your guess: 31
🎉 Correct! You got it in 4 guesses!

Play again? (yes/no): no
Thanks for playing!
```

## Python concepts used

- `import random` and `random.randint()` to pick a random number
- `while True` loop that keeps going until the right number is guessed
- `if / elif / else` to check if the guess is too high, too low, or correct
- A counter variable to track how many guesses the player has made
- `int(input())` to read numbers from the user
