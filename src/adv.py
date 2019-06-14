from room import Room
from player import Player
from item import Item

# Declare all the items

items = [
	Item("Flashlight", "to see in dark places."),
	Item("Key", "to open special locks."),
	Item("Backpack", "to carry possesions."),
	Item("Crowbar", "to open hatches."),
	Item("Treasure", "to help others."),
]

# Declare all the rooms

dollar_signs = 400*"$"

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items[0]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items[3]], []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items[2]], []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items[1]], [items[0]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber and unlocked the chest! Take the gold in your backpack before it's gone!.""", [items[4]], [items[0], items[1], items[2]]),
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
player1 = Player(name, room["outside"])

is_playing = True
error_message = None

do_not_print = False

key_message = """\n\nKeys:\n\n n - move north\n e - move east\n s - move south\n
 w - move west\n q - quit game\n take ____ - pick up item\n drop ____ - release item\n k - see key list"""

# Check function

def check_for_items(room, items):

	number_of_checks = 0
	player_need = None

	for i in items:
		
		for player_item in player1.items:
			if i.name == player_item.name:
				number_of_checks += 1
			else:
				player_need = i

	if len(items) == number_of_checks:
		player1.current_room = room
		return
	else:
		print(f"\n\nYou need the {player_need.name.lower()} {player_need.description}\nStay here for now...\n")
		do_not_print = True
		return

# Loop

while is_playing:
	
	current_room = player1.current_room

	description = current_room.description
	
	line_string = len(description)*"-"

	if error_message is not None:
		print("\n" + error_message + "\n")
		error_message = None
	elif do_not_print == True:
		print("\n")
		do_not_print = False
	else:
		print("\n" + "Player: " + player1.name + "\n")
		print(line_string + "\n")
		print(current_room.name + "\n")
		print(description + "\n")

		if len(current_room.items) > 0:
			print("Available items:\n")
			for i in current_room.items:
				print(f"{i.name} - {i.description}\n")
		else:
			print("There aren't any available items.\n")

		print(line_string + "\n")

	direction = input("What would you like to do? (\"k\" for Keys):").lower().split(" ")

	if direction is not None:
	
		if len(direction) <= 1:

			if direction[0] == "n":
				if current_room.n_to is not None:
					north_room = current_room.n_to
					check_for_items(north_room, north_room.needed_items)
					continue
				else:
					error_message = "Sorry, you can't go that direction."
					continue
			elif direction[0] == "s":
				if current_room.s_to is not None:
					south_room = current_room.s_to
					check_for_items(south_room, south_room.needed_items)
					continue
				else:
					error_message = "Sorry, you can't go that direction."
					continue
			elif direction[0] == "e":
				if current_room.e_to is not None:
					east_room = current_room.e_to
					check_for_items(east_room, east_room.needed_items)
					continue
				else:
					error_message = "Sorry, you can't go that direction."
					continue
			elif direction[0] == "w":
				if current_room.w_to is not None:
					west_room = current_room.w_to
					check_for_items(west_room, west_room.needed_items)
					continue
				else:
					error_message = "Sorry, you can't go that direction."
					continue
			elif direction[0] == "q":
				is_playing = False
				break
			elif direction[0] == "k":
				error_message = key_message
				continue
			elif direction[0] == "items":

				if len(player1.items) > 0:
					print("\nYour items:\n")

					for i in player1.items:
						print(f"{i.name} - {i.description}\n")
				else:
					print("\nYou currently don't have any items.\n")

				do_not_print = True
				continue
			else:
				error_message = f"Sorry that isn't a valid key.{key_message}"
				continue

		else:

			if direction[0] == "take":
				room_has_item = False
				for i in current_room.items:
					item_name = i.name.lower()
					if item_name == direction[1]:
						if len(player1.items) <= 1 or player1.has_backpack == True:
							player1.take_item(i)
							current_room.items.remove(i)
							

							if i.name == "Treasure":
								print(f"\n\nYou've done it! You've got the treasure!\n\n{dollar_signs}")
								is_playing = False
								room_has_item = True
								break
							else:
								print(f"\n\nYou've picked up the {i.name.lower()}.")
							room_has_item = True
						else:
							print("\n\nYou can't pick up any other items without a way to carry them.")
							room_has_item = True

				if room_has_item == False:
					print("\n\nThat item isn't here.")

				do_not_print = True
				continue

			elif direction[0] == "drop":
				player_has_item = False
				for i in player1.items:
					item_name = i.name.lower()
					if item_name == direction[1]:
						player1.drop_item(i)
						current_room.items += [i]
						print(f"\n\nYou've dropped the {i.name.lower()}.")
						player_has_item = True

				if player_has_item == False:
					print("\n\nYou don't have that item.")

				do_not_print = True
				continue

			else:
				error_message = f"Sorry that isn't a valid key.{key_message}"
				continue

	else:
		error_message = f"Sorry that isn't a valid key.{key_message}"
		continue


print("\n\nThanks for playing!\n\n")