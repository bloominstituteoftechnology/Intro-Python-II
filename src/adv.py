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
player_1 = Player("Player_1", room["outside"])

# Write a loop that:
while player_1.current_room:
    # * Prints the current room name
    print("---------------------------------------------")
    print("You are now in the room:\n",player_1.current_room.name)
    # * Prints the current description (the textwrap module might be useful here).
    print("Description:\n",player_1.current_room.description)
    print("---------------------------------------------")
    # * Waits for user input and decides what to do.
    move = input("Move North (n), South (s), East (e) or West (w), or press 'q' to exit:\n").lower()
    print("---------------------------------------------")
    # If the user enters a cardinal direction, attempt to move to the room there.
    if move == 'n':
        player_1.current_room = player_1.current_room.n_to
    elif move == 's':
        player_1.current_room = player_1.current_room.s_to
    elif move == 'e':
        player_1.current_room = player_1.current_room.e_to
    elif move == 'w':
        player_1.current_room = player_1.current_room.w_to
    # If the user enters "q", quit the game
    elif move == 'q':
        print("Have a nice day!")
        break
    # Print an error message if the movement isn't allowed.
    else:
        move = input("Please select 'n', 's', 'e', or 'w' to move to another room, \
or press 'q' to exit the game:\n").lower()
    # Print an error if the player tries to move where there is no room
    if not player_1.current_room:
        move = input("There is nothing in there. Game Over!")
