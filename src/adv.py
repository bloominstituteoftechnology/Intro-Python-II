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
player = Player("Chris", room['outside'])

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

while True:
    current_room = player.location
    print(f"Your location: {location.name}")
    print(f"{current_room.description}")
    nextMove = input("Enter your next move n, s, e, w or q for quit: ")

    # Setting it up for the user to make moves or quit
    if nextMove == "n":
        if current_room.n_to is not None:
            player.current_room = current_room.n_to
            print("You chose to go North!")
        else:
            print("There is not room that way; please try again!")
    
    elif nextMove == "s":
        if current_room.s_to is not None:
            player.current_room = current_room.s_to
            print("You chose to go South!")
        else:
            print("There is not room that way; please try again!")
    
    elif nextMove == "e":
        if current_room.e_to is not None:
            player.current_room = current_room.e_to
            print("You chose to go East!")
        else:
            print("There is not room that way; please try again!")
    
    elif nextMove == "w":
        if current_room.w_to is not None:
            player.current_room = current_room.w_to
            print("You chose to go West!")
        else:
            print("There is not room that way; please try again!")
    # Adding the ability 
    elif nextMove == "q":
        print("Thank you for playing! See you soon!")
        exit()
    # Adding an error message
    else:
        print("Please enter n, s, e, w to make a move or q to quit!")
