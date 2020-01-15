from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room('outside', "Outside Cave Entrance",
                     "North of you, the cave mouth beckons"),

    'foyer':    Room('foyer', "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room('overlook', "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room('narrow', "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room('treasure', "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['outside'].exits = 'N'

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].exits = ['N, S, and E']

room['overlook'].s_to = room['foyer']
room['overlook'].exits = 'S'

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].exits = 'N and W'

room['treasure'].s_to = room['narrow']
room['treasure'].exits = 'S'
#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_one = Player('outside')
# Write a loop that:
#
# * Prints the current room name
print(room[player_one.curr_room].name+'\n')
# * Prints the current description (the textwrap module might be useful here).
print(room[player_one.curr_room].description)
print('Exits are: '+room[player_one.curr_room].exits)
# Print Map


def print_map():
    map_id = room[player_one.curr_room].id
    top = '\u2554'+'\u2550'*13+'\u2557\n'
    mid = '\u2551'+' '*13+'\u2551\n'
    mid_name = '\u2551'+map_id+' '*(13-len(map_id))+'\u2551\n'
    mid_player = '\u2551'+' '*6+'@'+' '*6+'\u2551\n'
    mid_comp = mid_name+mid+mid_player+mid*2
    bot = '\u255A'+'\u2550'*13+'\u255D\n'
    print(top+mid_comp+bot)


# print_map()

# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
