from room import Room
from player import Player
# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount beckons"""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. 
    Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. 
    Ahead to the north, a light flickers in the distance, 
    but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. 
    The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! 
    Sadly, it has already been completely emptied by earlier adventurers. 
    The only exit is to the south."""),
}

# Link rooms together
room['outside'].n_to = room['foyer'] #outside N to Foyer
room['foyer'].s_to = room['outside'] #foyer S to Outside
room['foyer'].n_to = room['overlook'] #foyer N to Overlook
room['foyer'].e_to = room['narrow'] #foyer e to Narrow
room['overlook'].s_to = room['foyer']#overlook s to foyer
room['narrow'].w_to = room['foyer']#narrow w to foyer
room['narrow'].n_to = room['treasure']#narrow north to treasure
room['treasure'].s_to = room['narrow']#treasure south to narrow

#
# Main
#
# Make a new player object that is currently in the 'outside' room.
new_player = Player("Brandy", room['outside'])
#------------------------------------------------------------------------------
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
#----------------------------------------------------------------------------
#loop that
    #waits for the user input and decides what to so [ n s w e ]
        #if user goes n check to see if allowed
            # if allowed, move north
            # if not allowed, error message
        #if user goes s check to see if allowed
            # if allowed, move south
            # if not allowed, error message
        #if user goes w check to see if allowed
            # if allowed, move west
            # if not allowed, error message
        #if user goes e check to see if allowed
            # if allowed, move east
            # if not allowed, error message
        #if not allowed, error message
        #if user types 'q', end game

def check_move(move):
    current = new_player.room
    if current.__dict__[f'{move}_to'] == None:
        print("\n You can't move that way, something blocks your path.\n")
    else:
        new_player.room = current.__dict__[f'{move}_to']

while True:
    current = new_player.room
    movement_choice = ['n', 's', 'w', 'e']
    print(f"\n Welcome, {new_player.name}! Your current location is {current}.")
    print(f"------------------------------------------")
    choice = input(f"'What would you like to do?' | Move: [n, s, w, e] | Quit: [q] |\n")

    if choice in movement_choice:
        check_move(choice)
        print(f"------------------------------------------")
    elif choice == "q":
        print("Quitters never win, & winners never quit- \n Farewell for now ... \n")
        exit()
    else:
        print("\n You can't move that way, something blocks your path. \n")