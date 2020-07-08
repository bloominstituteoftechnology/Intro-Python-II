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
# * Prints the current description 
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

player = Player('Buzzy', 'outside')

is_playing = True

def find_key(value):
    for k, v in room.items():
        if value == v:
            return k

def find_item(item):
    for i in room[player.current_room].items:
        if item.name == i:
            return i

while is_playing:
    print(room[player.current_room])
    #TODO : the textwrap module??
    command = input('Where do you want to go? N, E, S, W ? >> ').lower().split()
    if len(command) == 1:
        if command[0] == 'n':
            if room[player.current_room].n_to == None:
                command = input("Can't get there from here. Try E, S, or W >> ")
            else:
                player.current_room = find_key(room[player.current_room].n_to)
        elif command[0] == 's':
            if room[player.current_room].s_to == None:
                command = input("Can't get there from here. Try N, W, or E >> ")
            else:
                player.current_room = find_key(room[player.current_room].s_to)
        elif command[0] == 'w':
            if room[player.current_room].w_to == None:
                command = input("Can't get there from here. Try N, S, or E >> ")
            else:
                player.current_room = find_key(room[player.current_room].w_to)
        elif command[0] == 'e':
            if room[player.current_room].e_to == None:
                command = input("Can't get there from here. Try W, S, or N >> ")
            else:
                player.current_room = find_key(room[player.current_room].e_to)
        elif command[0] == 'q':
            is_playing = False
        else:
            command = input('Please put in a valid direction: N, S, E, or W. >> ')
    elif len(command) == 2:
        if command[0] == 'get' or command[0] == 'take':
            # Check if item exists
            if command[1] in room[player.current_room].items:
                # Add to player inventory
                player.add_item(find_item(command[1]))
            else:
                command = input('Item does not exist in this room. Keep looking. >> ')
        else:
            command = input('Please enter a valid input. You may get or take an item, or you may enter a direction to move in: N, S, E, or W >> ')
    else:
        command = input('Please enter a valid input. You may get or take an item, or you may enter a direction to move in: N, S, E, or W >> ')
