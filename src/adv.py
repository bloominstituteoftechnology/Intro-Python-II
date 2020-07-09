from room import Room
from player import Player
import sys
# Declare all the rooms
from colorama import init
from colorama import Fore, Back, Style

init()
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
player = Player(input('Adventurer! What is your name?: '), room['outside'])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#q
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

## Welcome the player!
def player_welcome():
    print(f'{Fore.GREEN}Welcome {player.name}{Style.RESET_ALL}\n{Fore.YELLOW}Exploring the map is easy! Just remember to (n)ever, (e)at, (s)oggy, (w)heaties, and you should be fine.\nIf you desire to leave for any reason,{Style.RESET_ALL}{Fore.RED} enter "q".{Style.RESET_ALL}')
    print(f'You stand in the {player.current_room.name}\n{player.current_room.description}')
    ## need if playname is set, then don't run this function

## function for commands the player can input 
def select_command():
    player_input = (input('What would you like to do? '))
    if player_input == 'q': 
        player_quit()
    elif player_input == 'n' or player_input == 'e' or player_input == 's' or player_input == 'w':
        player.movePlayer(player_input)
        print()
        print(f'{Fore.BLUE}{player.current_room.name}{Style.RESET_ALL}\n{player.current_room.description}')
        print()
    else:
        print(f'{Fore.RED}Please use n, e, s, w{Style.RESET_ALL}')
        
## function to quit
def player_quit():
    print(f'{Fore.RED}Are you sure you want to leave? There is stuff to find!{Style.RESET_ALL}')
    quit = (input('Enter "y" to leave. Enter "n" to continue adventuring. '))
    if quit == 'n':
        print('Good choice!')
        select_command()
    elif quit == 'y':
        print("Good bye!")
        sys.exit()
    else:
        print("Please select 'n' or 'y'")

## game start
player_welcome()

#Here's the loop
while True:
    select_command()