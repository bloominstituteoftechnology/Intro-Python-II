from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", "Dim light filters in from the south. Dusty passages run north and east."),

    'overlook': Room("Grand Overlook", "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."),

    'narrow':   Room("Narrow Passage", "The narrow passage bends here from west to north. The smell of gold permeates the air."),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
Sadly, it has already been completely emptied by earlier adventurers. 
The only exit is to the south."""),
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

# Add items to rooms
room['foyer'].addItem(Item("Sword", "An old rusty blade, but still dangerous in the right hands."))
room['overlook'].addItem(Item("Coin", "Looks like a remnant of a great treasure."))

# Make a new player object that is currently in the 'outside' room.
print("WELCOME TO PYTHON ADVENTURE GAME!!!")
player_name = input("Please enter your name --> ")
player = Player(player_name, room["outside"])
print(f"\n---------- Welcome {player.name}! Get ready to start your adventure! ----------\n*press 'q' to quit\n")

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

possible_directions = ["n", "s", "e", "w"]

while True:
    print(f"Location: \033[1m{player.current_room.name}\033[0m")
    print(player.current_room.description)

    if len(player.current_room.items) > 0:
        print(f"*You found a {player.current_room.items[0].name}!*")
        pickup_item_input = input("Pick up item? --> 'y/n'").lower()
        if pickup_item_input == "y":
            item = player.current_room.items[0]
            player.take_item(item.name, player.current_room.name)

    selected_direction = input("Choose a direction --> [n, s, e, w]").lower()

    if selected_direction == "q":
        print("\n--- Thank you for playing the game ---")
        break
    elif selected_direction in possible_directions:
        try:
            player.move(selected_direction)
        except:
            print("--- You bump into a wall ---\n")

    else:
        print("\n--- Error: Please select a valid direction ---\n")
