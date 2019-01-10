from room import Room
from player import Player
from item import Item
import textwrap as tw

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


items = {
    'flashlight': Item("flashlight", "A device that provides a light source."),
    'mysterious_box': Item("mysterious_box", "A locked box of unknown origin.")
}

room['outside'].add_item(items['flashlight'])
room['outside'].add_item(items['mysterious_box'])


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player = Player(room['outside'])

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


def try_direction(direction):
    attribute = direction[0].lower() + "_to"

    if hasattr(player.current_room, attribute):
        return getattr(player.current_room, attribute)
    else:
        print("There's nothing there!")
        return player.current_room


print(tw.dedent(
    f"""
    You are in room: {player.current_room.name}
    {player.current_room.description}!
"""))

help_str = tw.dedent('''\
    What would you like to do?
    [check surroundings] Look around
    [check inventory] Show inventory
    [get <item>] or [take <item>] Put <item> in your inventory
    [drop <item>] Remove item from your inventory
    [<go, move> <n, e, s, w>] Go North, East, South, or West
    [help] check options
    [q] Quit
''')

print(help_str)

while True:
    command = input("> ").lower().split()

    if len(command) == 1:
        verb = command[0]
        if verb == "help":
            print("\n" + help_str)
            continue
        elif verb == "q":
            print("\nGoodbye!\n")
            break
        else:
            print("Invalid input. Type help for options.\n")
    elif len(command) == 2:
        verb, noun = command[0], command[1]
    else:
        command = print("Invalid input. Type help for options.\n")
        continue

    if verb == "get" or verb == "take":
        if isinstance(noun, str):
            if noun in items:
                item = items[noun]
                if item in player.current_room.items:
                    player.take_item(item)
                    player.current_room.remove_item(item)
                    item.on_take()
                else:
                    print(tw.dedent(f"That item is not in {player.current_room}, \
                            please try again\n"))
                    continue
            else:
                input("That's not an item, please try again\n")
                continue

    elif verb == "drop":
        if isinstance(noun, str):
            if noun in items:
                item = items[noun]
                if item in player.inventory:
                    player.drop_item(item)
                    player.current_room.add_item(item)
                    item.on_drop()

    elif verb == "go" or verb == "move":
        player.move_to(try_direction(noun))

    elif verb == "check":
        if noun == "inventory":
            player.show_inventory()
        elif noun == "surroundings":
            print(player.current_room.items)
        else:
            print("You can't check that!\n")

    else:
        print("\nInvalid input. Type help for options.\n")
