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
player = Player(room['outside']) #give entire outside instance
 
def try_direction(direction, current_room):
    #if/else logic could go here instead, but is less DRY
    attribute = direction + '_to'

    #see if the inputted direction is one we can move to w/ built in method
    if hasattr(current_room, attribute):
        return getattr(current_room, attribute) #fetch room w/ built in python methods
    else:
        print("This direction is unavailable!")
        return current_room
# Write a loop that:
while True:
    # * Prints the current room name
    #-->look up room in dictionary...
    print(player.current_room.name)

    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)
    # * Waits for user input and decides what to do.
    #d for direction
    d = input("\n>").lower()[0]

    

            
    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed. SEE try_direction
    #ALLOW : North, South, East, West, north, south, east, west, N, S, E, W, n, s , e, w

    # If the user enters "q", quit the game.
    if d =='q':
        print("Thanks for playing!")
        break

    player.current_room = try_direction(d, player.current_room)

    #NOTES FROM INSTRUCTOR HOUR/ELISSA
        #did user enter valid direction?
        #Yes? -
        #   is there anything IN that direction?
        #       Yes? - move in that diredction, print new room info
        #       No? - Print out message stating nothing in that direction
        #   No? - Print an error message if the movement isn't allowed.
        #continue promting for input



