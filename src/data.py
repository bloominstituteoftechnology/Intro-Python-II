from room import Room
from item import Item
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ""),
}

# Declare all items

item = {
    'sword': Item("sword", "pretty cool sword"),

    "shield": Item("shield", "pretty sturdy shield"),

    "boots": Item("boots", "a pair of pretty fashionable boots"),

    "armor": Item("armor", "a pretty weird looking suit"),

    "helmet": Item("helmet", "pretty regal looking headpiece")
}

# declare player

# Make a new player object that is currently in the 'outside' room.

player = Player(room["outside"], "")
