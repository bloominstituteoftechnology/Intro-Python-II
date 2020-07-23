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

player = Player("JP", room['outside'])
game_on = True

def move(dir):
    new_dir = dir[0] + "_to"
    if hasattr(player.current_location, new_dir):
        return getattr(player.current_location, new_dir)
    else:
        print(f"The move you have specified isn't allowed. Please read the instruction again. {player.current_location.name}")
        return player.current_location

print(f"Welcome to Adventure Super Cool Game {player.name}! {player.current_location}")

while game_on:
    if player.current_location != None:
        user_input = input("Please enter direction [n] for North, [s] for South, [e] for East or [w] for West. If you wish to Quit enter [q] ")
    #when entering Q player will quit game
    if(user_input == "q"):
        print("You've quit the game. Goodbye")
        #once quit games turns off
        game_on = False
    elif user_input in ['n', 's', 'e', 'w']:
        player.current_location = move(user_input)
        print(player.current_location)
    #if a move is not allowed this will prompt asking user to enter a new move. a hint will also prompt to help user
    else:
        print(f"The move you have specified isn't ALLOWED. Pay attention to hints for choosing the direction correctly.\n{player.current_location}")

