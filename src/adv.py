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
def set_up_rooms():

    room['outside'].n_to = room['foyer']
    room['foyer'].s_to = room['outside']
    room['foyer'].n_to = room['overlook']
    room['foyer'].e_to = room['narrow']
    room['overlook'].s_to = room['foyer']
    room['narrow'].w_to = room['foyer']
    room['narrow'].n_to = room['treasure']
    room['treasure'].s_to = room['narrow']
    print("Have set up rooms")

# Add items to room:
def add_room_items():
    room['outside'].add_item(Item("Sword", f"a close range weapon used to defeat enemies, cut tall grass and break open clay pots"))
    room['foyer'].add_item(Item("Rupee", f"this is the primary local unit of currency and can be used to purchase items from the local store"))
    room['overlook'].add_item(Item("Hookshot", f"a spring-loaded, trigger -pulled hook attached to some lengthy chains. It can atttack enemies at a distance"))
    room['treasure'].add_item(Item("Key", f"this key looks like it would fit into a lock on a treasure chest"))
    room['narrow'].add_item(Item("Potion", f"drink this potion to replenish your health if you are running low"))
    print("Have added items to rooms")
#
# Main
#

# Make a new player object that is currently in the 'outside' room.

possible_directions = ['n', 's', 'e', 'w']
actions = ['take', 'drop', 't', 'd']

player_name = input('What is your name, adventure? ')
player = Player(player_name, room['outside'])
print(f"To move around the map press {possible_directions}. Look for items to help on your way. For help try 'Help' or 'h'.")
print(f"Good luck, {player.name}")


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

set_up_rooms()
add_room_items()
player.look()
    # Program Start:
    
    

    
    # REPL Start:
while True:
    user_input = input(f"What would you like to do {player.name}? ").lower().split()

    if len(user_input) > 2 or len(user_input) < 1:
        print(f"Sorry, {player.name}, thats not a valid one or two word command. Would you like 'help'?")

    elif len(user_input) == 2:
        if user_input[0] in actions:
            if user_input[0] == "t" or user_input[0] == "take":
                item = player.select_item(user_input[1])
                player.take(item)
            elif user_input[0] == "d" or user_input[0] == "drop":
                item = player.select_inventory_item(user_input[1])
                player.drop(item)

    else:
        if user_input[0] == "q" or user_input[0] == "quit":
            print(f"Thanks for playing {player.name}!")
            break

        elif user_input[0] == "h" or user_input[0] == "help":
            print("Commands:\n'n' - Move North\n's' - Move South\n'e' - Move East\n'w' - Move West\n't' or 'take '<item>' - Take Item\n'd' or 'drop' '<item>' - Drop Item\n'inv' or 'inventory' - Inventory Items\n'l' or 'look' - Look around in current room\n'h' or 'help' - Help menu\n'q' or 'quit' - Exit Game\n")
            continue

        elif user_input[0] == "l" or user_input[0] == "look":
            player.look()
            continue

        elif user_input[0] == "inv" or user_input[0] == "inventory":
            player.show_inventory()
            continue
        elif user_input[0] in possible_directions:
            try:
                player.change_room(user_input[0])
                print(f"You are in the {player.current_room.name}. \n{player.current_room.description}")
            except AttributeError:
                print(f"{player.name}'s adventure lies elsewhere.'")

        else:
            print(f"Movement not allowed! Please enter direction {possible_directions} to move around the map.")

