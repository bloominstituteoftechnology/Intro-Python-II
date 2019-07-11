from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons."),

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

def hero():
    r = input("\n Are you a hero or villian?  ")
    if r.upper() == "HERO":
        return True 
    elif r.upper() == "VILLIAN":
        return False 
    else:
        print("\n Please type 'hero' or 'villian' ")
        return hero()

def getSpec():
    r = input("\n Are you Elvish, Human, or Wizard?  ")
    if r.upper() == "ELVISH" or r.upper() == "ELF":
        return "Elf" 
    elif r.upper() == "HUMAN":
        return "Human" 
    elif r.upper() == "WIZARD":
        return "Wizard"
    else:
        print("\n Please type 'Elf', 'Human', or 'Wizard' ")
        return hero()

# Make a new player object that is currently in the 'outside' room.

def newPlayer():
    name = input("\n What is your name, new adventurer?  ")
    good = hero()
    spec = getSpec()
    items = ["sword" , "antidote"]
    return Player(name, good, spec, room["outside"], items)

player = newPlayer()

action = ""

while action != "Q":
    print(f'Welcome {player.name}.\n')
    player.locate()
    # print(player.room.revealItems())

    action = input("Now what? \n [N] North [S] South [E] East [W] West [Q] Quit\n").upper()

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
