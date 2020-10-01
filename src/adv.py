import textwrap

from player import Player
from room import Room
from item import Item


def wonderland():


# * INTRODUCTION

    title = ('\nWELCOME TO WONDERLAND!\n')
    
    royal_order = '   By order of the Queen, you are required to enter your name to enter this realm.\n'

    intro_1 = '   Out of the corner of your eye, you see a White Rabbit with a pocketwatch. You start following the White Rabbit and suddenly start falling down down down ...'

    intro_2 = '   You open your eyes and are surrounded in darkness. Slowly your eyes adjust and you see a faint light. You start walking in that direction.'
    
    intro_commands = 'To see all commands type: commands\nTo quit type: q (or quit)\n'

    print('\n' * 20)
    print(title)
    print(textwrap.fill(royal_order, width=65))
    next_victim = input('\n▸ ')
    print('\n')
    print(textwrap.fill(intro_1, width=65))
    print('\n')
    print(textwrap.fill(intro_2, width=65))
    print('\n')
    print(intro_commands)

# * ITEMS

    items = {
        'bottle': Item('bottle', 'a bottle that says DRINK ME'),
        'cake': Item('cake', 'a very small cake that says EAT ME'),
        'key':  Item('key', 'a tiny golden key'),
        'torch': Item('torch', 'in the deepest shadow there is a flicker of light'),
        'coin': Item('coin', 'a golden coin'),
        'pocketwatch': Item('pocketwatch', 'a beautiful golden watch on a chain'),
        'chest': Item('chest', 'an empty chest')
    }

# * ROOMS

    room = {
        'outside':  Room("Outside Cave Entrance",
                        "North of you, the cave mount beckons.", 
                        [items['torch']]),

        'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north \nand east.""", [items['bottle'], items['cake'], items['key']]),

        'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness.\nAhead to the north, a light flickers in the distance, but \nthere is no way across the chasm.""", [items['coin']]),

        'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of \ngold permeates the air.""", [items['pocketwatch']]),

        'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has \nalready been completely emptied by earlier adventurers. \nThe only exit is to the south.""", [items['chest']]),
    }

    # Link rooms together
        # getattr
        # hasattr
    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside'] 
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']

# * PLAYERS

    # Make a new player object that is currently in the 'outside' room.

    player = Player(next_victim or 'Alice', room['outside'], [])
    print(player)
    

    rm_key = [k for k, v in room.items() if v == player.curr_room][0]
    rm_desc = room[rm_key]
    rm_inv_list = Room.get_inventory(room[rm_key])


    #  Write a loop that:
    #  Prints the current room name
    #  Prints the current description (the textwrap module might be useful here)
    #  Waits for user input and decides what to do.

    # outside = '{}'.format(player.get_room())
    # print(textwrap.fill(outside, width=50))

    options = '\nChase after the White Rabbit:\n[n] North   [e] East   [s] South   [w] West   [o] Outside   [q] quit\n\nPrepare for the adventure:\ntake <item> || drop <item> || inspect <item> || check inv || <commands>\n'

    all_verbs = ['take', 'drop', 'inspect', 'check']

    next_move = input('\n▸').lower()

    if next_move[0] in list('newsoq'):
        nsew = next_move

    elif next_move[0:4] == 'comm':
        print(options)

    curr_verb = next_move.split()[0]
    curr_obj = next_move.split()[1]

    # print('ITEMS IN ROOM', [i for i in rm_inv_list])


    all_item_keys = list(items.keys())[:]
    if curr_obj not in all_item_keys:
        print('Which item?', list(items.keys()))
    elif curr_verb == 'take':
        # print(player.take_item(curr_obj))
        # print(room[rm_key], curr_obj)
        # print(Room.item_taken(room[rm_key], curr_obj))
        player.take_item(curr_obj)
        Room.item_taken(room[rm_key], rm_inv_list[0])
        print('Current inventory:', player.get_inv())
        # print(Room.get_inventory(room[rm_key]))

# 
# Which direction would you like to go?
# [n] North   [e] East   [s] South   [w] West   [o] other   [q] Quit
# other = input()
# * If the user enters a cardinal direction, attempt to move to the room there.
# * Print an error message if the movement isn't allowed.
# * If the user enters "q", quit the game.

    def try_direction(direction, curr_room):
        attribute = direction + '_to'
        if hasattr(curr_room, attribute):
            return getattr(curr_room, attribute)
        else:
            print('Oouch!')
            return curr_room

    room_keys = list(room.keys())[:]
    room_values = list(room.values())[:]

    while next_move[0] != 'q':
        
        if next_move[0] == 'o':
            player.set_room(room[player.return_outside()])
            
        elif next_move[0] in list('news'):

            new_room = try_direction(nsew, player.curr_room)
            for i, e in enumerate(room_values):
                if e == new_room:
                    player.set_room(room[room_keys[i]])
                    # print(player.get_room())
        else:
            print(player.get_room())
            next_move = input('\n▸').lower()
            if next_move[0] in list('newsoq'):
                nsew = next_move
        print(player.get_room())
        print(' ')
        # print(room[player.get_room()])
        # print(x.get_inventory())

        next_move = input('\n▸').lower()
        if next_move[0] in list('newsoq'):
            nsew = next_move

        if next_move[0:4] == 'comm':
            print(options)

        curr_verb = next_move.split()[0]
        curr_obj = next_move.split()[1]

    # print('ITEMS IN ROOM', [i for i in rm_inv_list])


        all_item_keys = list(items.keys())[:]
        if curr_obj not in all_item_keys:
            print('Which item?', list(items.keys()))
        elif curr_verb == 'take':
        # print(player.take_item(curr_obj))
        # print(room[rm_key], curr_obj)
        # print(Room.item_taken(room[rm_key], curr_obj))
            player.take_item(curr_obj)
            Room.item_taken(room[rm_key], rm_inv_list[0])
        # print(player.get_inv())
        # print(Room.get_inventory(room[rm_key]))


if __name__ == '__main__':
  wonderland()


            # for i in 

            # if nsew == 'n':
            #     print(player.get_room())
            #     print(player.curr_room)
            #     # print(room[player.get_room].get('outside'))
            #     print(list(room.keys()))
            #     print(i for i in list(room.values()) if i == player.get_room())

            #     try:
            #         room[player.get_room()].n_to
            #     except:
            #         print('Choose another direction')
            #         nsew = input(which_way).lower()[0]
            #     else:
            #         x = [k for k in room[player.get_room()].n_to]
            #         print('X', x)

            # elif nsew == 'e':
            #     try:
            #         room[player.get_room()].e_to
            #     except:
            #         print('Choose another direction')
            #         nsew = input(which_way).lower()[0]
            #     else:
            #         x = [k for k, v in room.items() if v == room[player.get_room()].e_to]

            # elif nsew == 'w':
            #     try:
            #         room[player.get_room()].w_to
            #     except:
            #         print('Choose another direction')
            #         nsew = input(which_way).lower()[0]
            #     else:
            #         x = [k for k, v in room.items() if v == room[player.get_room()].w_to]
            # elif nsew == 's':
            #     try:
            #         room[player.get_room()].s_to
            #     except:
            #         print('Choose another direction')
            #         nsew = input(which_way).lower()[0]
            #     else:
            #         x = [k for k, v in room.items() if v == room[player.get_room()].s_to]