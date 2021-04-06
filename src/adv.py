from player import Player
from room import Room

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

player = Player(room['outside'], "player one has arrived outside the room.")

def instructions():
    return """
        Welcome to the labyrinth dear wanderer...

        * use [L] to look around
        * [N,S,E,W] [North, South, East, West] [Up, Down, Right, Left] to travel in those directions
        * [q] to quit
    """

def current_dirs():
    currentDirs = directions()

    if currentDirs.__contains__("n"):
        currentDirs.extend(["north", "up", "forward", "forwards"])
    if currentDirs.__contains__("s"):
        currentDirs.extend(["south", "down", "backward", "backwards"])
    if currentDirs.__contains__("e"):
        currentDirs.extend(["east", "right"])
    if currentDirs.__contains__("w"):
        currentDirs.extend(["west", "left"])

    return currentDirs

def directions():
    directions = []

    if hasattr(player.current_room, "n_to"):
        directions.append("n")
    if hasattr(player.current_room, "s_to"):
        directions.append("s")
    if hasattr(player.current_room, "e_to"):
        directions.append("e")
    if hasattr(player.current_room, "w_to"):
        directions.append("w")

    return directions

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.

def travel(input):

    input = input.lower()
    if input in current_dirs():
        if input == "n" or input == "north" or input == "up" or input == "forward" or input == "forwards":
            player.current_room = player.current_room.n_to
        elif input == "s" or input == "south" or input == "down" or input == "backward" or input == "backwards":
            player.current_room = player.current_room.s_to
        elif input == "e" or input == "east" or input == "right":
            player.current_room = player.current_room.e_to
        elif input == "w" or input == "west" or input == "left":
            player.current_room = player.current_room.w_to
    else:
        print("Wrong Way! There's nothing over there.")

def prompt(s):
    # print a quicklist of commands
    commands = f"(L to look around | {' | '.join(directions())} to travel | Q to quit | [Help|?] for common commands): "
    prompt = f"\nWhat would you like to do, {player.name}?\n{commands}"

    return input(s + prompt)


#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
