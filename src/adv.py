from room import Room, Item
from player import Player, Monster

# Declare all the rooms

rooms = {
    'outside':  Room("Outside Cave Entrance",
                     "You are standing to the South of the mouth of what appears to be a large cavern. It's dark inside of the cavern, but you think you make out the shadow of what appears to be a foyer with connected rooms. There also appears to be something skittering on the floor.",
                     [Item(1,
                            "chest",
                            "a battered wooden chest sits in the corner, its lock clearly having been picked by an adventurer before you. There's nothing you can do with this.",
                            0),
                      Item(0,                            
                            "torch",
                            "a crude stick with an oil soaked rag at its tip sits in the corner, hastily discarded.",
                            0)
                    ]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}

# Link rooms together

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']

room = rooms['outside']

#
# Main
#

# Print important messages
def sysPrint(s):
    print(f"\n***{s}***")
    
# Make a new player object that is currently in the 'outside' room.
i = input("Welcome to Cavern of Marvelous Adventures! Please enter your name:\n")
player = Player(i, 100, 0, 0)
sysPrint(f"\nWelcome to your doom, {player.name}")
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
def help():
    return """
            A friendly digitized voice that seems out of place in this dank, harsh environment says to you:

            * [l|L] to look around
            * [N,S,E,W|n,s,e,w] to travel
            * [i|I] [item] to inspect an item (ex: `i rock` to inspect an item named rock)
            * [t|T] [item] to take an item (ex: `t rock` to take a rock)
            * [Q|q] to quit

            Written on the wall nearby you see a message, hastily scrawled:
            The rock is a lie
        """

def parse(input):
    global room
    dirs = ["n", "N", "e", "E", "s", "S", "w", "W"]
    availableDirs = directions()
    
    if input == "q" or input == "Q":
        exit(0)
    elif input == "Help" or input == "help" or input == "?":
        print(help())

    elif input in dirs:
        for dir in availableDirs:
            dir = dir.lower
        if input in availableDirs:
            if input == "n" or input == "N":
                room = room.n_to
            elif input == "s" or input == "S":
                room = room.s_to
            elif input == "e" or input == "E":
                room = room.e_to
            elif input == "w" or input == "W":
                room = room.w_to
        else:
            sysPrint("There's nothing in that direction. Try again.")
    elif input == "l" or input == "L":
        look()
    else:
        sysPrint("invalid command")

def look():
    sysPrint("You look around the room and see:")
    #empty line
    print()    
    print("\n".join([str(x) for x in room.items]))

def inspect(item):
    print(item.description)

def directions():
    directions = []

    if hasattr(room, "n_to"):
        directions.append("n")
        directions.append("N")
    if hasattr(room, "s_to"):
        directions.append("s")
        directions.append("S")
    if hasattr(room, "e_to"):
        directions.append("e")
        directions.append("E")
    if hasattr(room, "w_to"):
        directions.append("w")
        directions.append("W")

    return directions

def prompt(s):
    # print a lit of commands, printing every other element in directions as a str
    commands = f"([l|L] to look around | {' | '.join(directions()[::2])} to travel | [q|Q] to quit | [Help|?] for common commands): "
    prompt = f"\nWhat would you like to do, {player.name}? {commands}"

    return input(s + prompt)

while True:
    p = prompt(f"\n{room.description}\n")
    parse(p)
#def inspect