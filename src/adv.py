from room import Room
from player import Player
# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", {'n': 'foyer'}),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", {'n': 'overlook', 'e': 'narrow', 's': 'outside'}),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", {'s': 'foyer'}),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", {'n': 'treasure', 'w': 'foyer'}),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", {'s': 'narrow'}),
}

#
# Main
#
fix_d=lambda d:"North"if d=="n"else"South"if d=="s"else"West"if d=="w"else"East"
# Make a new player object that is currently in the 'outside' room.
player = Player('outside')
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
loop = True
while(loop):
    room = rooms[player.room]
    print(room)
    valid = False
    while (not valid):
        inp = input("What would you like to do?\n")
        if inp == "q":
            loop = False
            valid = True
        elif inp in room.exits:
            player.set_room(room.exits[inp])
            valid = True
        else:
            print(f"\aYou attempt to walk {fix_d(inp)} and slam your face directly into a wall.")
            print("Maybe you shouldn't do that next time? I'd hate for your adventure to end prematurely.")
