import random
from room import Room
from item import Item
from player import Player
from adv_save import load_results, save_results
import os


def parse_command(com_mand):
    # To Do:code to parse/execute noun+verb commands

    # print("\nInvalid selection. Please try again.\n")
    
    print(com_mand)
    return

# Declare list of items
it_em = {
    'flask': Item('flask', 'a flask'),
    'torch': Item('torch', 'a torch'),
    'matches': Item('matches', 'some matches'),
    'sword': Item('sword', 'an old sword'),
    'rum': Item('rum', 'a bottle of rum'),
    'bones': Item('bones', 'a pile of bones'),
    'skull': Item('skull', 'a skull')
}

# Declare all the rooms
room = {
    'outside':  Room("outside the Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("in the Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("at the Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("in a narrow passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("in the Treasure Chamber!", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by earlier adventurers.
The only exit is to the south.""")
}

# Link rooms together
room['outside'].add_item(it_em['matches'])
room['foyer'].add_item(it_em['flask'])
room['overlook'].add_item(it_em['torch'])
room['treasure'].add_item(it_em['sword'])
room['narrow'].add_item(it_em['bones'])
room['narrow'].add_item(it_em['skull'])

# Place items in rooms
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# _________ init  _______________
# Make a new player object that is currently in the 'outside' room.
curr_player = Player("Player1", room['outside'])

# _______ welcome message _______
curr_player.name = ''
while curr_player.name == '':
    #os.system('cls' if os.name == 'nt' else 'clear')
    print("Welcome to Astrillia !")
    curr_player.name = input("What shall I call you m'Lord?   ",)
os.system('cls' if os.name == 'nt' else 'clear')
save_file = curr_player.name+".txt"

print("\nGreetings, Sir "+curr_player.name+"!\n")
print("You are currently "+curr_player.curr_room.name, "\n")
print(curr_player.curr_room.description, "\n")
curr_player.curr_room.inventory()
print("Where would you like to go?..")
com_mand = input("choose: [n]North [s]South [e]East [w]West   [q]Quit\n",)

# gamplay loop: Waits for user input and decides what to do.
while not com_mand == "q":  # If the user enters "q", quit the game.
    os.system('cls' if os.name == 'nt' else 'clear')
    if com_mand == "n":
        print('you head north...')
        try:
            curr_player.curr_room = curr_player.curr_room.n_to
        except:
            print("\nYou cannot go that way m'lord...\n")
    elif com_mand == "s":
        print('you head south...')
        try:
            curr_player.curr_room = curr_player.curr_room.s_to
        except:
            print("\nYou cannot go that way m'lord...\n")
    elif com_mand == "e":
        print('you head east...')
        try:
            curr_player.curr_room = curr_player.curr_room.e_to
        except:
            print("\nYou cannot go that way m'lord...\n")
    elif com_mand == "w":
        print('you head west...')
        try:
            curr_player.curr_room = curr_player.curr_room.w_to
        except:
            print("\nYou cannot go that way m'lord...\n")
    else:
        # not a directional move. parse for verb / noun
        parse_command(com_mand)

    # print updated location
    print("\nYou are currently "+curr_player.curr_room.name, "\n")
    print(curr_player.curr_room.description, "\n")
    # curr_player.curr_room.inventory()
    com_mand = input("choose: [n]North [s]South [e]East [w]West   [q]Quit\n")

# ________ game over _________
# save_results()
os.system('cls' if os.name == 'nt' else 'clear')
room['narrow'].inventory()
print('Goodbye, Sir '+curr_player.name+'! Safe travels & return soon!\n \n \n')
