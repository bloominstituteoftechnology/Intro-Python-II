from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run west and east. To the north, the room opens up into the grand overlook."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm. 
You can go south, or go west."""),

    'narrow':   Room("Narrow Passage", """The narrow passage splits in two here, one way bending to the north
and the other continuing east. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'library': Room("Library", """All four walls have ceiling-high shelves filled with books. 
West of you is the narrow passage you came in through."""),

    'parlor': Room("Parlor", """The room is elegant and eery. The black furniture, dark yet comfortable, seem to eminate more darkness. 
You feel a wave of sudden extreme anxiety, accompanied by the feeling of being unwelcome and unwanted. 
There are two other doors on the north and west walls."""),

    'music': Room("Music Room", """This room is strangely different from all the other rooms. You feel happy and hear calming music. 
The only door leads back east to the parlor."""),

    'kitchen': Room("Kitchen", """Straigh through on the other side is large entrance leading even further north to the dining room."""),    

    'dining': Room("Dining Room", """You see a large fireplace and a table set with crystal. To the east are double doors leading to the grand overlook."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['parlor']
room['parlor'].e_to = room['foyer']
room['parlor'].n_to = room['kitchen']
room['kitchen'].s_to = room['parlor']
room['kitchen'].n_to = room['dining']
room['dining'].s_to = room['kitchen']
room['dining'].e_to = room['overlook']
room['parlor'].w_to = room['music']
room['music'].e_to = room['parlor']
room['overlook'].s_to = room['foyer']
room['overlook'].w_to = room['dining']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['narrow'].e_to = room['library']
room['library'].w_to = room['narrow']
room['treasure'].s_to = room['narrow']

#add items into rooms 
room['library'].add_item_to_room("treasure", "You win.")
room['music'].add_item_to_room("crossbow", "A powerful weapon.")
room['dining'].add_item_to_room("key", "Unlocks secret room.")
room['overlook'].add_item_to_room("shield", "Protects you from enemies and evil spirits.")
# room['library'].add_add_to_room("treasure", "you are winning")
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Player 1", room['outside'])

player.current_room.add_item_to_room('item', 'test item')
playing = True

print(f"\n Welcome {player.name}! \n")  # welcome messages 
print(f'You are standing in the {player.current_room.name}, just north of you lies a large mansion. \n')

current_room = room['outside'] # new variable that holds the starting room. 
def determine_action(first, second=None):
    global current_room
    global playing
    if first in ['n', 's', 'e', 'w', 'd', 'q']:
        # if the command is d then print all possible directions 
        if first == 'd':
            current_room.possible_directions()
        # if the 
        elif first == 'q':
            print('Goodbye')
            playing = False
        else:
            current_room = current_room.move(first)

    elif first in ['get', 'take' 'pick'] and second in current_room.list_items():
        print(current_room.hasitem(second))
        print("first", first, "second", second)
        player.get_item(second)
        # item = self.current_room.items[index]get 
        # player.get_inventory()
    else:
        print('come agein')


while playing is True:
    selection = input("Enter direction to move >> ").lower().split(' ')
    # try: 
        # if the user enters single command and that command is a direction or q or d 
    determine_action(*selection)

    # except ValueError: 
        # print("That move isn't allowed please choose another direction. ") # Print an error message if the movement isn't allowed.

