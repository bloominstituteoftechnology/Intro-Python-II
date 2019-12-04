import sys
from room import Room
from player import Player
# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
    passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
    into the darkness. Ahead to the north, a light flickers in
    the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
    to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
    chamber! Sadly, it has already been completely emptied by
    earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Main

# Make a new player object that is currently in the 'outside' room.


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

print('\nEnter "q" to quit the game.')
player_name = input("Enter name: ")
player = Player(player_name, room['outside'])
print(f"\nWelcome {player_name}!")

while True:
    print(f"\nCurrent room: {player.current_room.name}")
    print(f"Description: {player.current_room.description}\n")
    action = input("Where to next? (N,E,S,W): ").upper()
    if (action == "N") and (player.current_room.n_to != None):
        print("Heading north...")
        player.current_room = player.current_room.n_to
    elif (action == "E") and (player.current_room.e_to != None):
        print("Heading east...")
        player.current_room = player.current_room.e_to
    elif (action == "S") and (player.current_room.s_to != None):
        print("Heading south...")
        player.current_room = player.current_room.s_to
    elif (action == "W") and (player.current_room.w_to != None):
        print("Heading west...")
        player.current_room = player.current_room.w_to
    elif action == "Q":
        print("\nGame Over\n")
        sys.exit()
    else:
        print(f"\n{action} leads to a dead end!")
