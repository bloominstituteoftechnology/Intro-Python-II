import random

class Opponent:

    def __init__(self, name):
        self.name = name
        self._move_choices = ["r", "p", "s"]
    def get_move(self):
        return random.choice(self._move_choices)

class RockOpponent(Opponent):
    def __init__(self, name):
        self.name = name
        self._move_choices = ["r", "r", "r", "r", "r", "r", "r", "p", "s"]

d = {"rp": -1, "rs": 1, "sp": 1, "sr": -1, "pr": 1, "ps": -1}

# Def a function that takes a player and CPU move and returns the win status
# 1 - win, 0 - tie, -1 - loss
def calculate_rps(player_move, cpu_move):
    if player_move == cpu_move:
        return 0
    else:
        return d[player_move + cpu_move]

wins = 0
losses = 0
ties = 0
move_choices = ["r", "p", "s"]

o = RockOpponent("Dumb Computer")

# Build a REPL command loop
while True:
    cmd = input("Type r/p/s; q to end -> ")
    # Calculate CPU move
    cpu_move = o.get_move()
    # Prompt the player to input r/p/s
    # Evaluate the results based on computer command
    # Check for input validity
    if cmd in move_choices:
        results = calculate_rps(cmd, cpu_move)
        if results == 1:
            # WIN
            wins += 1
            result_name = "win!"
        elif results == 0:
            # TIE
            ties += 1
            result_name = "tie."
        elif results == -1:
            # LOSE
            losses += 1
            result_name = "lose."
        print(f"\nComputer picks {cpu_move}. You {result_name}")
    elif cmd == "q":
        # If the player types 'q', quit the game
        print("Goodbye!")
        break
    else:
        print("What's the matter? Can't you read?")
        # If input is not valid, print an error message and loop
    print(f"You won {wins} times; you lost {losses} times; and tied {ties} times")
    # Display the results and score
    # Loop