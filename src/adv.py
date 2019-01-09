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

room['outside'].n_to = 'foyer'
room['foyer'].s_to = 'outside'
room['foyer'].n_to = 'overlook'
room['foyer'].e_to = 'narrow'
room['overlook'].s_to = 'foyer'
room['narrow'].w_to = 'foyer'
room['narrow'].n_to = 'treasure'
room['treasure'].s_to = 'narrow'

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
from player import Player

player = Player() #if no input, player is initialized with currentRoom='outside'

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

currentRoom = room[player.currentRoom]
roomName = currentRoom.name
print(f'Current location: {roomName}')
roomDesc = currentRoom.description
print(roomDesc)
print('Where do you want to go?')
direction = input('Enter a direction:')


if direction == 'n' and type(currentRoom.n_to) is str:
    player.currentRoom = currentRoom.n_to
    print(player.currentRoom)
elif direction == 's' and len(currentRoom.s_to) > 0:
    player.currentRoom = currentRoom.s_to
elif direction == 'e' and type(currentRoom.e_to) is str:
    player.currentRoom = currentRoom.e_to
elif direction == 'w' and type(currentRoom.w_to) is str:
    player.currentRoom = currentRoom.w_to
elif ['n', 's', 'e', 'w'].count(direction) == 0: 
    print('Use one of [n, s, e, w]')
else:
    print("You can't go that way!")
    
