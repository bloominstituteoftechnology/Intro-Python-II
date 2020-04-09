from room import Room
from player import Player
from item import Item
from book import Book
from treasure import Treasure
from colors import print_color
import time


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. You see a door to the west."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Look around to see what's inside."""),

    # add another room
    'library': Room("Library", """The room appears a mess. As though someone left 
    in a hurry. Are they trying to hide something?""", False)
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
# link the new room
room['foyer'].w_to = room['library']
room['library'].e_to = room['foyer']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Items

# Library - Room west to the Foyer (initially locked)
# key - Item found in Foyer - will unlock the library
# library will house 3 books
# Book - inherits from Item
# "read" i.e. collect all three books to access pieces of a password
# complete password will unlock "Treasure"

items = {
    'key': Item("key", "A heavy, bronze key."),
    'book1': Book("book1", "A dusty, old book. Try reading it.", "a8qr"),
    'book2': Book("book2", "A thick, leather book. Try reading it.", "f02g"),
    'book3': Book("book3", "A thin, fragile book. Try reading it.", "2h5n"),
    'treasure': Treasure("treasure", "One-thousand gold bars and a lifetime supply of burritos!")
}

# add the items to the rooms
room['foyer'].items = [items['key']]
room['library'].items = [items['book1'], items['book2'], items['book3']]
room['treasure'].items = [items['treasure']]


player_name = input('\nWhat is your name? ')

player = Player(player_name, room['outside'])

print_color('cyan', f'\nWelcome {player.name}!\n\n')

# time.sleep(1)


def location_print(color):
    print_color(
        color, f'\033[1m\n\nYour location: {player.current_room.name}\33[00m')
    # time.sleep(1)
    print_color(color, f'{player.current_room.description} \n')
    # time.sleep(1)


# loop that prints the current room name and description
while True:
    if player.current_room == room['outside']:
        location_print('green')
    elif player.current_room == room['foyer']:
        location_print('purple')
    elif player.current_room == room['library']:
        # make if and else statements based on whether the player has the key in inventory
        if len(player.inventory) > 0 and items['key'] in player.inventory:
            if room['library'].unlocked == False:
                print_color('green', "\n\nYou've unlocked the Library!")
            room['library'].unlocked = True
            location_print('yellow')
        else:
            print_color('red', f'\n\nThis room is locked')
            player.current_room = room['foyer']
            location_print('purple')
    elif player.current_room == room['overlook']:
        location_print('light_purple')
    elif player.current_room == room['narrow']:
        location_print('light_grey')
    elif player.current_room == room['treasure']:
        location_print('yellow')

    # prompt for possible commands
    player_move = input(
        """Move commands: (n, s, e, w)
    Check your inventory: 'i'
    Look around the room: 'l'
    Get item: 'get <item name>'
    Press 'q' to quit.\n\n""").lower()

    # moving rooms with directional inputs
    if player_move in ['n', 's', 'e', 'w']:
        player.move(player_move)
    # printing player inventory
    elif player_move == 'i':
        if len(player.inventory) > 0:
            print_color('yellow', '\n\nInventory:')
            for item in player.inventory:
                print_color('yellow', f'{item.name}')
            print_instructions = input("\nView item descriptions? (y/n): ")
            if print_instructions == 'y':
                for item in player.inventory:
                    print_color('yellow', f'\n{item.name}: {item.description}')
            elif print_instructions == 'n':
                pass
            else:
                print_color('red', '\n\nInvalid input')
        else:
            print_color('red', '\n\nNo items in your inventory')
    # printing list of items in the room
    elif player_move == 'l':
        # if there are items, loop over them and print them out
        if len(player.current_room.items) > 0:
            print_color('green', '\n\nThis room contains:')
            for item in player.current_room.items:
                print_color('yellow', f'\n{item.name}: {item.description}')
        # if there are no items in the room
        else:
            print_color('red', '\n\nThis room has nothing in it.')
    # getting specified item from room into player inventory
    elif player_move.startswith('get'):
        query = player_move.split()
        item = query[1].lower()
        # if the specified item is in the room, put in player inventory
        if len(player.current_room.items) > 0 and player.current_room.has_item(item) and item != 'treasure':
            player.grab_item(items[item])
            player.current_room.remove_item(items[item])
        elif item == 'treasure' and items[item].is_locked == True:
            if len(player.knowledge) > 0:
                knowledge = []
                for i in player.knowledge:
                    knowledge.append(i)
                if len(knowledge) == 1:
                    print_color(
                        'yellow', f'You only have one piece of the password: {knowledge[0]}')
                elif len(knowledge) == 2:
                    print_color(
                        'yellow', f'You only have two pieces of the password: {knowledge[0]}-{knowledge[1]}')
                elif len(knowledge) == 3:
                    print_color(
                        'green', f'You have all three pieces of the password: {knowledge[0]}-{knowledge[1]}-{knowledge[2]}')
            password_input = input(
                "The treasure is locked! What's the password? ")
            password = password_input.split('-')
            if 'a8qr' in password and 'f02g' in password and '2h5n' in password:
                print_color('green', "\n\nYou unlocked the treasure!!! :D")
                player.grab_item(items[item])
                player.current_room.remove_item(items[item])
            else:
                print_color('red', "\n\nIncorrect password :(")
        # if the specified item is not in the room, print this
        else:
            print_color(
                'red', f'\n\nThis room does not contain item {query[1]}')
    # reading a book
    elif player_move.startswith('read'):
        query = player_move.split()
        book = items[query[1].lower()]
        player.read_book(book)
    # quit the game
    elif player_move == 'q':
        exit()
    else:
        print_color('red', '\n\n\nInvalid input. Please try again.\n\n')
