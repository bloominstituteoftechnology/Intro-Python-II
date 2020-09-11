from room import Room
from player import Player
from item import Item

import textwrap

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

#
# Link rooms together
#
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Items
#
sword = Item("Sword", "Master sword, kills anything in one swing")
map = Item("Map", "Map of the entire world to aid you in your adventures")
slingshot = Item("Slingshot", "Practice your aim, a hit in the right location will keep you alive")
coffee = Item("Coffee", "This magical recipe will refill all your energy")
crossbow = Item("Crossbow", "Not as powerful as the sword but still a good weapon to have")

#
# Add items to room
#
room['outside'].items.append(map)
room['outside'].items.append(coffee)
room['foyer'].items.append(coffee)
room['foyer'].items.append(slingshot)
room['overlook'].items.append(coffee)
room['narrow'].items.append(crossbow)
room['narrow'].items.append(coffee)
room['treasure'].items.append(sword)

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("*******************************************************************")
playerName = input("Welcome to your new adventure, what is your name? \n")
print(f"Welcome {playerName}")
print("*******************************************************************")
newPlayer = Player(playerName, room["outside"])
print(f"{newPlayer.name} you are currently in {newPlayer.current_room}\n")
wrappedDescription = textwrap.wrap(newPlayer.current_room.description)
for line in wrappedDescription:
    print(line)

newPlayer.current_room.print_items()

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

directions = ['n', 's', 'w', 'e']

while True:
    direction = input("Enter the direction you want to go in i.e 'n', 's', 'e', 'w' : or 'other' for other instructions ")

    currentLocation = newPlayer.current_room

    if direction in directions:
        newPlayer.move(direction)

    elif direction == 'other':
        print("*******************************************************************")
        print("Enter 'i' if you want to see your inventory\n")
        print("Enter take <item name> if you want to pick up the item in the room\n")
        print("Enter drop <item name> if you want to drop the item from your inventory")
        print("*******************************************************************\n")
    elif direction == 'i':
        newPlayer.display_items()
    elif direction == 'take sword':
        newPlayer.add_item(sword)
        newPlayer.current_room.take_item(sword)
    elif direction == 'take map':
        newPlayer.add_item(map)
        newPlayer.current_room.take_item(map)
    elif direction == 'take slingshot':
        newPlayer.add_item(slingshot)
        newPlayer.current_room.take_item(slingshot)
    elif direction == 'take coffee':
        newPlayer.add_item(coffee)
        newPlayer.current_room.take_item(coffee)
    elif direction == 'take crossbow':
        newPlayer.add_item(crossbow)
        newPlayer.current_room.take_item(crossbow)
    elif direction == 'drop sword':
        newPlayer.drop_item(sword)
        newPlayer.current_room.add_item(sword)
    elif direction == 'drop map':
        newPlayer.drop_item(map)
        newPlayer.current_room.add_item(map)
    elif direction == 'drop slingshot':
        newPlayer.drop_item(slingshot)
        newPlayer.current_room.add_item(slingshot)
    elif direction == 'drop coffee':
        newPlayer.drop_item(coffee)
        newPlayer.current_room.add_item(coffee)
    elif direction == 'drop crossbow':
        newPlayer.drop_item(crossbow)
        newPlayer.current_room.add_item(crossbow)
    elif direction == 'q':
        print("Thanks for playing")
        break
    
    else:
        print("You didn't enter a proper direction. i.e 'n', 's', 'e', 'w' ")