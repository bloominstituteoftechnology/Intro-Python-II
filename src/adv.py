from room import Room
from player import Player
from direction import Direction
from item import Item

# Declare all the rooms

rooms = {
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

rooms['outside'].n_to = rooms['foyer']
rooms['foyer'].s_to = rooms['outside']
rooms['foyer'].n_to = rooms['overlook']
rooms['foyer'].e_to = rooms['narrow']
rooms['overlook'].s_to = rooms['foyer']
rooms['narrow'].w_to = rooms['foyer']
rooms['narrow'].n_to = rooms['treasure']
rooms['treasure'].s_to = rooms['narrow']


rooms['foyer'].items.append(Item("Sword", "A sharp length of metal"))

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player_one = Player("Player One", rooms['outside'])

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

print('')



# Parsing

def parse_word(verb: str):
    for direction in Direction:
        if verb== direction.value:
            player_one.move(direction)
            break
    
    if verb == 'q':
        print("Thanks for playing!")
        exit()

def parse_words(verb: str, obj: str):
    if verb == 'get' or verb == 'take':
        for item in player_one.current_room.items:
            if obj.lower() == item.name.lower():
                player_one.take(item)
                return
        print("There are no items in the room by that name")
    elif verb == 'drop':
        for item in player_one.inventory:
            if obj.lower() == item.name.lower():
                player_one.drop(item)
                return
        print("You don't have any items in your inventory by that name")
    else:
        print("You must enter a valid command! Accepted verbs are 'get' 'take' and 'drop'")


# REPL

while True:
    print(player_one.current_room.name)
    print(player_one.current_room.description)
    if len(player_one.current_room.items) > 0:
        print("Items in the room:")
        for item in player_one.current_room.items:
            print(f"{item.name}: {item.description}")

    command = input("\nEnter a command: ")
    print('')

    words = command.split()
    
    if len(words) == 1:
        parse_word(words[0])
    elif len(words) == 2:
        parse_words(words[0], words[1])
    