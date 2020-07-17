# Implement a class to hold room information. This should have name and
# description attributes.

from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.e_to = None
        self.w_to = None
        self.n_to = None
        self.s_to = None
        self.items = []
    def add_items(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items[0]: 
            self.items[0].remove(item)
        

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to th
e north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

room['outside'].add_items(['plant', 'playground', 'pond'])
room['foyer'].add_items(['sofa', 'tv', 'drawer'])
room['overlook'].add_items(['dinning table', 'painting'])
room['narrow'].add_items(['lights'])
room['treasure'].add_items(['treasure chest'])


# user_input = input('Press keys (n, s, e, w )to move the player\nOR press get item_name or drop item_name: ')
# print('*******'*10)
# if len(user_input.split()) == 2:
#             if user_input.split()[0] == 'get':
#                 if user_input.split()[1] in (player.current_room.items):
#                     print('Items in the Room--', (*player.current_room.items))
# else:
#     print('no')
# print(room['outside'])
# print(room['outside'].name)
# print(room['outside'].description)
print(room['outside'].items)
#print(room['outside'].remove_item('pond'))
print(room['outside'].items)
#room_1=Room ('abd', 'skmdksmdl')
#items= Item('sword', 'Be carefull')  

#room_1.room_item(['a', 'b', 'c'])
#print(room_1.items_name)