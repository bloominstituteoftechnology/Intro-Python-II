import sys
from player import Player

# Main

# Make a new player object that is currently in the 'outside' room.
print("\n--Python RPG Game (Alpha)--\n")
player_name = input("Enter name: ")
player = Player(player_name)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

print(f"\nWelcome {player_name}!")
print('\nEnter "q" to quit the game.')
print("Navigate by entering [N,E,S,W]\n")
print(f"Current room: {player.current_room.name}")
print(f"Description: {player.current_room.description}\n")

while True:
    action = input("\nWhat next? ").upper()
    if action in ['N', 'E', 'S', 'W']:
        player.move(action)
    # elif action[0] in ['take','get','pick','drop']:
    #     player.inventory(action[0],action[1])
    elif action == "Q":
        print("\nGame Over\n")
        sys.exit()
    else:
        print("\nInvalid command!\n")
