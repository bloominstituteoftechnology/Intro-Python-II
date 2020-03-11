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
#           |ovlk|trsr|
#           | foy|nrrw|
#           | out|

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
CJ = Player("Carlo", room['outside'])

# 4 cardinal direction INPUT pass to room instance
# if the room > 0 then pass the room to the player elif n_to == 0 then return "there's nothing over there try again" and input
#     n_to
#     e_to
#     s_to
#     w_to
#     they PRINT the player's NAME and current ROOM
#     they PRINT error IF string does not equal n, s, e, or w 
#     they PRINT error IF room does not exist

# user inputs n 
#     north exists so room.n_to returns viable room to adv condition
#         the loop updates the player's current_room with that variable
#             the adv.py REPL prints the player's name and current_room

going_toward = input("which direction are you headed? ")
#while NOT q, continue running file
while not going_toward == "q":
    # going_toward = input("which direction are you headed? ")
    if going_toward not in ["n", "s", "e", "w"]:
        print("there's nutin o'er yonder!!")
    elif going_toward == "n" and CJ.current_room.n_to != "default":
        CJ.current_room = CJ.current_room.n_to
        print(f"{CJ.current_room.name} \r\n {CJ.current_room.descr}")
        going_toward = input("which direction are you headed? ")
    elif going_toward == "s" and CJ.current_room.s_to != "default":
        CJ.current_room = CJ.current_room.s_to
        print(f"{CJ.current_room.name} \r\n {CJ.current_room.descr}")
        going_toward = input("which direction are you headed? ")
    elif going_toward == "e" and CJ.current_room.e_to != "default":
        CJ.current_room = CJ.current_room.e_to
        print(f"{CJ.current_room.name} \r\n {CJ.current_room.descr}")
        going_toward = input("which direction are you headed? ")
    elif going_toward == "w" and CJ.current_room.w_to != "default":
        CJ.current_room = CJ.current_room.w_to
        print(f"{CJ.current_room.name} \r\n {CJ.current_room.descr}")
        going_toward = input("which direction are you headed? ")
    elif CJ.current_room.n_to == "default" or CJ.current_room.s_to == "default" or CJ.current_room.e_to == "default" or CJ.current_room.w_to == "default":
        print("what exactly are you trying to do")
        going_toward = input("which direction are you headed? ")
# Make a new player object that is currently in the 'outside' room.


print(f"{CJ.name} quit the game")

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
