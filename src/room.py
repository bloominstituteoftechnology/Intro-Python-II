# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__ (self, name, description):
        self.name = name
        self.description = description
        self.inventory = []

o = Room("Outside", "North of you, the cave mount beckons")
f = Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""")
t =  Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""")
ov = Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""")
n = Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""")


o.n_to = f
f.s_to = o
f.n_to = ov
f.e_to = n
ov.s_to = f
n.w_to = f
t.s_to = n


'''
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#'''