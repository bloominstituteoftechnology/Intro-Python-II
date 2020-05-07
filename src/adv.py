from colors import Colors
from room import Room
from player import Player
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = None

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

# get key with value function


def get_key(val):
    for key, value in room.items():
        if val == value:
            return key

    return "key doesn't exist"
# player approaches function


def player_approaches(player):
    print(f'{Colors.OKBLUE}Player approaches {player.location.name}...\n{player.location.description}{Colors.ENDC}')


while True:
    # prompts user to create new player
    if not player:
        prompt = input(
            f'\n{Colors.WARNING}*** WELCOME TO THE ADVENTURE GAME ***\n \nCreate a new character by typing in a name:{Colors.ENDC} ')
        if prompt == "q":
            print("Goodbye! Thanks for playing!")
            break
        else:
            player = Player(prompt, room['outside'])
            print(
                f'\n{Colors.OKGREEN}*** Created New Player ***\n\n{player}\n\n{Colors.ENDC}')
            currentRoom = get_key(player.location)
            print(
                f'{Colors.UNDERLINE}{Colors.WARNING}Current Location: {room[currentRoom].name}{Colors.ENDC}')
    # adventure game starts
    else:
        try:
            # initial prompt
            prompt = input(
                f'\nEnter Command or type "help" for a list of commands: ')
            # exit prompt
            if prompt.lower() == "q":
                print("Goodbye! Thanks for playing!")
                break
            # returns player info
            elif prompt.lower() == "player":
                print(
                    f'\n*** Player Info ***\n\n{player}\n\n\n*** Player Info End ***\n')
            # handles north navigation
            elif prompt.lower() == "n":
                print(f'\n{Colors.HEADER}Navigating......\n{Colors.ENDC}')
                if not player.location.n_to:
                    print('You see nothing interesting northward..')
                else:
                    player.setLocation(player.location.n_to)
                    player_approaches(player)
            # handles east navigation
            elif prompt.lower() == "e":
                print(f'{Colors.HEADER}Navigating...... {Colors.ENDC}')
                if not player.location.e_to:
                    print('You see nothing interesting eastward..')
                else:
                    player.setLocation(player.location.e_to)
                    player_approaches(player)
            # handles south navigation
            elif prompt.lower() == "s":
                print(f'{Colors.HEADER}Navigating...... {Colors.ENDC}')
                if not player.location.s_to:
                    print('You see nothing interesting eastward..')
                else:
                    player.setLocation(player.location.s_to)
                    player_approaches(player)
            # handles west navigation
            elif prompt.lower() == "w":
                print(f'{Colors.HEADER}Navigating...... {Colors.ENDC}')
                if not player.location.w_to:
                    print('You see nothing interesting eastward..')
                else:
                    player.setLocation(player.location.w_to)
                    player_approaches(player)
            else:
                print(
                    f'\n{Colors.FAIL}Command not recognized. Please try again{Colors.ENDC}\n')

        except ValueError:
            print('error')
