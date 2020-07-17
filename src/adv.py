from room import Room
from player import Player
from item import Item 

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

player = Player("Ruby", room['outside'])

rock = Item("Rock", "Just a rock.")
sword = Item("Sword", "A magical sword.")
potion = Item("Potion", "Restore's health.")
rubies = Item("Rubies", "Not gold but still worth keeping.")
scroll = Item("Scroll", "Left over by the previous adventurers.")

room["outside"].room_items.append(rock) 
room["outside"].room_items.append(potion)
room["foyer"].room_items.append(sword)
room["overlook"].room_items.append(potion)
room["overlook"].room_items.append(rock) 
room["narrow"].room_items.append(rubies)
room["treasure"].room_items.append(scroll)

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

directions = ['n', 's', 'e', 'w']

print(player.room)

while True:
    cmd = input("Please enter a direction : ")
    if cmd in directions:
        player.move(cmd)
    elif cmd == 'q':
        print("Thanks for Playing! :)")
        break
    else:
        print("Oops! Choose a valid direction.")