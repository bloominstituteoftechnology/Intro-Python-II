from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),
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

player = Player("Player1", room['outside'])

#Items Outside
rock = Item("Rock", "This is a rock.")
branch = Item("Branch", "Sharp branch")

room['outside'].items.append(rock)
room['outside'].items.append(branch)

# Items Foyer
wrench = Item("Rusty Wrench", "A Wrench that hasn't been used in a long time")
screwdriver = Item("Screwdriver", "Can be used on screws")

room['foyer'].items.append(wrench)
room['foyer'].items.append(screwdriver)

# Items Overlook
key = Item("Key", "Can be used to unlock a door")

room['overlook'].items.append(key)

# Items Narrow
bag = Item("Large bag", "Someone must've dropped this")

room['narrow'].items.append(bag)

# Items Treasure
coins = Item("gold coins", "Is that Jon Snow on the face?")
gauntlet = Item("gauntlet", "Similar to that of Thanos")
mirror = Item("mirror", "Is it saying I'm a treasure?")

room['treasure'].items.append(coins)
room['treasure'].items.append(gauntlet)
room['treasure'].items.append(mirror)

#
# Main
#

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

valid_directions = ['n', 's', 'e', 'w']

print(player.current_room)

while True:
    cmd = input("-> ")
    if cmd in valid_directions:
        player.travel(cmd)
    elif cmd == "q":
        print("Goodbye!")
        break
    else:
        print("command invalid.")
