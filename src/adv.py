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

name = input("Enter your name to begin:")

# Make a new player object that is currently in the 'outside' room.

player1 = Player(name, room["outside"])

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

is_playing = True
error_message = None

while is_playing:
	
	current_room = player1.current_room

	description = current_room.description
	
	line_string = len(description)*"-"

	if error_message is not None:
		print("\n" + error_message + "\n")
		error_message = None
	else:
		print("\n" + "Player: " + player1.name + "\n")
		print(line_string + "\n")
		print(current_room.name + "\n")
		print(description + "\n")
		print(line_string + "\n")

	direction = input("Which direction would you like to go? (n, e, s, w):").replace(" ", "").lower()

	if direction is not None:
		if direction == "n":
			if current_room.n_to is not None:
				north_room = current_room.n_to
				player1.current_room = north_room
				continue
			else:
				error_message = "Sorry, you can't go that direction."
				continue
		elif direction == "s":
			if current_room.s_to is not None:
				south_room = current_room.s_to
				player1.current_room = south_room
				continue
			else:
				error_message = "Sorry, you can't go that direction."
				continue
		elif direction == "e":
			if current_room.e_to is not None:
				east_room = current_room.e_to
				player1.current_room = east_room
				continue
			else:
				error_message = "Sorry, you can't go that direction."
				continue
		elif direction == "w":
			if current_room.w_to is not None:
				west_room = current_room.w_to
				player1.current_room = west_room
				continue
			else:
				error_message = "Sorry, you can't go that direction."
				continue
		elif direction == "q":
			is_playing = False
			break
		else:
			error_message = "Sorry that isn't a valid key.\n\nKeys:\n\n n - move north\n e - move east\n s - move south\n w - move west\n q - quit game"
			continue
	else:
		error_message = "Sorry that isn't a valid key.\n\nKeys:\n\n n - move north\n e - move east\n s - move south\n w - move west\n q - quit game"
		continue


print("Thanks for playing!")