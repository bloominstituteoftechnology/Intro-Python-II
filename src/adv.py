from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'studio':  Room("Studio", """Dim light filters in from the south. Dusty
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

item = {
    "Katana": Item("Katana", "Slices Fruit"),
    "MIDI Keyboard": Item("MIDI Keyboard", "Produces Music")
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

room["treasure"].items = [
    str(item["Katana"]), str(item["Katana"])]
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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

name = input("Enter your name\n")

player = Player(name, room["outside"], items=["nickel", "good for flippin"])

while True:
    print(
        f"Current Room: {player.room.name}\nCurrent Items {player.items}\nItems in the Room {player.room.items}\n {player.room.description}")
    playerInput = input(
        "Enter N: Move North\nEnter S: Move South\nEnter E: Move East\nEnter W: Move West\nEnter Q: Enter q to quit\n")
    print(f"You moved {playerInput}\n")
    if playerInput == 'n' or playerInput == 's' or playerInput == 'w' or playerInput == 'e' or playerInput == 'q':
        if playerInput == "n":
            player.room = player.room.n_to
        elif playerInput == "s":
            player.room = player.room.s_to
        elif playerInput == "w":
            player.room == player.room.w_to
        elif playerInput == "e":
            player.room == player.room.e_to
        elif playerInput == "q":
            print("Game Over (For Now)")
            break
        else:
            print("Enter a cardinal direction on your keyboard")
