from textwrap import fill, wrap
from player import Player
from room import Room

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", {'n': 'foyer'}),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", {'s': 'outside', 'n': 'overlook', 'e': 'narrow'}),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", {'s': 'foyer'}),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", {'w': 'foyer', 'n': 'treasure'}),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", {'s': 'narrow'}),
}


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


player = Player("outside")

user_input = ""

while user_input != "q":
    location = player.get_location()
    current_room = room[location]
    print(current_room.get_room())
    print(fill(current_room.get_description()))
    user_input = input("Please input which direction you would like to move: n/s/e/w or q to quit")
    if user_input in current_room.exits:
        next_room = current_room.exits[user_input]
        player.set_location(next_room)
    else:
        print("You cannot move in that direction")
    


