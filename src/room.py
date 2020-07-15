# Implement a class to hold room information. This should have name and
# description attributes.

from collections import namedtuple

class Room:
    n_to = []
    s_to = []
    e_to = []
    w_to = []
    
    def __init__(self, name, description):
        self.name = name
        self.description = description

if __name__ == '__main__':
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
    room['outside'].n_to = room['foyer']

    print(room['outside'].n_to.name)