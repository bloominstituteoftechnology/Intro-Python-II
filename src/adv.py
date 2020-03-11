from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(room['outside'])

# Write a loop that:
while True:

	print("##################################################################")
# * Prints the current room name
	print(f"# Current Room: {player.room.name}")
# * Prints the current description (the textwrap module might be useful here).
	print("##################################################################")
	print(f"# {player.room.description}")
	print("##################################################################\n")
# * Waits for user input and decides what to do.
	user = input("[n] North  [s] South  [e] East  [w] West    [q] Quit:\n").lower()

# If the user enters "q", quit the game.
	if user == 'q':
		break
# If the user enters a cardinal direction, attempt to move to the room there.
	elif user == 'n':
		if player.room.n_to != None:
			player.room = player.room.n_to
		else:
			print("Can't go to the North...")
	elif user == 's':
		if player.room.s_to != None:
			player.room = player.room.s_to
		else:
			print("Can't go to the South...")
	elif user == 'e':
		if player.room.e_to != None:
			player.room = player.room.e_to
		else:
			print("Can't go to the East...")
	elif user == 'w':
		if player.room.w_to != None:
			player.room = player.room.w_to
		else:
			print("Can't go to the West...")
# Print an error message if the movement isn't allowed.
	else:
		print("Invalid command.")
