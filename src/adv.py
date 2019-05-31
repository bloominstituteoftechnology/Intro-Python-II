import os
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
player = Player('Player 1', 'outside')
print(f"Welcome {player.name}")
print("Enter q or Q to quit the game.")
print('')
# Write a loop that:
#
good_move = True 
while True:
    if good_move:
        os.system('clear')
    good_move = True
# * Prints the current room name
    print(f"Current Location: {room[player.cur_room]}")
# * Prints the current description (the textwrap module might be useful here).
    print(room[player.cur_room].description)
# * Waits for user input and decides what to do.
    action = input("Where would you like to go? ")
#
# If the user enters "q", quit the game.
    if action.lower() == 'q':
        os.system('clear')
        print("Thank you for playing!\n")
        exit()
# If the user enters a cardinal direction, attempt to move to the room there.
    elif action.lower() == 'n':
        if not room[player.cur_room].n_to == None:
            room[player.cur_room] = room[player.cur_room].n_to
        else:
            good_move = False
            os.system('clear')
            print(f"\nThere is no room to the North of {room[player.cur_room]}\n")
    elif action.lower() == 'e':
        if not room[player.cur_room].e_to == None:
            room[player.cur_room] = room[player.cur_room].e_to
        else:
            good_move = False
            os.system('clear')
            print(f"\nThere is no room to the East of {room[player.cur_room]}\n")
        # room[player.cur_room] = room[player.cur_room].e_to
    elif action.lower() == 's': 
        if not room[player.cur_room].s_to == None:
            room[player.cur_room] = room[player.cur_room].s_to
        else:
            good_move = False
            os.system('clear')
            print(f"\nThere is no room to the South of {room[player.cur_room]}\n")
    elif action.lower() == 'w':
        if not room[player.cur_room].w_to == None:
            room[player.cur_room] = room[player.cur_room].w_to
        else:
            good_move = False
            os.system('clear')
            print(f"\nThere is no room to the West of {room[player.cur_room]}\n")
    else:
# Print an error message if the movement isn't allowed.
        print("\nPlease enter valid direction. (n, e, s, w)\n")
#
