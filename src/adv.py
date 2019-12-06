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
print(f"Description: {player.current_room.description}")

while True:
    action = input("\nWhat next? ").lower().split(" ")
    if action[0] in ['n', 'e', 's', 'w']:
        player.move(action[0])
    elif action[0] in ['take', 'get', 'pick', 'grab', 'hold', 'drop']:
        player.handle_items(action[0], action[1])
    elif action[0] in ['i','inventory']:
        player.inventory()
    elif action[0] in ["q", 'quit', 'exit']:
        print("\nGame Over\n")
        sys.exit()
    else:
        print("\nInvalid command!")
