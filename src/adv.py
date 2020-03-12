from room import *
from player import *
from items import *

# Declare items

lint = Basic('Some Lint', 'Just some old lint', 0, False)
dagger = Weapon('Stabby - ', 'A short dagger. ', 5, 2)
sword = Weapon('Slash - ', 'A large sword. ', 12, 4)
needle = Weapon(
    'Pokey - ', 'A long, NEEDLE-like sword. (stick them with the pointy end) ', 25, 9)
rock = Basic('Pet Rock - ', 'Just a rock... ', 1, False)
shoes = Basic(
    'Shoes - ', 'Pair of Jordans. What are those doing here? ', 20, True)
book = Book('Book - ', 'An old book. Most of the pages are faded ', 3, 'Unknown')
great_book = Book('Cryptonomicon - ',
                  'A fantastic book, seriously read it! ', 20, 'Neal Stephenson')

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [rock.name, rock.description]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [dagger.name, dagger.description, book.name, book.description]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [rock.name, rock.description, dagger.name, dagger.description]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [rock.name, rock.description]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [sword.name, sword.description, shoes.name, shoes.description]),

    'easteregg': Room('Secret Cache', '''HOW DID YOU FIND THIS ROOM! You basically
beat the game, well done!''', [needle.name, needle.description, great_book.name, great_book.description])
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


# Make a new player object that is currently in the 'outside' room.

# Write a loop that:

def adventure_ish():
    print(f'''\nWelcome to Adventure-Ish Game! The goal is to get to the treasure room...\n
{'*' * 30} Or is it? {'*' * 30}''')

    name = input(f'''\nWhat do they call you?\n{'-'*20} \n''')
    rp = input(f'''\nAnd what are you famous for {name}?\n''')
    player = Player(name, rp, room['outside'], inventory=[lint.name])
    player.welcome_player()

    cmd = ''

    while cmd != 'q':
        key_commands = {
            'n': 'Move North',
            's': 'Move South',
            'e': 'Move East',
            'w': 'Move West',
            'i': 'Check Inventory',
            'r': 'Describe Room',
            'c': 'Describe Character'
        }

        for i in key_commands:
            print(f'[{i}]: {key_commands[i]}')
        cmd = input('\nWhat would you like to do?\n')
#         cmd = input(f'''What do you want to do?
# {'-' * 125}
# [n]: Move North [s]: Move South [e]: Move East [w]: Move West [i]: Check Inventory [r]: Describe Room [c]: Describe Character
# {'-' * 125}
#         ''')
        # Dict for movement
        room_movement = {
            'n': player.current_room.n_to,
            's': player.current_room.s_to,
            'e': player.current_room.e_to,
            'w': player.current_room.w_to
        }

        # Dict for actions
        player_actions = {
            'i': player.check_inv(),
            'r': player.current_room.room_describe(),
            'c': player.self_describe()
        }

        if cmd in room_movement:
            player.move(room_movement[cmd])
            player.current_room.room_describe()
        # else:
        #     player_actions[cmd]
        # if cmd[0][0].lower() == 'n':
        #     if player.current_room.n_to:
        #         player.current_room = player.current_room.n_to
        #         player.looper_info()
        # elif cmd.lower() == 'take me to the secret underground layer!':
        #     player.current_room = room['easteregg']
        #     player.looper_info()
        # elif cmd.lower() == 'take me back':
        #     player.current_room = room['outside']
        #     player.looper_info()
        # elif cmd[0][0].lower() == 's':
        #     if player.current_room.s_to:
        #         player.current_room = player.current_room.s_to
        #         player.looper_info()
        # elif cmd[0][0].lower() == 'e':
        #     if player.current_room.e_to:
        #         player.current_room = player.current_room.e_to
        #         player.looper_info()
        # elif cmd[0][0].lower() == 'w':
        #     if player.current_room.w_to:
        #         player.current_room = player.current_room.w_to
        #         player.looper_info()
        # elif cmd[0][0].lower() == 'i':
        #     if player.inventory:
        #         player.check_inv()
        # elif cmd[0][0].lower() == 'r':
        #     player.current_room.room_describe()
        # elif cmd[0][0].lower() == 'c':
        #     player.self_describe()
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


if __name__ == '__main__':
    adventure_ish()