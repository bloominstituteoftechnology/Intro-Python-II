from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons", "Nothing"),

    'studio':  Room("Studio", """Dim light filters in from the south. Dusty
passages run north and east.""", "Katana"),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", "Nothing"),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", "Nothing"),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", "MIDI Keyboard"),
}

items = {
    "Katana": Item("Katana", "Shiny and sharp, please don't poke people with the pointy end", "Swing, Slice"),
    "MIDI Keyboard": Item("MIDI Keyboard", "12 Keys Black and White, One Hole, Two connections", "Music Powa")
}

# Link rooms together

room['outside'].n_to = room['studio']
room['studio'].s_to = room['outside']
room['studio'].n_to = room['overlook']
room['studio'].e_to = room['narrow']
room['overlook'].s_to = room['studio']
room['narrow'].w_to = room['studio']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room["treasure"].items = [items["Katana"], items["MIDI Keyboard"]]
#
# Main
#

currRoom = room["studio"]

name = input("Enter your name soldier\n")

# Make a new player object that is currently in the 'outside' room.
player = Player(name, room["outside"], items)
# Write a loop that:
#
# * Prints the current room name
# --> Look up room in dictionary...?
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

direction = ""

while True:
    print(
        f"Current space\n You are Carrying: {player.items}\n This room has these items: {player.room.items}\n {player.room.description}")
    directionChoice = input(
        "Pick a direction to move: n, w, s, or e, or enter q to quit\n")

    if directionChoice == "n" or directionChoice == "w" or directionChoice == "s" or directionChoice == "e" or directionChoice == "q":
        if directionChoice == "n":
            player.room == player.room.n_to
        elif directionChoice == "w":
            player.room == player.room.w_to
        elif directionChoice == "s":
            player.room == player.room.s_to
        elif directionChoice == "e":
            player.room == player.room.e_to
        # Quits the game
        elif directionChoice == "q":
            print("Ended the game")
            break
        else:
            print("Pick another way to walk friend")
