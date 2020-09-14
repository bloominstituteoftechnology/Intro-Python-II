from room import Room
from player import Player

# Declare rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mouth beckons",
                    ["Small rocks"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 
                    []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    []),
}


# Link rooms together

rooms['outside'].n_to = 'foyer'
rooms['foyer'].s_to = 'outside'
rooms['foyer'].n_to = 'overlook'
rooms['foyer'].e_to = 'narrow'
rooms['overlook'].s_to = 'foyer'
rooms['narrow'].w_to = 'foyer'
rooms['narrow'].n_to = 'treasure'
rooms['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player("Steve", "outside", "Rock")

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

playing = True

while playing:
    current_room = rooms[player.current_room]
    print(f"-----\n{current_room.name}\n{current_room.description}")

    cmd = input(" >>> ")

    if cmd in ["n", "s", "e", "w"]:
        if hasattr(current_room, f"{cmd}_to"):
            player.current_room = getattr(current_room, f"{cmd}_to")
            print(f"Moving {cmd.upper()}")
        else:
            print(f"Can't move {cmd.upper()}")

    elif cmd == "q":
        playing = False
        print("Goodbye!")
    else:
        print(f"I do not understand {cmd}")