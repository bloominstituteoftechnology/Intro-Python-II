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

# Make a new player object that is currently in the 'outside' room.
player = Player("Bob", "outside")
roomKey = player.location
roomName = room[player.location].name
roomDesc = room[player.location].description
# Write a loop that:
#
while True:
    # * Prints the current room name
    print(roomName)
    # * Prints the current description (the textwrap module might be useful here).
    print(roomDesc)
    # * Waits for user input and decides what to do.
    userInput = input("Pick a direction to move: n, s, e, or w")
    # If the user enters a cardinal direction, attempt to move to the room there.
    if userInput == "n" and roomKey == 'outside':
        roomKey = room[player.location].n_to
        roomName = room[player.location].n_to.name
        roomDesc = room[player.location].n_to.description
    # If the user enters "q", quit the game.
    elif userInput == "q":
        print("You quit")
        break
    else:
        # Print an error message if the movement isn't allowed.
        print("Cannot move that direction, try another: ")
        continue
