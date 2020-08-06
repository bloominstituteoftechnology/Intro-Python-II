from room import Room
from player import Player
from item import Item

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

# make some items

foyer_items = [Item("dagger", "sharp with a wooden handle")]
overlook_items = [Item("rock", "round and dull"), Item("torch", "unlit")]
narrow_items = [Item("branch", "jagged with two leaves")]
treasure_items = [Item("coin", "nice and shiny!")]

# put items in room
room['foyer'].add_items(foyer_items)
room['overlook'].add_items(overlook_items)
room['narrow'].add_items(narrow_items)
room['treasure'].add_items(treasure_items)

# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player("Player 1", room["outside"])

# TODO: add player input for name

print(f"Welcome to your adventure {player.name}!\n")
print("""How to play:
Movement: (n,e,s,w)
See inventory: (i or inventory)
Pickup item: (get/take 'item')
Drop item: (drop 'item')
Location: (loc)
Quit: (q)
""")

while True:
    player.location()

    command = input("> ").split(' ')
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
    if command[0] == 'q':
        print("Till next time adventurer!")
        break
    else:
        player.command(command)