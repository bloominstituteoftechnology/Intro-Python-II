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
player1 = Player('JmFatal', room['outside'])
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
command = None

def possibleCommands(room):
    acceptableCommands = ['q']
    if room.n_to != None:
        acceptableCommands.append('n')
    if room.s_to != None:
        acceptableCommands.append('s')
    if room.e_to != None:
        acceptableCommands.append('e')
    if room.w_to != None:
        acceptableCommands.append('w')
    return acceptableCommands

def filterCommand(command,room):
    acceptableCommands = possibleCommands(room)
    for aCommand in acceptableCommands:
        if aCommand == command:
            global valid
            valid = True
    if valid == False:
        print('Please enter a valid command')
        print(f'Commands: {acceptableCommands}')


while command != 'q':
    print(f'\nCurrent Location: {player1.current_room.name}')
    print(f'Direction: \n{player1.current_room.description}\n')
    print(f'\nAvailable Commands: {possibleCommands(player1.current_room)}')
    command = input("Awaiting your command:").lower()
    print('----------')
    valid = False
    filterCommand(command, player1.current_room)
    if valid:
        if command == 'n':
            player1.current_room = player1.current_room.n_to
        if command == 's':
            player1.current_room = player1.current_room.s_to
        if command == 'e':
            player1.current_room = player1.current_room.e_to
        if command == 'w':
            player1.current_room = player1.current_room.w_to
