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

# Items
book = Item("book", "Contains a treasure map.")
crossbow = Item("crossbow", "A powerful weapon.")
key = Item("key", "Unlocks secret room.")
shield = Item("shield", "Protects you from enemies and evil spirits.")

room['library'].items = [book]
room['music'].items = [crossbow, shield]
room['dining'].items = [key]

# Main
# 
def get_next(input, room):
    key = input + "_to" 
    if hasattr(player.current_room, key):
        if getattr(room, key) is not None:
            return getattr(room, key)
    
def interpret_input(input):
    # split input
    # destructor verb, object
    # if verb is n/s/w/e
        # player moves to that room player.move() ?
    pass
# Make a new player object that is currently in the 'outside' room.
player = Player("Player 1", room['outside'])

# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# If the user enters a cardinal direction, attempt to move to the room there.

playing = True

print(f"\n Welcome {player.name}! \n")

print(f'You are standing in the {player.current_room.name}, just north of you lies a large mansion. \n')

while playing is True:
    selection = input("Enter direction to move >> ").lower().split() # * Waits for user input and decides what to do.

    # try: 

    if len(selection) == 1 and selection[0] in ['n', 's', 'e', 'w', 'd', 'q']:
        if selection[0] == 'd':
            print(f'\n{player.current_room}')
            player.current_room.possible_directions()
        elif selection[0] == 'q':
            print('Goodbye')
            playing = False
        else:
            if player.current_room.new_room(f'{selection[0]}_to') != None:
                new = player.current_room.new_room(f'{selection[0]}_to')
                print(new)
                # player.move(new)
                print(player.current_room)
            else:
                print(" There is nothing in that direction. try 'd' to see available directions")
                
    elif len(selection) == 2:
        if selection[0] in ['get', 'take' 'pick'] and player.current_room.hasitem(selection[1]):
            print(selection[1])
            index = player.current_room.list_items().index(selection[1])
            player.get_item(player.current_room.items[1])
            player.get_inventory()
            continue
        else:
            print(selection)
            print("That item is not in the room. ")
            player.current_room.list_items()
    else: 
        print('Invalid input. try n, s, e, w in order to move or enter command "get book" to collect items')
    # except ValueError: 
    #     print("That move isn't allowed please choose another direction. ") # Print an error message if the movement isn't allowed.

# If the user enters "q", quit the game.
