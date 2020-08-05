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
player = Player(room['outside'])
starting_room = 1
current_room = 1
outside = 1
overlook_room = 3
foyer_room = 2
treasure_room = 5
narrow_room = 4
# Write a loop that:
while True:
   # Prints the current room name
    
    command = input("> Input n, e, s, or w to move that direction ").split(',')

    if command[0] == 'q':
        break     
    elif command[0] == 'n':
        if current_room == 2:
            current_room = 3
            overlook_room = Player(room['overlook'])
            print(overlook_room.location)
        elif current_room == 1:
            foyer_room = Player(room['foyer'])
            current_room = 2
            print(foyer_room.location)
        elif current_room == 5:
            print('You can only go south')         
        elif current_room == 4:
            current_room = 5
            treasure_room = Player(room['treasure'])
            print(treasure_room.location)
        elif current_room == 3:
            print("You can only move South")
    elif command[0] == 's':
        outside_room = Player(room['outside'])
        if current_room == 1:
            print('You can only move North')
            current_room = 1
        elif current_room == 2:
            current_room = 1
            outside_room = Player(room['outside'])
            print(outside_room.location)
        elif current_room == 5:
            current_room = 4
            narrow_room = Player(room['narrow'])
            print(narrow_room.location)
        elif current_room == 4:
            print('You can only move north or West')
        elif current_room == 3:
            current_room = 2
            foyer_room = Player(room['foyer'])
            print(foyer_room.location)
    

    elif command[0] == 'e':
        if current_room == 2:
             current_room = 4
             narrow_room = Player(room['narrow'])
             print(narrow_room.location)
        else:
            print('You cannot move east')


    elif command[0] == 'w':
        if current_room == 4:
            current_room = 2
            foyer_room = Player(room['foyer'])
            print(foyer_room.location)
        else:
            print("You can't move West")

# * 
    
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
