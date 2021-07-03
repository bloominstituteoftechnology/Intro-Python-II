from room import Room
from player import Player
from os import system, name

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


def clear_screen():
    _ = system('cls' if name == 'nt' else 'clear')


#
# Main
#

def adventure_game():
    clear_screen()

    print(f'\nWelcome!')

    player = Player(input(f'\nWhat is your name?'), room['outside'])
    print(f'\nWelcome {player.name}!\n')
    print(f'You are currently at the {player.current_room.name}\n')

    cmd = ''

    while cmd != 'q':
        # Dict for movement
        room_movement = {
            'n': player.current_room.n_to,
            's': player.current_room.s_to,
            'e': player.current_room.e_to,
            'w': player.current_room.w_to
        }

        cmd = input('\nWhat would you like to do?'
                    '\nType n, s, e or w to move and q to quit\n')

        if cmd in room_movement.keys():
            clear_screen()
            if room_movement[cmd]:
                player.move(room_movement[cmd])
                player.current_room.room_description()
            else:
                print(f'\nYou can not go there!')
        elif cmd != 'q':
            clear_screen()
            print(f'\nThat is not a valid command!')

    clear_screen()
    print('Bye bye!')


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

if __name__ == '__main__':
    adventure_game()
