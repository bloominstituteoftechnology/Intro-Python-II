from room import Room
from player import Player, Monster

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
i = input("Welcome to Cavern of Marvelous Adventures! Please enter your name:\n")
player = Player(i, 100, 0, 0)
print(f"\nWelcome to your doom, {player.name}\n\n")
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
def parse(input):
    if input == "q" or input == "Q":
        exit(0)
    elif input == "Help" or input == "help" or input == "?":
        print(help())

def prompt(s):
    commands = "[Q|q] to quit | [N,S,E,W|n,s,e,w] to travel | [Help|?] for common commands:\n"
    prompt = " - What would you like to do? \t{}".format(commands)    
    return input(s + prompt)

def help():
    return """
        * [Q|q] to quit
        * [N,S,E,W|n,s,e,w] to travel
        * [i|I] [item] to inspect an item (ex: `i rock` to inspect an object named rock)
        """

while True:
    p = prompt("You are standing to the South of the mouth of what appears to be a large cavern. It's dark inside of the cavern, but you think you make out the shadow of what appears to be a foyer with connected rooms. There also appears to be something skittering on the floor.")
    parse(p)

#Create our player

#loop forever


#class object

#def inspect