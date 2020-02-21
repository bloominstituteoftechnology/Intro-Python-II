from room import Room
from player import Player
from item import Item
import textwrap

# Declare all the rooms

room = {
    'outside':Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),
    'foyer':Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook':Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure':Room("Treasure Chamber", """You've found the long-lost treasure
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
player_1 = Player("1", room['outside'])
wrappedDesc = textwrap.wrap(player_1.current_room.desc)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

print(f"Player's current room: {player_1.current_room.name}")
print(f"Current room desc: {wrappedDesc}")
userInput = input("Select one of the following direction to move the player. \nN (north), S (south), E (east), W (west):\n ---> ").lower()

# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

def askNextMove():
    return input("What's the next move. Please select a direction:\n ---> ").lower()

def cantBeInThisRoom(room):
    return input(f"You can't move to {room}. Please make another choice:\n ---> ").lower()

while userInput is not None:
    if userInput == "n":
        north_room = player_1.current_room.n_to
        if north_room is not None:
            player_1.current_room = north_room
            userInput = askNextMove()
        else:
            userInput = cantBeInThisRoom("north")
    elif userInput == "s":
        south_room = player_1.current_room.s_to
        if south_room is not None:
            player_1.current_room = south_room
            userInput = askNextMove()
        else:
            userInput = cantBeInThisRoom("south")
    elif userInput == "e":
        east_room = player_1.current_room.e_to
        if east_room is not None:
            player_1.current_room = east_room
            userInput = askNextMove()
        else:
            userInput = cantBeInThisRoom("east")
    elif userInput == "w":
        west_room = player_1.current_room.w_to
        if west_room is not None:
            player_1.current_room = west_room
            userInput = askNextMove()
        else:
            userInput = cantBeInThisRoom("west")
    elif userInput == "q":
        print(f'You exited the game. Sorry to see you go. Bye!')
        break
    else:
        if len(userInput) == 0:
            userInput = input("Please enter a value from N, S, E, W. Make a selection:\n ---> ")
        elif len(userInput) > 1:
            userInput = input("You can only select a value from N, S, E, W. Make a selection:\n ---> ")
        else:
            userInput = input("This movement is not allowed. You can only select a value from N, S, E, W:\n ---> ").lower()

