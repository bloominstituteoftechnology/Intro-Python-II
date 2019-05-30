import sys

from room import Room
from player import Player

# Declare all the rooms

thief = Player('Kjadra, The Cunning', 1, 2, 'Human', 'Thief')
brawler = Player('Yaegar, The Mighty', 3, 8, 'Orc', 'Brawler')

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 
                     thief, 
                     ['Iron Sword', 'Iron Shield', '5 Gold Pieces', 'Wine']),

    'foyer':    Room("Foyer", 
                     """Dim light filters in from the south. Dusty passages run north and east.""",
                     brawler,
                     ['Silver Helmet', '15 Gold Pieces', 'Goblet'] ),

    'overlook': Room("Grand Overlook", 
                     """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in
                        the distance, but there is no way across the chasm.""",
                    items=['The Skeleton Key', 'The Sword of 1000 Truths']),

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

def createCharacter():
    races = ['', 'Night Elf', 'High Elf', 'Human', 'Orc', 'Jin', 'Draconian']
    classes = ['', 'Shadow Priest', 'Bard', 'Warlord', 'Nighthawk', 'Mage', 'Sentinel', 'Bounty Hunter', 'Smuggler']

    name = input("What is the name of your hero? ")
    race = int(input("What is your race? 1 - Night Elf, 2 - High Elf, 3 - Human, 4 - Orc, 5 - Jin, 6 - Draconian "))
    archetype = int(input("What is your class? 1 - Shadow Priest, 2 - Bard, 3 - Warlord, 4 - Nighthawk, 5 - Mage, 6 - Sentinel, 7 - Bounty Hunter, 8 - Smuggler "))

    if race < 0 or race > 6: 
        race = 3 #default to creating human 

    if archetype < 0 or archetype > 8:
        archetype = 3 # default to Warlord 

    return Player(name, 3, races[race], classes[archetype], current_room=room['outside'])

player = createCharacter()

def getMove(player):
    print(f'{player.current_room}')
    print(f'Your available moves are: {player.getAvailableRooms()}')

    legal_moves = player.getAvailableRooms()
    move = ""

    while move not in legal_moves.keys():
        move = input('Which direction would you like to go? (N, S, E, W) ')
        if move == 'q' or move == 'Q':
            print('Thanks for playing!')
            sys.exit()

    if move == 'N' or move == 'n':
        player.current_room = player.current_room.n_to
    if move == 'S' or move == 's':
        player.current_room = player.current_room.s_to
    if move == 'E' or move == 'e':
        player.current_room = player.current_room.e_to
    if move == 'W' or move == 'w':
        player.current_room = player.current_room.w_to

print(player.current_room)
getMove(player)
print(player.current_room)