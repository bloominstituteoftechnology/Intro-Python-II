import random
from room import Room
from item import Item, Treasure, LightSource
from player import Player
from adv_save import load_results, save_results
import os


def parse_command(com_mand):
    if com_mand == '':
        return
    cmd_words = com_mand.split()  # split into word list

    if str(cmd_words[0]).lower() == 'inventory':  # __ player inventory _
        curr_player.list_inventory()
        return


    if (curr_player.curr_room.is_light) or (curr_player.has_light()) or (curr_player.curr_room.has_light()):

        if (str(cmd_words[0]).lower() == 'get') or (str(cmd_words[0]).lower() == 'take'):        # __ get/take item __
            if len(cmd_words) > 1:
                item_name = str(cmd_words[1]).lower()
                if curr_player.curr_room.in_room(item_name):
                    curr_player.add_item(curr_player.curr_room.get_item(item_name))
                    curr_player.curr_room.remove_item(item_name)
                    return
                else:
                    print('There is no', item_name, 'here')
                    return
            else:
                print('Get what?.......')
                return



    else:
        print('Good luck finding that in the dark!')
        return


    if str(cmd_words[0]).lower() == 'drop':       # ___ drop item ___
        if len(cmd_words) > 1:
            item_name = str(cmd_words[1]).lower()
            if curr_player.in_inv(item_name):
                curr_player.curr_room.add_item(curr_player.get_item(item_name))
                curr_player.remove_item(item_name)
                return
            else:
                print('You do not have a ', item_name)
                return
        else:
            print('Drop what?.......')
            return


    # ____ fall-thru:  command is unreckognized ____
    print("Sorry, I did not understand '"+com_mand+"' Try again.\n")
    return


# Declare all the rooms
room = {
    'outside':  Room("outside the Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('matches', 'some matches')],
                     ),
    'foyer':    Room("in the Foyer",
                     """Dim light filters in from the south. Dusty passages run north and east.""",
                     [Item('flask', 'a flask'),
                      LightSource('lamp', 'a lamp'),
                      Item('bones', 'some old bones'),
                      ],
                     ),
    'overlook': Room("at the Grand Overlook",
                     """A steep cliff appears before you, falling into the darkness.
Ahead to the north, a light flickers in the distance,
but there is no way across the chasm.""",
                     [Item('flask', 'a flask of water'),
                      Item('coins', 'some old coins'),
                      ],
                     ),

    'narrow':   Room("in a narrow passage",
                     """The narrow passage bends here from west to north.
The smell of gold permeates the air.""",
                     [Item('skull', 'a skull'),
                      LightSource('torch', 'a torch'),
                      ],
                     ),
    'treasure': Room("in the Treasure Chamber!",
                     """You've found the long-lost treasure chamber!
Sadly, it has already been completely emptied by earlier adventurers
The only exit is to the south.""",
                     [Treasure('amulet', 'an amulet'),
                      Item('rum', 'a bottle of rum'),
                      ],
                     ),
    'hidden': Room("there is a strange seam in the wall You push on it and find a hidden room!",
                   """You've found a hidden treasure chamber!""",
                   [Treasure('emerald', 'an emerald jewel'),
                    Item('flask', 'a flask'),
                    ],
                   ),
    'library': Room("in a room with old books",
                    """It seems to be an old library and smells musty""",
                    [Item('scroll', 'an old scroll'),
                     Item('book', 'an old book'),
                     Item('claytablet', 'a claytablet'),
                     ],
                    )
}

# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['foyer'].w_to = room['library']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
room['library'].e_to = room['foyer']
room['library'].s_to = room['hidden']
room['hidden'].n_to = room['library']

# ___room defaults to lit... darken select rooms ____
room['library'].is_light = False
room['hidden'].is_light = False
room['treasure'].is_light = False
room['narrow'].is_light = False


# _________ init  _______________
# Instantiate new player in the 'outside' room.
curr_player = Player("Player1", room['outside'])

# _______ get player's name _______
curr_player.name = ''
while curr_player.name == '':
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Astrillia !")
    curr_player.name = input("What shall I call you m'Lord?   ",)
os.system('cls' if os.name == 'nt' else 'clear')
save_file = curr_player.name+".txt"

# _______  greet the player _____________
print("Greetings, Sir "+curr_player.name+"!\n")
print("You are "+curr_player.curr_room.name)
print(curr_player.curr_room.description)
curr_player.curr_room.inventory()
print("\nWhere would you like to go?..")
com_mand = input("choose: [n]North [s]South [e]East [w]West   [q]Quit\n>",)

# ___________ REPL loop __________________________
while not com_mand == "q":  # "q" quits the game.
    os.system('cls' if os.name == 'nt' else 'clear')
    if com_mand == "n":
        if curr_player.curr_room.n_to is None:
            print("You cannot go north m'lord...\n")
        else:
            print('you head north...\n')
            curr_player.curr_room = curr_player.curr_room.n_to
    elif com_mand == "s":
        if curr_player.curr_room.s_to is None:
            print("You cannot go south m'lord...\n")
        else:
            print('you head south...\n')
            curr_player.curr_room = curr_player.curr_room.s_to
    elif com_mand == "e":
        if curr_player.curr_room.e_to is None:
            print("You cannot go east m'lord...\n")
        else:
            print('you head east...\n')
            curr_player.curr_room = curr_player.curr_room.e_to
    elif com_mand == "w":
        if curr_player.curr_room.w_to is None:
            print("You cannot go west m'lord...\n")
        else:
            print('you head west...\n')
            curr_player.curr_room = curr_player.curr_room.w_to
    elif (com_mand == "i") or (com_mand == "I"):
        curr_player.list_inventory()
        print('')
    else:
        # not a single-letter command. parse for verb / noun
        parse_command(com_mand)

    # print updated location
    print("You are "+curr_player.curr_room.name)
    if (curr_player.curr_room.is_light) or (curr_player.has_light()) or (curr_player.curr_room.has_light()):
        print(curr_player.curr_room.description)
        curr_player.curr_room.inventory()
    else:
        print("It is pitch black!")
    print('')
    com_mand = input("choose: [n]North [s]South [e]East [w]West   [q]Quit\n>")

# ______________ game over ____________________
# save_results()
os.system('cls' if os.name == 'nt' else 'clear')
print('Goodbye, Sir '+curr_player.name+'! Safe travels & return soon!\n \n \n')
