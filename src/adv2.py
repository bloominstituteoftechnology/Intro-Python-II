 
from room import Room
from player import Player
from item import Item
import helpers

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

room_directions = {
    'outside':[{'north':'foyer'}],
    'foyer':[{'north':'overlook'}, {'south':'outside'}, {'east':'narrow'}],
    'overlook':[{'south': 'overlook'}],
    'narrow':[{'west':'foyer'}, {'north': 'treasure'}],
    'treasure':[{'south':'narrow'}]
}

 

items = {
    'Sword': Item('sword', 'A Sharp sword'),
    'Axe': Item('axe', 'A deadly Viking Battleaxe'),
    'Staff':Item('staff', 'A Magic Staff'),
    'Crystal':Item('crystal', 'A Magic Crystal')

}

print("HAY!!",room['outside'].n_to)

print()
  
print(room['outside'].name, room['outside'].description)
#
# Main
#

 # Make a new player object that is currently in the 'outside' room.
player1 = Player('Khajit',  'outside')

user_choice = (input('Which direction to Travel? North[n] South[s] East[e] West[w] press Q to quit'))

# while user_choice != 'q':
#     print(player1.name, 'is', player1.current_room )
    
#     current_room_directions = room_directions[room_type]

#     for r in current_room_directions:
#         for k ,v in r.items():
#             if k [:1].lower() == user_choice.lower():
#                 print(k)
#                 print(v)
#                 room_type = v
#                 player1.move_player(room[room_type])


   
 