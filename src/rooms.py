from room import Room
from monster import Monster
from item import Item
from weapon import Weapon
from lightsource import Lightsource

"""
Information on the game world: its various rooms, the objects they contain,
and how they are linked
"""

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Weapon('sword', 'An old, rusty sword', 2), Item(
                         'rope', 'A long coil of rope with a hook on the end')],
                     True,),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [], True),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [], True, True),

    'clifftop': Room("Clifftop", """From across the cliff, a dark forest covers most
of the horizon. Ahead and to the west, you see a small hut with a fire
outside. Back down south is the overlook.""", [], True),

    'shack': Room("Shack", """The shack appears to be empty, but the fire is still roaring.
Some other adventurers must have been not long ago - you can see the
remains of their meal. Besides the fire, you see they left
some of their supplies behind.""", [Lightsource('lamp', 'An old oil lamp with some fuel inside')], True),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [], True),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. On the west end of the room is a dark, narrow tunnel.
The exit is to the south.""", [], True, True),

    'dark': Room("Dark Tunnel", """You squeeze through the tunnel. Inside, it's pitch black.
You can hear some distant noises from deeper inside the caverns.""", [Item('note', """a piece of parchment
with some words scribbled on it""")], False, True),

    'final': Room("Final Chamber", """You walk through the secret door. The previous chamber was a decoy!
You are surroundeed by piles of gleaming gold coins and rubies the size of ostrich eggs. But you are not 
alone. Ahead of you, you see a terrifiying monster swivels round and glare at you with terrifying red eyes.""", [], True)
}

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['overlook'].n_to = rooms['clifftop'] # todo restrict this
rooms['clifftop'].w_to = rooms['shack']
rooms['clifftop'].s_to = rooms['overlook']
rooms['shack'].e_to = rooms['clifftop']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']
rooms['treasure'].w_to = rooms['dark']
rooms['treasure'].n_to = rooms['final']
rooms['dark'].e_to = rooms['treasure']
