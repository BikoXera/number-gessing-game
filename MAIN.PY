#MADE BY PRIYNAHSU KOTIA
#NUMBER GUESSING GAME

from random import randint

target = randint(1, 200)
guesses = 0

while True:
    raw = input("Guess a number from 1 to 200: ").strip()

    if not raw.isdigit() or not 1 <= int(raw) <= 200:
        print("Enter a whole number from 1 to 200.")
        continue

    guess = int(raw)
    guesses += 1

    if guess < target:
        print("your guess is lower.")
    elif guess > target:
        print("your guess is higher.")
    else:
        word = "guess" if guesses == 1 else "guesses"
        print(f"You got it in {guesses} {word}.")
        break
