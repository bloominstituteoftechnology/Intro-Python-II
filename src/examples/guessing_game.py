import random


def guessing_game():
    print("Guess the number!")

    # game picks a random number between 0 and 100
    secret_number = random.randrange(101)
    # loop forever until user guesses correctly
    # or user quits game
    while True:
        # prompt the user to make a guess
        guess = input("Input your guess: ")
        # make sure input is of proper format
        try:
            guess = int(guess)
        except ValueError:
            print("Please enter an integer.")
            continue

        print(f"You guessed: {guess}")
        # check to see if the guess is too high, too low, or correct
        if guess == secret_number:
            print("You win!")
            break
        elif guess < secret_number:
            print("Too small!")
        else:
            print("Too big!")


if __name__ == '__main__':
    guessing_game()
