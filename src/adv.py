from room import *
from player import *
from items import *
from os import system, name

# Declare items

items = {
    'lint': Basic('Some Lint', 'Just some old lint', 0, False),
    'secret': Basic('Torn Page', '''A torn piece of paper. \
Across it you can read: "take me to the secret room!"''', 0, True),
    'secret2': Basic('Torn Paper', '''A torn piece of paper. \
Across it you can read: "take me back!"''', 0, True),
    'backpack': Basic('Back-Pack', 'To hold your treasures', 6, True),
    'dagger': Weapon('Stabby', 'A short dagger.', 5, 10),
    'sword': Weapon('Slash', 'A large sword.', 12, 17),
    'needle': Weapon('Pokey', '''A long, NEEDLE-like sword. \
(stick them with the pointy end)''', 25, 25),
    'rock': Basic('Pet Rock', 'Just a rock...', 1, False),
    'shoes': Basic('Shoes', '''Pair of Jordans.
What are those doing here?''', 20, True),
    'book': Book('Book', '''An old book. \
Most of the pages are faded''', 3, 'Unknown'),
    'great_book': Book('Cryptonomicon', '''A fantastic book, \
seriously read it!''', 20, 'Neal Stephenson')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", '''North of you, \
the cave mount beckons''',
                    [items['rock'].name]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. \
Dusty passages run north and east.""",
                     [items['dagger'].name, items['book'].name]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, \
falling into the darkness. Ahead to the north, 
a light flickers in the distance, but there is no
way across the chasm.""",
                     [items['rock'].name, items['dagger'].name,
                     items['secret'].name]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends \
here from west to north. The smell of gold \
permeates the air.""",
                     [items['rock'].name]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost \
treasure chamber! Sadly, it has already been \
completely emptied by earlier adventurers. \
The only exit is to the south.""",
                     [items['sword'].name, items['shoes'].name]),

    'easteregg': Room('Secret Cache', '''HOW DID YOU FIND THIS ROOM! 
You basically beat the game, well done!''',
                       [items['needle'].name, items['great_book'].name,
                       items['secret2'].name])
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

# Function to clear old output


def clear():
    _ = system('cls' if name == 'nt' else 'clear')

# Main


def adventure_ish():
    clear()
    print(f'''\nWelcome to Adventure-Ish Game! The goal is to get to the treasure room...\n
{'*' * 31} Or is it? {'*' * 31}''')

    player = Player(input(f'''\nWhat do they call you?\n{'-'*22} \n'''), room['outside'], [
                    items['lint'].name, items['backpack'].name])
    player.welcome_player()

    cmd = ''

    while cmd != 'q':
        # Dict for movement
        room_movement = {
            'n': player.current_room.n_to,
            's': player.current_room.s_to,
            'e': player.current_room.e_to,
            'w': player.current_room.w_to
        }

        # Dict for actions
        player_actions = {
            'i': player.check_inv,
            'r': player.current_room.room_describe,
            'c': player.self_describe,
        }

        # Dict for all commands, except hidden commands
        key_commands = {
            'n': 'Move North',
            's': 'Move South',
            'e': 'Move East',
            'w': 'Move West',
            'i': 'Check Inventory',
            'r': 'Describe Room',
            'c': 'Describe Character',
            'p': 'Pickup Item (p stabby)',
            'd': 'Drop Item (d some lint)',
            'x': 'Examine item (x stabby)'
        }

        for i in key_commands:
            print(f'[{i}]: {key_commands[i]}')
        cmd = input('\nWhat would you like to do?\n')

        if cmd == '':
            clear()
            lengther = len('you must enter something!')
            print('*'*lengther)
            print('*'*lengther)
            print('You must enter something!')
            print('*'*lengther)
            print('*'*lengther)
        elif cmd.split()[0] in room_movement.keys():
            clear()
            if room_movement[cmd.split()[0]]:
                player.move(room_movement[cmd.split()[0]])
                player.current_room.room_describe()
            else:
                print('-'*28)
                print(f"You can't go that direction!")
                print('-'*28)
        elif cmd.split()[0] in player_actions.keys():
            clear()
            player_actions[cmd.split()[0]]()
        elif cmd.split()[0] == 'p':
            clear()
            if ' '.join(cmd.lower().split()[1:]) in [i.lower() for i in player.current_room.item_names]:
                player.pickup(' '.join(cmd.split()[1:]))
            else:
                print('-'*25)
                print('That item is not present!')
                print('-'*25)
        elif cmd.split()[0] == 'd':
            clear()
            if ' '.join(cmd.lower().split()[1:]) in [i.lower() for i in player.inventory]:
                player.drop_item(' '.join(cmd.split()[1:]))
            else:
                print('-'*30)
                print(f"You aren't carrying that item!")
                print('-'*30)
        elif cmd.split()[0] == 'x':
            clear()
            if ' '.join(cmd.lower().split()[1:]) in [i.lower() for i in player.inventory]:
                player.inspect_item(' '.join(cmd.split()[1:]))
            else:
                print('-'*28)
                print('That item is not in your inventory!')
                print('-'*28)
        elif cmd == 'take me to the secret room!':
            clear()
            player.current_room = room['easteregg']
            player.current_room.room_describe()
        elif cmd == 'take me back!':
            clear()
            player.current_room = room['overlook']
            player.current_room.room_describe()
        elif cmd != 'q':
            clear()
            print('-'*28)
            print('That is not a valid command!')
            print('-'*28)
    clear()
    print('Goodbye!')


if __name__ == '__main__':
    adventure_ish()