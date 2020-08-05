from player import Player
from room import Room

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

#  The outside room to the north of it is the foyer from the foyer to the south is outside
#  to the north of the foyer is the overlook(this and the one above it point to each other)

#  to the east of foyer is the narrow
#  to the south of the overlook is the foyer (this and the one above it point to each other)

# to the  west of the foyer is the narrow
#  to the north of the narrow is the treausre
#  to the south of the treasure is the narrow (this and the one above it point to each other)

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
player = Player("Nonye", room["outside"])

# # Write a loop that:
# while True:
# #
# # * Prints the current room name


# print(player.location)
# #  HAVE TO FIX, NEED TO OVERRIDE THE STR METHOD

# # * Prints the current description (the textwrap module might be useful here).
# # * Waits for user input and decides what to do.
# #
# # If the user enters a cardinal direction, attempt to move to the room there.
# # Print an error message if the movement isn't allowed.
# #
# # If the user enters "q", quit the game.
#    command = input(">").split(',')
   

#    if command[0] = 'q':
#        break
#     #  if command equals equal they we will quit the game
#     elif command[0] == 'n':
#         #  check if the player can move to the north
#         # if there is, set the north room as the players location

#     elif command [0] == 's':

#     elif command[0] == 'e':

#     elif command[0] == 'w':


    #  WE NEED TO PARSE COMMANDS

while True:
    location = player.location
    print(f"Your location: {location.name}")
    print(f"{location.description}")
    nextMove = input("Enter your next move n, s, e, w or q for quit: ")

    # Setting it up for the user to make moves or quit
    if nextMove == "n":
        if location.n_to is not None:
            player.location = location.n_to
            print("You chose to go North!")
        else:
            print("There is not room that way, try again!")

    elif nextMove == "s":
        if location.s_to is not None:
            player.location = location.s_to
            print("You chose to go South!")
        else:
            print("There is not room that way, try again!")

    elif nextMove == "e":
        if location.e_to is not None:
            player.location = location.e_to
            print("You chose to go East!")
        else:
            print("There is not room that way, try again!")

    elif nextMove == "w":
        if location.w_to is not None:
            player.location = location.w_to
            print("You chose to go West!")
        else:
            print("There is not room that way, try again!")
    # Adding the ability to exit game
    elif nextMove == "q":
        print("Thank you for playing! See you soon!")
        exit()
    # Adding an error message
    else:
        print("There is not room that way, try again!")