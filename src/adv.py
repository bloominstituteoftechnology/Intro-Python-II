from room import Room
from player import Player
import textwrap

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
print("*******************************************************************")
playerName = input("Welcome to your new adventure, what is your name? \n")
print(f"Welcome {playerName}")
print("*******************************************************************")
newPlayer = Player(playerName, room["outside"])
print(f"{newPlayer.name} you are currently in {newPlayer.current_room}\n")
wrappedDescription = textwrap.wrap(newPlayer.current_room.description)
for line in wrappedDescription:
    print(line)
        
print("*******************************************************************\n")

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

directions = ['n', 's', 'w', 'e']

while True:
    direction = input("Enter the direction you want to go in i.e 'n', 's', 'e', 'w' :  ")

    currentLocation = newPlayer.current_room

    if direction in directions:
        newPlayer.move(direction)
    elif direction == 'q':
        print("Thanks for playing")
        break
    
    else:
        print("You didn't enter a proper direction. i.e 'n', 's', 'e', 'w' ")