from room import Room
from item import Weapon, Item

def build_rooms():
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

    return room


def link_rooms(room):
    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

def populate_rooms(room):
    pass

def stock_rooms(room):
    sword = Item(1, 'sword', 'a double edged weapon with a handle')
    lantern = Item(2, 'lantern', 'An old mining lantern')
    hat = Item(3, 'hat', 'a miners\' cap')
    rope = Item(4, 'rope', '50 ft of hempen rope')
    chest =Item(5,'chest', 'A giant empty chest. How do you plan on carrying this?')
    room['outside'].contents = [sword]
    room['foyer'].contents = lantern
    room['overlook'].contents = hat
    room['narrow'].contents = rope
    room['treasure'].contents = chest