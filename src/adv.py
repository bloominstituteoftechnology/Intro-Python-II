from room import Room
from player import Player
from items import Item
# Declare all the rooms


room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("torch", "old torched that has been used")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("boots", "a pair of worn out boots")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("rusted knife", "rusty knife used for home use")]),

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


# Make a new player object that is currently in the 'outside' room.
print("\nEnter n to go north, s to go south, w, to go west, e to go east, q to exit the game.")
print("\nIf there are item in the room, input 'get' to take or 'drop' to drop it.")
name = input("Enter your name: ")
player = Player(name, room["outside"])


# direction is the direction the user input
# current_room is the current room the player is in

# return the new room that the player moves to if the
# move was succesful or returns the current room if
# the move was not successful


def try_direction(direction, current_room):
    attribute = direction + '_to'
    # See if the inputted direction is the one we can move to
    if hasattr(current_room, attribute):
        # fetch the new room
        return getattr(current_room, attribute)
    else:
        print("You can't go that way")
        return current_room


print("\n", player)
# Write a loop that:
#
item_name = ""

while True:
    # * Prints the current room name
    print("\n", player.current_room.name)
    # print out items in that room
    print(f"This room has the current items: {player.current_room.items}")
    # * Prints the current description (the textwrap module might be useful here).
    print(player.current_room.description)

    # * Waits for user input and decides what to do.
    s = input("\n> ").lower().split()
    grab_item = False
    if len(s) == 1:
        s = s[0]
        if s == 'q':
            break
        player.current_room = try_direction(s, player.current_room)

    # condition for picking up and dropping items
    elif len(s) == 2:
        action = s[0]
        item_name = s[1]
    # array of item in current room

    # array of item in player inventory

        if action == 'get':
            print(player.current_room.items)
            for item in player.current_room.items:
                if item.name == item_name:
                    player.inventory.append(item)
                    grab_item = True
                    print(f"You took {item_name} from {player.current_room.name}")
                    break
    
                    
            if grab_item:
                for item in player.inventory:
                    if item in player.current_room.items:
                        player.current_room.items.remove(item)
                        break
        elif action == 'drop':
            for item in player.inventory:
                if item.name == item_name:
                    player.inventory.remove(item)
                    player.current_room.items.append(item)
                    print(f"You dropped {item_name}")
    # If the user enters a cardinal direction, attempt to move to the room there.

    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
