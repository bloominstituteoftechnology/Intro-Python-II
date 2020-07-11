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

def north(plyr):
    toroom = plyr.current_room.n_to
    if toroom:
        plyr.current_room = toroom
        return 'You move to:'
    else:
        return 'There is nothing to the north of you'
def south(plyr):
    toroom = plyr.current_room.s_to
    if toroom:
        plyr.current_room = toroom
        return 'You move to:'
    else:
        return 'There is nothing to the south of you'
def east(plyr):
    toroom = plyr.current_room.e_to
    if toroom:
        plyr.current_room = toroom
        return 'You move to:'
    else:
        return 'There is nothing to the east of you'
def west(plyr):
    toroom = plyr.current_room.w_to
    if toroom:
        plyr.current_room = toroom
        return 'You move to:'
    else:
        return 'There is nothing to the west of you'
def quiter(plyr):
    '''Accepts player object strictly for conformity'''
    return 'It has been fun. See you nex time.'
def error(plyr):
    '''Accepts player object strictly for conformity'''
    err_msg = """Invalid command please use one of the following:
'n' to travel north
's' to travel south
'e' to travel east
'w' to travel west
'q' to quit the game"""
    return err_msg

def cmd_switch(argument):
    '''
    A quick switch block for processing user input
    '''
    switcher = {
        'n': north,
        's': south,
        'e': east,
        'w': west,
        'q': quiter
    }

    function = switcher.get(argument, error)

    # returning the reference to the function
    return function

def main():
    
    print('Welcome to Lambda Quest')

    player = Player('Felix Peone')
    player.current_room = room['outside']

    while True:
        print(player.current_room)
        cmd = input('>> ')
        func = cmd_switch(cmd)
        print(func(player))

        #The conditional to break our loop, must remain at end of loop
        if cmd == 'q':
            break

if __name__ == "__main__":
    main()
