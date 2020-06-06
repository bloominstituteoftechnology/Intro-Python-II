
# Declare all the rooms
from src.item import Item
from src.room import Room
from src.player import Player

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
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

item = {
    'rock': Item("Rock", "Stones you can throw"),
    'stick': Item("Stick", "You can hit with a stick"),
    'shield': Item("Shield", "You can block"),
    'dagger': Item("Dagger", "You can stab with it"),
    'gold': Item("Gold", "You can become rich")
}

room['outside'].items.append(item['rock'])
room['foyer'].items.append(item['stick'])
room['overlook'].items.append(item['shield'])
room['narrow'].items.append(item['dagger'])
room['treasure'].items.append(item['gold'])

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player('Charles', room['outside'])

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

exitGame = False

while not exitGame:
    print(f"You are here {player.room.name}")
    print(f"You are here {player.room.description}")

    userInput = input("Where do you want to go?")

    if userInput == "q":
        print("Give me a sec..Done")
        exitGame = True
        break
    elif userInput == "n":
        if player.room.n_to is not None:
            player.room = player.room.n_to
        else:
            print("No room here")
    elif userInput == "e":
        if player.room.e_to is not None:
            player.room = player.room.e_to
        else:
            print("No room here")
    elif userInput == "w":
        if player.room.w_to is not None:
            player.room = player.room.w_to
        else:
            print("No room here")
    elif userInput == "s":
        if player.room.s_to is not None:
            player.room = player.room.s_to
        else:
            print("No room here")
    else:
        print("Not allowed")
