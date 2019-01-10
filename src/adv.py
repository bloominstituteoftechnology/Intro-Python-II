from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

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
player_name = input("    Please enter player name: ")
player = Player(player_name, room['outside'])

# Write a loop that:
while True:
# * Prints the current room name
    print(f'    {player.name} is currently in the {player.currentRoom.name}.')
# * Prints the current description (the textwrap module might be useful here).
    print(f'    {player.currentRoom.desc}')
# * Waits for user input and decides what to do.
    print(f'''    Your options:
        n to go North
        s to go South
        e to go East
        w to go West
        q  to   Quit
    ''')
    decision = input('    Where would you like to go? ')
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
    if (len(decision) == 1):
        if (not (decision in ['n','s','e','w', 'q'])):
            print(f'    {decision} is not an option, try again.')
        elif (decision == 'n'):
            try:
                player.currentRoom = player.currentRoom.n_to
            except AttributeError:
                print(f'    {player.name} cannot move north, try again.')
        elif (decision == 's'):
            try:
                player.currentRoom = player.currentRoom.s_to
            except AttributeError:
                print(f'    {player.name} cannot move south, try again.')
        elif (decision == 'e'):
            try:
                player.currentRoom = player.currentRoom.e_to
            except AttributeError:
                print(f'    {player.name} cannot move east, try again.')
        elif (decision == 'w'):
            try:
                player.currentRoom = player.currentRoom.w_to
            except AttributeError:
                print(f'    {player.name} cannot move west, try again.')
# If the user enters "q", quit the game.
        

