from room import Room
import item

def build_rooms():
    room = {
            'outside':  Room("Outside Cave Entrance",
                "North of you, the cave mount beckons", {'sword': item.Sword(1)}),

            'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
                passages run north and east.""", {"lantern": item.Lantern(2)}),

            'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
                into the darkness. Ahead to the north, a light flickers in
                the distance, but there is no way across the chasm.""",{'hat': item.Item(3, 'hat', 'a miners\' cap')}),

            'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
                to north. The smell of gold permeates the air.""",{'rope': item.Item(4, 'rope', '50 ft of hempen rope')}),

            'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
                chamber! Sadly, it has already been completely emptied by
                earlier adventurers. The only exit is to the south.""",{'chest': item.Item(5,'chest', 'A giant empty chest. How do you plan on carrying this?')}),
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

