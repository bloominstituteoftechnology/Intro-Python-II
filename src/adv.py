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
    'this': Item("this", "this item"),
    'that': Item("that", "that item")
}

room['outside'].add_item(items['this'])
room['outside'].add_item(items['that'])


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

print(tw.dedent(
    f"""\
    You are in room: {player.current_room.name}
    {player.current_room.description}!\
    """))

print(tw.dedent('''
        What would you like to do?
        [n] Go North [e] Go East [s] Go South [w] Go West
        [l] Look around
        [get <item>] or [take <item>] Put <item> in your inventory
        [drop <item>] Remove item from your inventory
        [i] Show inventory
        [q] Quit
    '''))

while True:
    choice = input()

    if choice.count(" ") > 1:
        choice = input("\nInvalid input.\n")
    elif choice.count(" ") == 1:
        verb, noun = choice.split(" ")
    else:
        verb = choice

    if verb == "get" or verb == "take":
        if isinstance(noun, str):
            if noun in items:
                item = items[noun]
                if item in player.current_room.items:
                    player.take_item(item)
                    player.current_room.remove_item(item)
                    item.on_take()
                else:
                    # TODO
                    print(f"That item is not in {player.current_room}")
            else:
                # TODO
                input("That's not an item, please try again")

    elif verb == "drop":
        if isinstance(noun, str):
            if noun in items:
                item = items[noun]
                if item in player.inventory:
                    player.drop_item(item)
                    player.current_room.add_item(item)
                    item.on_drop()

    elif verb == "q" or verb == "Q":
        print("goodbye!")
        break

    elif verb == "i" or verb == "I":
        player.show_inventory()

    elif verb == "n" or verb == "N":
        if isinstance(player.current_room.n_to, Room):
            player.move_to(player.current_room.n_to)
        else:
            print("There is nothing ahead of you.")

    elif verb == "s" or verb == "S":
        if isinstance(player.current_room.s_to, Room):
            player.move_to(player.current_room.s_to)
        else:
            print("There is nothing behind you.")

    elif verb == "w" or verb == "W":
        if isinstance(player.current_room.w_to, Room):
            player.move_to(player.current_room.w_to)
        else:
            print("There is nothing to the left of you.")

    elif verb == "e" or verb == "E":
        if isinstance(player.current_room.e_to, Room):
            player.move_to(player.current_room.e_to)
        else:
            print("There is nothing to the right of you.")

    elif verb == "l" or verb == "L":
        print(player.current_room.items)
