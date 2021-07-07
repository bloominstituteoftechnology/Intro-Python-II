from room import Room
from player import Player
from item import Item
# Declare all the rooms

items = {
    'sword': Item("sword", 'Andúril, also called the Flame of the West, is the reforged sword from the shards of Narsil.'),
    'ring': Item("ring", 'The One Ring was one of the most powerful artifacts ever created in Middle-earth.')
}

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items['ring']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items['sword']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together
#accessing room instance via bracket notation so now access class to attributes via dot notation.
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
player_name = input("Enter the name of your character: ")
player = Player(player_name, room['outside'])

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


def try_direction(direction, current_room):
    attribute = direction + '_to'
    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print("You can not go that way.  Please try again.")
        return current_room

while True:
    print(player.current_room.name)
    print(player.current_room.description)

    c = input("\n>").lower().split()

    if len(c) == 1:
        c = c[0][0]
        player.current_room = try_direction(c, player.current_room)

    elif len(c) == 2:
        action = c[0]
        item = c[1]
        #if item is in room, remove and add it to inv
        if action == "take":
            if item in player.current_room.items:
                player.current_room.items.remove(item)
                player.inventory.append(item)
                print(f"{item.name} was added to your inventory.")

        if action == "drop":
            if item in player.inventory:
                player.inventory.remove(item)
                player.current_room.items.append(item)
                print(f"You dropped the {item.name}")

    elif c == 'q':
        break

    else:
        print("I do not understand that.  Please try again")
        continue
    
    



"""
while True:
    action = input("What is your next move? ").lower()

    if action == 'n':
        try:
            player.room = player.room.n_to
        except AttributeError:
            print("You can not move that direction.  Try again.")
    elif action == 'e':
        try:
            player.room = player.room.e_to
        except AttributeError:
            print("You can not move that direction.  Try again.")
    elif action == 's':
        try:
            player.room = player.room.s_to
        except AttributeError:
            print("You can not move that direction.  Try again.")
    elif action == 'w':
        try:
            player.room = player.room.w_to
        except AttributeError:
            print("You can not move that direction.  Try again.")
    elif action == 'q':
        break 
    else:
        print(f"That is not a valid action.")
"""

