# Import module we need
import random

# File i/o functions for historical results
def load_results():
    text_file = open("examples/1history.txt", "r")
    history = text_file.read().split(",")
    text_file.close()
    return history

def save_results( w, t, l):
    text_file = open("history.txt", "w")
    text_file.write( str(w) + "," + str(t) + "," + str(l))
    text_file.close()

# Welcome message
results = load_results()
wins = int(results[0])
ties = int(results[1])
losses = int(results[2])
print("Welcome to Rock, Paper, Scissors!")
print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))
print("Please choose to continue...")


# Initialize user, computer choices
computer = random.randint(1,3)
user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

# Gamplay loop
while not user == 9:
    # User chooses ROCK
    if user == 1:
        if computer == 1:
            print("Computer chose rock...tie!")
            ties += 1
        elif computer == 2:
            print("Computer chose paper...computer wins :(")
            losses += 1
        else:
            print("Computer chose scissors...you win :)")
            wins += 1

    # User chooses PAPER
    elif user == 2:
        if computer == 1:
            print("Computer chose rock...you win :)")
            wins += 1
        elif computer == 2:
            print("Computer chose paper...tie!")
            ties += 1
        else:
            print("Computer chose scissors...computer wins :(")
            losses += 1
    
    # User chooses SCISSORS
    elif user == 3:
        if computer == 1:
            print("Computer chose rock...computer wins :(")
            losses += 1
        elif computer == 2:
            print("Computer chose paper...you win :)")
            wins += 1
        else:
            print("Computer chose scissors...tie!")
            ties += 1
    else:
        print("Invalid selection. Please try again.")
    # Print updated stats
    print("Wins: %s, Ties: %s, Losses: %s" % (wins, ties, losses))

    # Prompt user to make another selection
    print("Please choose to continue...")

    # Initialize user, computer choices
    computer = random.randint(1,3)
    user = int(input("[1] Rock  [2] Paper   [3] Scissors    [9] Quit\n"))

# Game over, save results
save_results(wins, ties, losses)