from room import Room
from player import Player
from item import Item
from item import Herb
import sys
import os
import cmd
import textwrap
import time
import random

#### Map ####
"""
____________________________________________________________
                                      ===================
                                      |     TREASURE    |
                                      |                 |
                                      |     [_-__-_]    |
                                      |                 |
                                      |======   =======|
            +_+_+_+_+_+_+_+_+_+_+           {   }
            |                   |           |  |
            |     OVERLOOK      |           |  |
            |                   |           |  |
            |_______   _________|      ____{   }___
                 __|  |____          /             \
                |         |_________|   NARROW     |
                |  FOYER   _________               |
                |___   ___|        |______________/
                  |    |
__________________|    |_____________________________________

                OUTSIDE                     

"""
# zonemap = {
#     'foyer': {
#             ZONENAME: '',
#             DESCRIPTION: 'description',
#             EXAMINATION: 'examine',
#             SOLVED: False,
#             UP: 'up', 'north',
#             DOWN: 'down', 'south',
#             LEFT: 'left', 'west',
#             RIGHT: 'right', 'east'
#     }
# }
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     "You see the sun set, and this beauty is bitter sweet. Unscramble this word ==> `lusunec`",
                     "False",
                     'foyer',
                     "False",
                     "False",
                     "False",
                     [Item("Red Stone", "Illuminates a red hue when held to light."), 
                     Item("Demon Skull", "It makes a faint humming sound."),
                     Herb("Healing Leaf", "A minty tasting leaf", 25, "Herb")
                     ]
                     ),

    'foyer':    Room("Foyer",
                     """Dim light filters in from the south. Dusty
                     passages run north and east.""",
                     'You hear the cries of tortured people.\nThey eagerly would like to know what `avogadros number` is. (4 sig figs)',
                     "False",
                     'overlook',
                     'outside',
                     "False",
                     'narrow',
                     []
                     ),

    'overlook': Room("Grand Overlook",
     """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                      "The door has locked behind you.\nAnother tortured scientist appears and asks:\nWhat is π/2 radians in degrees?",
                      "False",
                      "False",
                      'foyer',
                      "False",
                      "False",
                      []
),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     "Ancient writing teaches you the code combination `1337`",
                     "False",
                     'treasure',
                     "False",
                     'foyer',
                     "False",
                     []
),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber. Leroy Jenkins stands before you,\nand he looks hungry and ready to rap.\nIf you answer his riddle, he will give you his WoW account information.""",
                     "Your palms are sweaty, knees weak, mom's spaghetti. The cake is a lie,\nbecause Leroy Jenkins ate it with what kind of food?",
                     "True",
                     "False",
                     'narrow',
                     "False",
                     "False",
                     []
),
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

starting_knight = [
    Item("Steel Sword", "Something To Slice With."), 
    Item("Lions Mane", "Increases Health Slightly")
]

starting_magi = [
    Item("Magic Spell Book", "Provides Knowledge Of Ancient Spells"), 
    Item("Lions Mane", "Increases Health Slightly")
]

starting_assassin = [
    Item("Steel Dagger", "Something To Stab With."), 
    Item("Lions Mane", "Increases Health Slightly")
]


#
# Main
#
def main():
    print(os.getenv)
    os.system('clear')
    print("#########################################\n")
    print("# Welcome To Troy's Text Adventure Game #\n")
    print("#########################################\n")
    print("#                1.) Start              #  ")
    print("#                2.) Load               #  ")
    print("#                3.) Help               #  ")
    print("#                4.) Exit               #  ")
    print("#########################################\n")
    option = input("-> ")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        help_menu()
    elif option == "4":
        sys.exit()

    else:
        print("Requires 1, 2, or 3 inputs")
        main()

def help_menu():
    
    print("#########################################\n")
    print("# Welcome To Troy's Text Adventure Game #\n")
    print("#########################################\n")
    print("# type 1, 2, 3, 4 for menu navigation\n         ")
    print("# - Use `up`, `down`, `left`, `right` to move\n ")
    print("# - Type The Following Commands For Actions:\n['quit', 'q']\n['move', 'go', 'travel', 'walk']\n['examine', 'inspect', 'interact', 'look']\n['inventory', 'items']\n[drop, get]\n[search, heal]  ")
    print("# - Use 'examine' to examine something\n        ")
    print("# - Good Luck Adventurer.                     ")
    print("#########################################\n")
    main()


def class_define(player_name):
    print("Which Class Would You Like To Be {}: ".format(player_name))
    print("1.) Knight")
    print("2.) Magi")
    print("3.) Assassin")
    

    player_class = input('Class: \n').upper()
    if player_class == "1" or player_class == "KNIGHT":
        global starting_knight
        default_inventory = starting_knight
        class_name = "Knight"
    elif player_class == "2" or player_class == "MAGI":
        global starting_magi
        default_inventory = starting_magi
        class_name = "Magi"
    elif player_class == "3" or player_class == "ASSASSIN":
        global starting_assassin
        default_inventory = starting_assassin
        class_name = "Assassin"
    else:
        print("Requires 1, 2, or 3 inputs or specify as `knight`, `magi`, or `assassin`\n")
        class_define(player_name)
    
    default_location = room['outside']
    
    global PlayerIG
    PlayerIG = Player(player_name, default_location, default_inventory)
    start1(class_name)

def start():
    os.system('clear')
    print("Hello, what is your name?")
    global room
    # print(room['outside'])
    options = input('-->')

    class_define(options)


### Game Interactivity ###
def print_location():
    print('\n' + ('#' * (4 + len(PlayerIG.current_room.name))))
    print('# ' + PlayerIG.current_room.name.upper() + ' #')
    print('# ' + PlayerIG.current_room.description + ' #')
    print('' + ('#' * (4 + len(PlayerIG.current_room.name))))


#### Game Functionality ####


def player_move(myAction):
    ask = "What direction would you like to {} to?\n".format(myAction)
    print('    ____________________________________________________________')
    print('                                      ===================       ')
    print('                                      |     TREASURE    |       ')
    print('                                      |                 |       ')
    print('                                      |     [_-__-_]    |       ')
    print('                                      |                 |       ')
    print('                                      |======   =======|        ')
    print('            +_+_+_+_+_+_+_+_+_+_+           {   }               ')
    print('            |                   |           |  |                ')
    print('            |     OVERLOOK      |           |  |                ')
    print('            |                   |           |  |                ')
    print('            |_______   _________|      ____{   }___             ')
    print('                 __|  |____          /             |            ')
    print('                |         |_________|   NARROW     |            ')
    print('                |  FOYER   _________               |            ')
    print('                |___   ___|        |______________/             ')
    print('                  |    |                                        ')
    print('__________________|    |_____________________________________   ')
    print('                                                                ')
    print('                OUTSIDE                                         ')

    dest = input(ask)
    if dest in ['up', 'north']:
        destination = room[PlayerIG.current_room.up]
        print(destination)
        movement_handler(destination)
    elif dest in ['down', 'south', 'd', 's']:
        destination = room[PlayerIG.current_room.down]
        movement_handler(destination)
    elif dest in ['left', 'west', 'l', 'w']:
        destination = room[PlayerIG.current_room.left]
        movement_handler(destination)
    elif dest in ['right', 'east', 'r', 'e']:
        destination = room[PlayerIG.current_room.right]
        movement_handler(destination)

def movement_handler(destination):
    print("\n" + "You are in the " + destination.name)
    try:
        PlayerIG.current_room = destination
        print_location()
        print("\n" + "======================================")
        print("What would you like to do?")
        action = input("--->" + "\n")
        acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'q', 'examine', 'inspect', 'interact', 'look', 'inventory', 'items', 'drop', 'get', 'search', 'heal']
        while action.lower() not in acceptable_actions:
            print("Unknown Action, Try Again.\n try 'move', 'go', 'travel', 'walk'")
            action = input("-->")
        if action.lower() in ['quit', 'q']:
            sys.exit()
            
        elif action.lower() in ['move', 'go', 'travel', 'walk']:
            if PlayerIG.current_room.solved == "False":
                print("\n### Please `examine` Your Surroundings ###")
                movement_handler(destination)
            else:
                player_move(action.lower())
        elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
            player_examine(action.lower())
        elif action.lower() in ['inventory', 'items']:
            player_items(action.lower())
        elif action.lower() in ['drop']:
            player_drop()
        elif action.lower() in ['get']:
            player_get()
        elif action.lower() in ['search']:
            player_search()
        elif action.lower() in ['heal']:
            Herb.recover(PlayerIG)
            movement_handler(destination)

    except: 
        if action.lower() in ['move', 'go', 'travel', 'walk']:
            print("You Can't Go That Way, follow the clues.")
            player_move(myAction='move')
        else:
            sys.exit()
            

def start1(x):
    os.system('clear')
    # print_location()
    print("Hello {} {},\nyou have been chosen to infiltrate and retrieve \nan `item` of great power.".format(x ,PlayerIG.name))
    print("\n" + "======================================")
    destination = PlayerIG.current_room
    movement_handler(destination)
    # print("What would you like to do?")
    # action = input("--->")
    # acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look']
    # while action.lower() not in acceptable_actions:
    #     print("Unknown Action, Try Again.\n")
    #     action = input("-->")
    # if action.lower() == 'quit':
    #     sys.exit()
    # elif action.lower() in ['move', 'go', 'travel', 'walk']:
    #     player_move(action.lower())
    # elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
    #     player_examine(action.lower())

def player_search():
    destination = PlayerIG.current_room
    print("You search the room.")
    print("These items are spotted: ")
    print(PlayerIG.current_room.items)
    movement_handler(destination)

def player_get():
    destination = PlayerIG.current_room
    print("You search the room.")
    print("These items are spotted: ")
    print(PlayerIG.current_room.items)
    item = input('input item you would like to pick up -->')
    room_items = PlayerIG.current_room.items
    print(room_items[0].name)
    print([i.name for i in room_items])
    if any([i.name == item for i in room_items]):
        match = next((l for l in room_items if l.name == item), None)
        # print(match)
        PlayerIG.inventory.append(match)
        print(PlayerIG.inventory)
        # PlayerIG.currentRoom.items.remove(match)
        movement_handler(destination)
    else:
        print(f"There is no item with the name of {item}")
        movement_handler(destination)

def player_drop():
    destination = PlayerIG.current_room
    item = input('input item you would like to drop -->')
    items = PlayerIG.inventory
    if any([i.name == item for i in items]):
        match = next((l for l in items if l.name == item), None)
        print(match)
        PlayerIG.inventory.remove(match)
        PlayerIG.current_room.items.append(match)
        print("Your Inventory: ", PlayerIG.inventory)
        print("Items In Room: ", PlayerIG.current_room.items)
        movement_handler(destination)
    else: 
        print(f"There is no item with the name of {item} in your inventory")
        movement_handler(destination)

def player_items(item):
    destination = PlayerIG.current_room
    print("These are your items...\n")
    print(PlayerIG.inventory)
    movement_handler(destination)

def player_examine(action):
    destination = PlayerIG.current_room
    print(PlayerIG.current_room.name)

### Outside Cave Entrance EXAMINE PUZZLE ###

    if PlayerIG.current_room.name == 'Outside Cave Entrance':
        if PlayerIG.current_room.solved == True:
            print("You have already exhausted this zone")
            movement_handler(destination)
        else:
            print('# ' + PlayerIG.current_room.examination + ' #')
            word = input('->')
            if word == 'nucleus':
                PlayerIG.current_room.solved = True
                print(PlayerIG.current_room.solved)
                print("\nGreat Job, the word is `nucleus`, You May Move North.")

                movement_handler(destination)
            else:
                print("Wrong, Try Again")
                print(action)
                player_examine(action)

### Foyer EXAMINE PUZZLE ###

    if PlayerIG.current_room.name == 'Foyer':
        if PlayerIG.current_room.solved == True:
            print("You have already exhausted this zone")
            movement_handler(destination)
        else:
            print('# ' + PlayerIG.current_room.examination + ' #')
            word = input('->')
            if word == '6.022*10**23' or word == '6.022x10^23':
                PlayerIG.current_room.solved = True
                print(PlayerIG.current_room.solved)
                print("\nGreat Job, the tortured scientists rejoice, and laugh at you.\nThey unlock various passageways.")

                movement_handler(destination)
            else:
                print("Wrong, Try Again")
                print(action)
                player_examine(action)

### Grand Overlook EXAMINE PUZZLE ###

    if PlayerIG.current_room.name == 'Grand Overlook':
        if PlayerIG.current_room.solved == True:
            print("You have already exhausted this zone")
            movement_handler(destination)
        else:
            print('# ' + PlayerIG.current_room.examination + ' #')
            word = input('->')
            if word == '90' or word == '90 degrees':
                PlayerIG.current_room.solved = True
                print(PlayerIG.current_room.solved)
                print("\nGreat Job, the scientist realizes the meaning of his bald circular 2πr shaped head.\nThe door has now unlocked behind you.")

                movement_handler(destination)
            else:
                print("Wrong, Try Again")
                print(action)
                player_examine(action)

### Narrow Passage EXAMINE PUZZLE ###

    if PlayerIG.current_room.name == 'Narrow Passage':
        if PlayerIG.current_room.solved == True:
            print("You have already exhausted this zone")
            movement_handler(destination)
        else:
            print('# ' + PlayerIG.current_room.examination + ' #')
            word = input('->')
            if word == '1337':
                PlayerIG.current_room.solved = True
                print(PlayerIG.current_room.solved)
                print("\nGreat Job, but you aren't elite just yet, the next puzzle awaits.")

                movement_handler(destination)
            else:
                print("Wrong, Try Again")
                print(action)
                player_examine(action)

### Treasure Chamber EXAMINE PUZZLE ###

    if PlayerIG.current_room.name == 'Treasure Chamber' and room['outside'].solved == True and room['foyer'].solved == True and room['overlook'].solved == True and room['narrow'].solved == True:
        if PlayerIG.current_room.solved == False:
            print("You have already exhausted this zone, you won now go home.")
        elif room['outside'].solved == True and room['foyer'].solved == True and room['overlook'].solved == True and room['narrow'].solved == True:
            print('# ' + PlayerIG.current_room.examination + ' #')
            word = input('->')
            if word == 'chicken':
                PlayerIG.current_room.solved = False
                # print(PlayerIG.current_room.solved)
                print("\nYou Have Won The Game, gratz.\nYou proceed to play World of Warcraft with Leroy for 2 months straight.\n At Least You Had Chicken.")

                
            else:
                print("Wrong, Try Again")
                print(action)
                player_examine(action)
    else:
        print("\n### More Rooms Need Examining/Solving.. Chum ###")
        movement_handler(destination)



ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'outside': False, 
                 'foyer': False, 
                 'overlook': False, 
                 'narrow': False, 
                 'treasure': False
}


main()
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
