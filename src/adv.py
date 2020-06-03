from room import Room
from player import Adventurer

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'entrance': Room("Entrance", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm. A slimy set of stairs is barely be visible to your east."""),

    'grotto': Room("Grotto", """You carefully decend the wet steps. The smell of damp lime permeates the air. Finally you reach a turquoise lake.  Stalagmites grow from the floor and walls, making it impossible to continue on without getting into the ominous water..."""),

    'crag': Room("Crag", """The narrow passage along the crag bends here from west to north. The smell of gold permeates the cold breeze."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together
room['outside'].n_to = room['entrance']

room['entrance'].s_to = room['outside']
room['entrance'].n_to = room['overlook']
room['entrance'].e_to = room['crag']

room['overlook'].s_to = room['entrance']
room['overlook'].e_to = room['grotto']

room['crag'].w_to = room['entrance']
room['crag'].n_to = room['treasure']

room['treasure'].s_to = room['crag']

# add exits
room['outside'].exits['n'] = room['entrance']

room['entrance'].exits['s'] = room['outside']
room['entrance'].exits['n'] = room['overlook']
room['entrance'].exits['e'] = room['crag']

room['overlook'].exits['s'] = room['entrance']
room['overlook'].exits['e'] = room['grotto']

room['treasure'].exits['s'] = room['crag']



#
# Main
#

# Make a new player object that is currently in the 'outside' room.
adventurer = Adventurer(rooms['outside'])

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

print("Greetings Adventurer! You can move around the world using:")
print("\n n-> North \n s -> South \n e -> East \n w -> West")
print("you are currently at {adventurer.room}")

directions = ['n','s','e','w']
start = True

action = input(f'{adventurer.room} \n which way would you like to go? \n{prompt}')

while action != 'q':
    try:
        adventurer.room = adventurer.room.exits[action]
        action = input(f'{adventurer.room}\n\n{prompt}')
    except KeyError:
        action = input(f'Hmm.. It seems like there is no obvious way to do that.\n\n{prompt}')
