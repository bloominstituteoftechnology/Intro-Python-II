from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("rope", "A rope lies here, ropily"), Item("mirror", "A dusty old mirror.  Who the crap leaves a mirror outside a cave"), Item("buttfor", "A buttfor dangles on a nearby flagpole.  What's a buttfor?")]),

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
player = Player(room['outside'])


def try_direction(direction, current_room):
    attribute = direction + "_to"

    if hasattr(current_room, attribute):
        return getattr(current_room, attribute)
    else:
        print("You can't go that way!")
        return current_room
# Write a loop that:
#


while True:

    # * Prints the current room name
    print(player.current_room.name)
    # * Prints the current description (the textwrap module might be useful here)
    print(player.current_room.description)

    if len(player.current_room.loot) > 0:
        for item in player.current_room.loot:
            print(item.description)

    # * Waits for user input and decides what to do.
    s = input("\n").lower().split()

    if len(s) == 1:
        s = s[0][0]
        if s == 'q':
            break
        player.set_current_room(try_direction(s, player.current_room))
        # player.current_room = try_direction(s, player.current_room)
    elif len(s) == 2:
        # * command
        first_word = s[0]
        second_word = s[1]
        loot_pile = player.current_room.loot
        name_list = [item.name for item in loot_pile]

        if first_word in ["get", "take", "drop"]:
            if first_word == "get" or "take":
                if second_word in name_list:
                    for item in loot_pile:
                        if item.name == second_word:
                            player.get_item(item)
                            loot_pile.remove(item)
                else:
                    print(f"You don't see a {second_word} here")

            elif first_word == "drop":
                print("droppin it")
            else:
                print("something went wrong")
        else:
            print("that's not a verb i allow goggs")
    else:
        print("invalid command")

    #
    # If the user enters a cardinal direction, attempt to move to the room there.

    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
