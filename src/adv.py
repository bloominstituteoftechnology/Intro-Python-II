from room import Room
from player import Player

print('Welcome to a Haunted House Adventure!')

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

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

name = input('Howdy, what is your name?')

player1 = Player(name, room['outside'])

dir = input(f'Start exploring, {player1.name}! You are in the {player1.room}Press [s] to move South, [n] for North, [e] for East, [w] for West, and [q] to quit: ')
for answer in dir:
    if answer not in ['n', 's', 'e', 'w', 'q']:
        print("Sorry that's not a possible direction!")
        continue
    elif answer == 'q':
        print('Thanks for playing!')
        break
    else:
        player_location = player1.room
        print(f'You are now in {player_location}: ')
        print(player_location.description)

        if dir == 'n':
            player_location = player_location.n_to
        elif dir == 's':
            player_location = player_location.s_to
        elif dir == 'w':
            player_location = player_location.w_to
        elif dir == 'e':
            player_location = player_location.e_to
        else:
            print("Oops you can't move that way")
        break  # to stop infinite loop


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
