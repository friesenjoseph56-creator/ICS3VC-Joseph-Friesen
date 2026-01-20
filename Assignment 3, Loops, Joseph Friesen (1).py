
# SETUP
secret_number = 4
guess = None
guess_count = 0

print("I'm thinking of a number between 1 and 10.")

# LOOP UNTIL CORRECT GUESS
while guess != secret_number:
    guess = int(input("Enter your guess: "))
    guess_count += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"You got it! The secret number was {secret_number}.")
        print(f"It took you {guess_count} guesses!")
