# from room import Room

# # Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }


# # Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

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

def north():
    return 'You moved North'
def south():
    return 'You moved South'
def east():
    return 'You moved East'
def west():
    return 'You moved West'
def quiter():
    return 'It has been fun. See you nex time.'

def cmd_switch(argument):
    error = """Invalid command please use one of the following:
'n' to travel north
's' to travel south
'e' to travel east
'w' to travel west
'q' to quit the game"""

    switcher = {
        'n': north,
        's': south,
        'e': east,
        'w': west,
        'q': quiter
    }

    function = switcher.get(argument, error)

    return function()


def main():

    cmd = input('>> ')
    print(cmd_switch(cmd))

    if cmd == 'q':
        return False
    else:
        return True

if __name__ == "__main__":
    print('Welcome to Lambda Quest')
    while main():
        continue
